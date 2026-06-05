# Changelog

Toutes les modifications notables apportées à ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-05
### Ajouté
- Interface graphique moderne avec CustomTkinter.
- Lancement automatisé des analyses de convergence via `ansys-mechanical-core`.
- Extraction des métriques de contraintes, déplacements, énergie et qualité de maillage.
- Prise en charge dynamique du Scoping via Named Selection (`Face_critique_test`) ou fallback global.
- Affichage de graphiques lissés (Pchip) et interactifs via Matplotlib et mplcursors.
- Exports complets en CSV, Excel, PNG et rapports PDF (ReportLab).
- Algorithme de diagnostic automatique de la convergence et des singularités.