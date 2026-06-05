import System
import json

model = ExtAPI.DataModel.Project.Model

analysis = model.Analyses[0] if len(model.Analyses) > 0 else model.AddStaticStructuralAnalysis()

mesh = model.Mesh
analysis.ClearGeneratedData()
mesh.ElementSize = Quantity(SIZE, "mm")
mesh.GenerateMesh()
mesh.ComputeMeshQualityMetrics()

target_metrics = [
    MeshMetricType.ElementQuality,
    MeshMetricType.AspectRatio,
    MeshMetricType.JacobianRatioGaussPoints,
    MeshMetricType.Skewness,
]

available_metrics = mesh.GetVolumeMeshMetrics()
mesh_results = {}

for metric in available_metrics:
    if metric in target_metrics:
        mesh.SetActiveVolumeMeshQuality(metric, True)
        try:
            worst = mesh.GetVolumeMeshQualityWorstMetricValue(metric)
            avg   = mesh.GetVolumeMeshQualityAverageMetricValue(metric)
            mesh_results[metric.ToString()] = (float(worst.Value), float(avg.Value))
        except Exception as e:
            mesh_results[metric.ToString()] = (-999.0, -999.0)

analysis.Solve()
solution = analysis.Solution

# --- 1. RÉCUPÉRATION SÉCURISÉE DE LA NAMED SELECTION ---
ns_name = "Face_critique_test"
named_selections = []

if model.NamedSelections is not None:
    named_selections = [ns for ns in model.NamedSelections.Children if ns.Name == ns_name]

result = None

# --- 2. GESTION DU SCOPING AVEC FALLBACK ---
if len(named_selections) > 0:
    # La Named Selection existe ! On la récupère en toute sécurité.
    ns = named_selections[0]
    
    for c in solution.Children:
        if c.DataModelObjectCategory.ToString() == "EquivalentStress":
            try:
                if c.Location.Name == ns.Name:
                    result = c
                    break
            except:
                pass
                
    if result is None:
        result = solution.AddEquivalentStress()
        result.Location = ns
        result.Name = "Stress_Zone_Critique"
        
else:
    # La Named Selection N'EXISTE PAS -> Fallback (Plan B) sur toute la géométrie
    for c in solution.Children:
        if c.DataModelObjectCategory.ToString() == "EquivalentStress":
            try:
                if c.Location is None:
                    result = c
                    break
            except:
                result = c
                break
                
    if result is None:
        result = solution.AddEquivalentStress()
        result.Name = "Stress_Global"

disp_results = [c for c in solution.Children if c.DataModelObjectCategory.ToString() == "TotalDeformation"]
disp = disp_results[0] if len(disp_results) > 0 else solution.AddTotalDeformation()

energy_results = [c for c in solution.Children if (c.DataModelObjectCategory.ToString() == "StrainEnergy")
                  or (c.DataModelObjectCategory.ToString() == "UserDefinedResult" and c.Expression == "ENERGYPOTENTIAL")]

if len(energy_results) > 0:
    energy = energy_results[0]
else:
    energy = solution.AddUserDefinedResult()
    energy.Expression = "ENERGYPOTENTIAL"
    energy.Name = "Strain Energy"

solution.EvaluateAllResults()

# --- STRUCTURATION ET ENVOI EN JSON ---
out_data = {
    "stress_max": float(result.Maximum.Value),
    "stress_avg": float(result.Average.Value),
    "disp_max": float(disp.Maximum.Value),
    "energy_max": float(energy.Maximum.Value),
    "eq_min": float(mesh_results.get("ElementQuality", (-999, -999))[0]),
    "eq_avg": float(mesh_results.get("ElementQuality", (-999, -999))[1]),
    "ar_max": float(mesh_results.get("AspectRatio", (-999, -999))[0]),
    "ar_avg": float(mesh_results.get("AspectRatio", (-999, -999))[1]),
    "jr_min": float(mesh_results.get("JacobianRatioGaussPoints", (-999, -999))[0]),
    "jr_avg": float(mesh_results.get("JacobianRatioGaussPoints", (-999, -999))[1]),
    "sk_max": float(mesh_results.get("Skewness", (-999, -999))[0]),
    "sk_avg": float(mesh_results.get("Skewness", (-999, -999))[1]),
    "elements": int(mesh.Elements)
}

json.dumps(out_data)