import joblib
import datetime
from datetime import date
import pandas as pd

from os import listdir
from os.path import isfile, join

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


# Récupération de la liste de tous les modèles
def get_list_model():
    allfiles = [f for f in listdir("./model") if isfile(join("./model", f))]
    return allfiles

# Entraînement d'un modèle 
def train_model(df, model="rl_model.sav"):
    # Code à faire
    return True