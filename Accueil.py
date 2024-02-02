import streamlit as st
import datetime
from datetime import date
import pandas as pd
from functions import *


st.set_page_config(
    page_icon=':file_folder:'
)


st.title("Projet IA - Groupe 5")
st.write("---")



text_side = """
Bienvenue sur notre Web App!
Découvrez le prix estimé de votre voiture en remplissant un formulaire simple. 
Visualisez les détails du dataset sur notre page analytique. 
Contribuez à l'amélioration de l'IA en ajoutant des données sur la page d'entraînement.
"""

image_path = "f9e14c9e-facc-46d4-b5e1-1138baaaee9c.webp"


col1, col2 = st.columns([3, 2])  # Ajustez les proportions selon vos besoins


with col1:
    st.image(image_path, caption='', width=400)


with col2:
    st.write(text_side)


st.write("---")
st.header("Estimation")
st.subheader("Estimez la valeur de votre voiture")
st.write("---")

# ------------
form_publishedsince = st.number_input('Ancienneté de l\'annonce (en jours)', min_value=0, step=1)
st.write(" ")
# ------------
form_carmodel_input = st.selectbox("Modèle de voiture",get_list_voitures())
index_carmodel = [index for index, value in enumerate(get_list_voitures()) if value == form_carmodel_input]
form_carmodel = index_carmodel[0]
st.write(" ")
# ------------
form_annee = st.slider("Année", 1950, 2024)
st.write(" ")
# ------------
form_controletechnique_input = st.radio("Contrôle technique", ["Non requis","Requis"])
if form_controletechnique_input == "Non requis":
    form_controletechnique = 0
else:
    form_controletechnique = 1
st.write(" ")
# ------------
form_kilometrage = st.number_input('Kilométrage', min_value=0, step=1)
st.write(" ")
# ------------
list_energie = ["Essence","Diesel", "Hybride essence électrique", "Electrique", "Hybride diesel électrique", "Bicarburation essence GPL", "Bicarburation essence bioéthanol"]
form_energie_input = st.selectbox("Energie", list_energie)
index_energie = [index for index, value in enumerate(list_energie) if value == form_energie_input]
form_energie = index_energie[0]
st.write(" ")
# ------------
form_boitedevitesse_input = st.radio("Boite de vitesse", ["mécanique","automatique"])
if form_boitedevitesse_input == "mécanique":
    form_boitedevitesse = 0
else:
    form_boitedevitesse = 1
st.write(" ")
# ------------
form_couleurexterieure_input = st.selectbox("Couleur extérieure",get_list_couleurexterieure())
index_couleurexterieure = [index for index, value in enumerate(get_list_couleurexterieure()) if value == form_couleurexterieure_input]
form_couleurexterieure = index_couleurexterieure[0]
st.write(" ")
# ------------
form_nombredeportes = st.slider("Nombre de portes", 2, 8)
st.write(" ")
# ------------
form_nombredeplaces = st.slider("Nombre de places", 1, 8)
st.write(" ")
# ------------
form_garantie = st.slider("Garantie (en nombre de mois)", 0, 60)
st.write(" ")
# ------------
form_premieremain_input = st.radio("Première main ?", ["Oui","Non"])
if form_premieremain_input == "Oui":
    form_premieremain = 0
else:
    form_premieremain = 1
st.write(" ")
# ------------
form_puissancefiscale = st.number_input('Puissance fiscale (en CV)', min_value=0, step=1)
st.write(" ")
# ------------
form_puissancedin = st.number_input('Puissance DIN (en CH)', min_value=0, step=1)
st.write(" ")
# ------------
form_critair = st.slider("Indice Crit'air", 0, 5)
st.write(" ")
# ------------
form_emmissionsdeco2 = st.number_input("Emission de CO2 (en g/km)", min_value=0, step=1)
st.write(" ")

# ------------
form_normeeuro_input = st.selectbox("Norme européenne",get_list_norme_euro())
index_normeeuro = [index for index, value in enumerate(get_list_norme_euro()) if value == form_normeeuro_input]
form_normeeuro = index_normeeuro[0]
st.write(" ")
# ------------
st.write(" ")
form_departement = st.number_input("Département", min_value=1, step=1)
st.write(" ")

# ------------
form_vendeur = 0
# ------------
form_couleurintérieure_input = st.selectbox("Couleur intérieure",get_list_couleurintérieure())
index_couleurintérieure = [index for index, value in enumerate(get_list_couleurintérieure()) if value == form_couleurintérieure_input]
form_couleurintérieure = index_couleurintérieure[0]
st.write(" ")
# ------------

data = {
    'publishedsince': [form_publishedsince],
    'carmodel': [form_carmodel],
    'année': [form_annee],
    'contrôletechnique': [form_controletechnique],
    'kilométragecompteur': [form_kilometrage],
    'énergie': [form_energie],
    'boîtedevitesse': [form_boitedevitesse],
    'couleurextérieure': [form_couleurexterieure],
    'nombredeportes': [form_nombredeportes],
    'nombredeplaces': [form_nombredeplaces],
    'garantie': [form_garantie],
    'premièremain(déclaratif)': [form_premieremain],
    'puissancefiscale': [form_puissancefiscale],
    'puissancedin': [form_puissancedin],
    'crit\'air': [form_critair],
    'émissionsdeco2': [form_emmissionsdeco2],
    'normeeuro': [form_normeeuro],
    'departement': [form_departement],
    'vendeur': [form_vendeur],
    'couleurintérieure': [form_couleurintérieure],
    }

if st.button("Estimer mon bien"):

    # st.write(data)    
    # df = pd.DataFrame(data)
    # st.write(df)
    retour = predict(pd.DataFrame(data))
    st.markdown(retour)
    print(retour)

# Noms dans la sidebar
st.sidebar.markdown("Ahmed Amine BOUTHALEB")
st.sidebar.markdown("Fatima OUDAHMANE")
st.sidebar.markdown("Ayse YILDRIM")
st.sidebar.markdown("Florian ALVAREZ RODRIGUEZ")
