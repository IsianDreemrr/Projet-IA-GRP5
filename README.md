# Projet-IA-GRP5


# Projet

- **Projet de Machine Learning** : Ce projet implique l'utilisation de techniques de classification, régression, et clustering. Votre application inclura une **page analytique**, une **page d'entraînement**, et une page pour **utiliser les modèles entraînés**.

# Objectif

- **Estimation de prix** : Découvrez le prix estimé de votre voiture en remplissant un formulaire simple.
- **Analyse des données** : Visualisez les détails du dataset sur notre page analytique.
- **Amélioration de l'IA**
- **Modele 'IA** : Contribuez à l'amélioration de l'intelligence artificielle en ajoutant des données sur la page d'entraînement.

# Données

- Le dataset utilisé peut être trouvé sur Kaggle : [French Second Hand Car Data](https://www.kaggle.com/datasets/spicemix/french-second-hand-car/data).

# Algorithme

Les algorithmes suivants sont employés pour l'analyse et la prédiction des prix des voitures d'occasion :

- **Régression Linéaire** : Un modèle de base pour prédire la valeur continue (le prix) en fonction des variables indépendantes.
- **Ridge** : Une variation de la régression linéaire qui inclut la régularisation L2 pour éviter le surajustement.
- **Gradient Boosting** : Une méthode puissante qui construit des modèles de prédiction sous forme d'ensemble de modèles de prédiction faibles, typiquement des arbres de décision.
- **Random Forest** : Un ensemble d'arbres de décision pour la régression (et la classification), qui améliore la robustesse et la précision de la prédiction en moyennant les résultats de divers arbres.

 
# Commandes pour l'installation et le lancement de la Web App : 

(Dans le dossier du projet)
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install streamlit
pip install joblib
streamlit run accueil.py
