import joblib
import datetime
from datetime import date
import pandas as pd
import sklearn
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.ensemble import _gb_losses


from os import listdir
from os.path import isfile, join

# Prédire avec le modèle de régression linéaire par défaut
def predict(data):
    clf = joblib.load("./model/lr_model.sav")
    return clf.predict(data)

# Prédire avec un modèle généré par entrainement sur la Web App
def predict_with(data, model):
    clf = joblib.load("./model/"+model)
    return clf.predict(data)

# Récupération d'un dataframe 
def get_données(dataset="data_trained.csv"):
    df = pd.read_csv('./data/'+dataset)
    return df

# Ajout d'une ligne au dataset 
def add_voiture(df):
    df.to_csv('./data/data_trained.csv', mode='a', index=False, header=False)
    return True

# Récupération d'un dataframe 
def get_list_voitures(dataset="dataset_cleaned.csv"):
    df = pd.read_csv('./data/'+dataset)
    return df['carmodel'].unique()

# Récupération d'un dataframe 
def get_list_couleurexterieure(dataset="dataset_cleaned.csv"):
    df = pd.read_csv('./data/'+dataset)
    return df['couleurextérieure'].unique()

# Récupération d'un dataframe 
def get_list_couleurintérieure(dataset="dataset_cleaned.csv"):
    df = pd.read_csv('./data/'+dataset)
    return df['couleurintérieure'].unique()

# Récupération d'un dataframe 
def get_list_norme_euro(dataset="dataset_cleaned.csv"):
    df = pd.read_csv('./data/'+dataset)
    return df['normeeuro'].unique()

# Récupération de la liste de tous les modèles
def get_list_model():
    allfiles = [f for f in listdir("./model") if isfile(join("./model", f))]
    return allfiles

# Entraînement d'un modèle 
def train_model(df, selectedmodel="lr_model.sav"):
    X = get_données().drop(columns=['price'])  # Variables indépendantes
    y = get_données()['price']  


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    if selectedmodel == "lr_model.sav":
        model = LinearRegression() 
    elif selectedmodel == "ridge_model.sav":
        alpha = 1.0  # Paramètre de régularisation, ajustez-le au besoin
        model = Ridge(alpha=alpha) 

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)

    print("RMSE:", rmse)
    print("R^2:", r2)

    pickle.dump(model, open(selectedmodel, 'wb'))
    os.replace(selectedmodel, "./model/"+selectedmodel)
    return True