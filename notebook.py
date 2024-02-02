
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    chemin_fichier = 'dataset.csv'
    df = pd.read_csv(chemin_fichier)
    return df

#Nettoyage des données
def clean_data(df):
    df['publishedsince'] = df['publishedsince'].astype(str).str.extract('(\d+)').astype(int)
    df['carmodel'] = df['carmodel'].astype(str).replace('\n', '').str.strip()
    df['price'] = df['price'].astype(str).str.replace(' ', '').str.extract('(\d+)').astype(float)
    df['année'] = df['année'].fillna(0).astype(int)
    df['miseencirculation'] = pd.to_datetime(df['miseencirculation'], format='%d/%m/%Y', errors='coerce')
    df['kilométragecompteur'] = df['kilométragecompteur'].astype(str).str.extract('(\d+)').astype(float)
    df['puissancemoteur'] = df['puissancemoteur'].astype(str).str.extract('(\d+)').astype(float)
    df['voltagebatterie'] = df['voltagebatterie'].astype(str).str.extract('(\d+)').astype(float)
    df['année'] = df['année'].apply(lambda x: np.nan if x < 1885 else x)
    median_year = df['année'].median()
    df['année'].fillna(median_year, inplace=True)
    df['année'] = df['année'].astype(int)
    return df


def basic_analyses(df):
    analyses = {
        'Le type des données ': df.dtypes,
        'Valeurs manquantee ': df.isnull().sum(),
        'Statistique déscriptives ': df.describe(),
        'Années': sorted(df['année'].unique()),
        'Analyses sur les années': df['année'].describe(),
        'Analyse des prix': df['price'].describe(),
    }
    return analyses


def plot_correlations(df):
    correlations = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlations, annot=True, fmt=".2f", cmap='coolwarm')
    plt_path = "correlation_heatmap.png"
    plt.savefig(plt_path)
    plt.close()
    return plt_path, correlations


def generate_plots(df):
    plot_paths = {}

    
    plt.figure()
    df['price'].hist(bins=30)
    plt.title('Distribution des prix')
    plt.xlabel('Prix')
    plt.ylabel('Nombre de véhicules')
    hist_path = "price_histogram.png"
    plt.savefig(hist_path)
    plt.close()
    plot_paths['histogram prix '] = hist_path
    plot_paths['Boxplot énergie et prix'] = boxplot_energy_price(df)
    plot_paths['Scatterplot kilométrage et prix'] = scatterplot_km_price(df)
    plot_paths['Comptage types d\'énergie'] = countplot_energy(df)
    plot_paths['Tendance des prix par année'] = price_trend_by_year(df)


    plt.figure()
    sns.boxplot(x=df['price'])
    plt.title('Boxplot des prix')
    boxplot_path = "price_boxplot.png"
    plt.savefig(boxplot_path)
    plt.close()
    plot_paths['Boxplot prix '] = boxplot_path

    return plot_paths


def boxplot_energy_price(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='énergie', y='price', data=df)
    plt.title('Boxplot des prix par type d\'énergie')
    plt.xticks(rotation=45)  # Rotation des étiquettes si nécessaire
    boxplot_energy_path = "energy_price_boxplot.png"
    plt.savefig(boxplot_energy_path)
    plt.close()
    return boxplot_energy_path


def scatterplot_km_price(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='kilométragecompteur', y='price', data=df)
    plt.title('Relation entre kilométrage et prix')
    plt.xlabel('Kilométrage')
    plt.ylabel('Prix')
    scatter_km_price_path = "km_price_scatterplot.png"
    plt.savefig(scatter_km_price_path)
    plt.close()
    return scatter_km_price_path


def countplot_energy(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='énergie')
    plt.title('Distribution des types d\'énergie')
    plt.xticks(rotation=45)
    countplot_energy_path = "energy_distribution_countplot.png"
    plt.savefig(countplot_energy_path)
    plt.close()
    return countplot_energy_path


def price_trend_by_year(df):
    plt.figure(figsize=(10, 6))
    df.groupby('année')['price'].mean().plot(kind='line')
    plt.title('Prix moyen par année')
    plt.xlabel('Année')
    plt.ylabel('Prix moyen')
    price_trend_path = "price_trend_by_year.png"
    plt.savefig(price_trend_path)
    plt.close()
    return price_trend_path




#  Les résultats
def execute_all_analyses():
    df = load_data()
    df_cleaned = clean_data(df)
    analyses = basic_analyses(df_cleaned)
    plt_path, correlations = plot_correlations(df_cleaned)
    plot_paths = generate_plots(df_cleaned)
    return analyses, plt_path, correlations, plot_paths






