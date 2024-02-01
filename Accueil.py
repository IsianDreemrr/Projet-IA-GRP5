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

st.write("Bienvenue sur notre Web App !")
st.write("---")
st.header("Estimation")
st.subheader("Estimez le bien de votre voiture")
st.write("---")

# ------------
form_publishedsince = st.number_input('Ancienneté de l\'annonce (en jours)', min_value=0, step=1)
st.write(" ")
# ------------
form_carmodel = st.text_input("Modèle de voiture")
st.write(" ")
# ------------
form_annee = st.slider("Année", 1950, 2024)
st.write(" ")
# ------------
form_miseencirculation = st.date_input("Mise en circulation", datetime.date(int(date.today().year), int(date.today().month), int(date.today().day)))
st.write(" ")
# ------------
form_controletechnique = st.radio("Contrôle technique", ["non requis","requis"])
st.write(" ")
# ------------
form_kilometrage = st.number_input('Kilométrage', min_value=0, step=1)
st.write(" ")
# ------------
form_energie = st.radio("Energie", ["Essence","Diesel", "Hybride essence électrique", "Electrique", "Hybride diesel électrique", "Bicarburation essence GPL", "Bicarburation essence bioéthanol"])
st.write(" ")
# ------------
form_boitedevitesse = st.radio("Boite de vitesse", ["mécanique","automatique"])
st.write(" ")
# ------------
form_couleurexterieure = st.text_input("Couleur extérieure")
st.write(" ")
# ------------
form_nombredeportes = st.slider("Nombre de portes", 2, 8)
st.write(" ")
# ------------
form_nombredeplaces = st.slider("Nombre de places", 1, 8)
st.write(" ")
# ------------
form_garantie_input = st.slider("Garantie (en nombre de mois)", 0, 60)
form_garantie = str(form_garantie_input)+" mois"
st.write(" ")
# ------------
form_premieremain = st.radio("Première main ?", ["oui","non"])
st.write(" ")
# ------------
form_nombredeproprietaires = st.slider("Nombre de propriétaires", 0, 5)
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
form_consommationmixte = st.number_input("Consommation mixte (en l/100km)", min_value=0.0, step=0.1)
st.write(" ")
# ------------
form_normeeuro = st.radio("Norme européenne", ["EURO2","EURO3","EURO4","EURO5","EURO6",])
st.write(" ")
# ---- OPTIONS ----
form_options = []
# ------------
st.write(" ")
form_departement = st.number_input("Département", min_value=1, step=1)
st.write(" ")
form_id = st.number_input("Identifiant", min_value=0, step=1)
st.write(" ")

# ---- Garantie : Doublon avec l'autre colonne un peu plus haut, mais les valeurs sont potentiellement différentes car ici
# il a la mention "Garantie constructeur" qui existe ----
form_warranty_input = st.radio("Type garantie", ["Garantie constructeur","Garantie","Aucune"])
if form_warranty_input == "Garantie":
    form_warranty = "Garantie "+str(form_garantie)+" mois"
elif form_warranty_input == "Aucune":
    form_warranty = ""
else:
    form_warranty = "Garantie constructeur"

st.write(" ")

# ---- Vendeur : Cette colonne ne sert pas à grand chose vu qu'il n'y a que "Professionnel" comme valeur existante, ou alors [vide]... ----
form_vendeur_input = st.radio("Type de vendeur", ["Professionnel","Particulier","Non-renseigné"])
if form_warranty_input == "Non-renseigné":
     form_vendeur = ""
else:
    form_vendeur = form_vendeur_input
st.write(" ")
# ------------
form_verifieetgaranti = st.text_input("Vérifié et garanti par")
st.write(" ")
# ------------
form_rechargeable_input = st.checkbox("Rechargeable ?")
if form_rechargeable_input:
    form_rechargeable = "oui"
else:
    form_rechargeable = "non"
st.write(" ")
# ------------
form_autonomiebatterie_input = st.number_input('Autonomie de la batterie (en Km)', min_value=0, step=1)
form_autonomiebatterie = str(form_autonomiebatterie_input) + " Km"
st.write(" ")
# ------------
form_capacitébatterie_input = st.number_input('Capacité de la batterie (en kWh)', min_value=0.0, step=0.1)
form_capacitébatterie = str(form_capacitébatterie_input) + " kWh"
st.write(" ")


data = {
    'publishedsince': [form_publishedsince],
    'carmodel': [form_carmodel],
    'année': [form_annee],
    'miseencirculation': [form_miseencirculation],
    'contrôletechnique': [form_controletechnique],
    'kilométragecompteur': [form_kilometrage],
    'énergie': [form_energie],
    'boîtedevitesse': [form_boitedevitesse],
    'couleurextérieure': [form_couleurexterieure],
    'nombredeportes': [form_nombredeportes],
    'nombredeplaces': [form_nombredeplaces],
    'garantie': [form_garantie],
    'premièremain(déclaratif)': [form_premieremain],
    'nombredepropriétaires': [form_nombredeproprietaires],
    'puissancefiscale': [form_puissancefiscale],
    'puissancedin': [form_puissancedin],
    'crit\'air': [form_critair],
    'émissionsdeco2': [form_emmissionsdeco2],
    'consommationmixte': [form_consommationmixte],
    'normeeuro': [form_normeeuro],
    'options': [form_options],
    'departement': [form_departement],
    'id': [form_id],
    'waranty': [form_warranty],
    'vendeur': [form_vendeur],
    'vérifié&garanti': [form_verifieetgaranti],
    'rechargeable': [form_rechargeable],
    'autonomiebatterie': [form_autonomiebatterie],
    'capacitébatterie': [form_capacitébatterie],
    }

if st.button("Estimer mon bien"):

    # st.write(data)    
    # df = pd.DataFrame(data)
    # st.write(df)
    retour = predict(data)
    st.markdown(retour)
    print(retour)

# Noms dans la sidebar
st.sidebar.markdown("Ahmed Amine BOUTHALEB")
st.sidebar.markdown("Fatima OUDAHMANE")
st.sidebar.markdown("Ayse YILDRIM")
st.sidebar.markdown("Florian ALVAREZ RODRIGUEZ")
