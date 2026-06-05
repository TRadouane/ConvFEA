# ConvFEA — Automatisation des Études de Convergence FEA

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Ansys](https://img.shields.io/badge/Ansys-Mechanical-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**ConvFEA** est une application desktop développée en Python permettant d'automatiser entièrement les études de convergence de maillage sur des modèles **ANSYS Mechanical**. 

![Démo de ConvFEA](assets/demo.gif)

## Problématique résolue

La validation d'un modèle par éléments finis (FEA) exige de prouver que les résultats (contraintes, déplacements) sont indépendants de la taille du maillage. Manuellement, cette tâche est chronophage : itérer sur les tailles d'éléments, relancer le solveur, extraire les métriques de qualité et tracer les courbes d'erreur asymptotique.

**ConvFEA résout ce problème en un clic :**
L'outil pilote ANSYS en arrière-plan (via `ansys-mechanical-core`), itère sur une liste de tailles de maillage, extrait intelligemment les résultats et génère instantanément des graphiques de convergence, un diagnostic automatique et un rapport PDF prêt pour l'ingénierie.

## Fonctionnalités

- **Pilotage de Solveur :** Exécution d'Ansys Mechanical en mode silencieux (Batch) ou visuel.
- **Scoping intelligent :** Détection automatique d'une *Named Selection* ciblée (par défaut `Face_critique_test`). Si elle est absente, l'outil bascule sur la géométrie globale.
- **Extraction multicritères :**
  - Mécanique : Contraintes de Von Mises (max/moyenne), Déplacements, Énergie de déformation.
  - Qualité de maillage : Element Quality, Aspect Ratio, Jacobian Ratio, Skewness.
- **Data Visualisation interactive :** Courbes de convergence lissées (interpolation Pchip) avec info-bulles au survol.
- **Diagnostic IA-like :** Algorithme détectant les singularités géométriques, l'atteinte d'un palier asymptotique ou les éléments dégénérés.
- **Génération de Livrables :** Export des résultats en `.csv`, `.xlsx`, images `.png`, et rapport PDF complet auto-généré.

## Prérequis

1. **ANSYS Mechanical** installé sur votre machine (version 2022 R2 ou supérieure recommandée) avec une licence active.
2. **Python 3.10+**.

## Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/TRadouane/ConvFEA.git
   cd ConvFEA