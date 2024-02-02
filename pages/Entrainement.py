import streamlit as st
import datetime
from datetime import date
from functions import *
import pandas as pd

st.set_page_config(
    page_icon=':file_folder:'
)

st.title("Entraînement")
st.write("---")
st.subheader("Données existantes")
if st.button("Afficher tableau"):
    df_full = get_données()
    st.write(df_full)


st.write("---")
st.subheader("Ajout de données")


# ------------
form_publishedsince = st.number_input('Ancienneté de l\'annonce (en jours)', min_value=0, step=1)
st.write(" ")
# ------------
form_carmodel_input = st.selectbox("Modèle de voiture",get_list_voitures())
index_carmodel = [index for index, value in enumerate(get_list_voitures()) if value == form_carmodel_input]
form_carmodel = index_carmodel[0]
st.write(" ")

# ------------
form_price = st.number_input('Prix', min_value=0, step=1)
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
    'price': [form_price],
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

if st.button("Aperçu"):

    # st.write(data)    
    df = pd.DataFrame(data)
    st.write(df)
    # retour = predict(data)
    # st.markdown(retour)
    # print(retour)

if st.button("Ajouter voiture"):

    # st.write(data)    
    df = pd.DataFrame(data)
    IsAdded = add_voiture(df)
    if IsAdded:
        st.write("Ajouté avec succès")
    # retour = predict(data)
    # st.markdown(retour)
    # print(retour)

st.write("---")
st.subheader("Entraînement d'un modèle")
st.text("Mettre à jour un modèle en l'entraînant avec les nouvelles données")
# ------------
selected_model = st.selectbox("Modèle",get_list_model())
st.write(" ")
# ------------

if st.button("Entraîner modèle"):
    df_training = get_données()
    IsTrained = train_model(df_training, selected_model)
    if IsTrained:
        st.write("Modèle entraîné avec succès")


# Noms dans la sidebar
st.sidebar.markdown("Ahmed Amine BOUTHALEB")
st.sidebar.markdown("Fatima OUDAHMANE")
st.sidebar.markdown("Ayse YILDRIM")
st.sidebar.markdown("Florian ALVAREZ RODRIGUEZ")