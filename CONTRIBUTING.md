# Contribuer à ConvFEA

Merci de l'intérêt que vous portez à ce projet ! Toutes les contributions sont les bienvenues, qu'il s'agisse de signalement de bugs, de suggestions de fonctionnalités ou de pull requests.

## Comment contribuer ?

1. **Signaler un bug ou demander une fonctionnalité :** Ouvrez une "Issue" sur GitHub en décrivant clairement le problème ou la demande.
2. **Soumettre du code :**
   - Forkez le dépôt.
   - Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`).
   - Commitez vos changements (`git commit -m 'Add some AmazingFeature'`).
   - Poussez la branche (`git push origin feature/AmazingFeature`).
   - Ouvrez une Pull Request.

## Règles de développement
- Afin de faciliter la distribution de l'exécutable, le code principal de l'interface doit rester dans le fichier source principal.
- Assurez-vous que le script Mechanical (`src/mechanical_script.py`) reste compatible avec l'API IronPython d'Ansys.