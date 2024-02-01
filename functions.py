import joblib
import datetime
from datetime import date
import pandas as pd

# Prédire avec le modèle de régression linéaire par défaut
def predict(data):
    clf = joblib.load("./model/rl_model.sav")
    return clf.predict(data)

# Prédire avec un modèle généré par entrainement sur la Web App
def predict_with(data, model):
    clf = joblib.load("./model/"+model)
    return clf.predict(data)

# Récupération d'un dataframe 
def get_données(dataset="dataset_trained.csv"):
    df = pd.read_csv('./data/'+dataset)
    return df

# Ajout d'une ligne au dataset 
def add_voiture(df):
    df.to_csv('./data/dataset_trained.csv', mode='a', index=False, header=False)
    return True