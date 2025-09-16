import streamlit as st
from fruit_manager import *


st.title("Dashboard de la Plantation")

inventaire = ouvrir_inventaire()
tresorerie = ouvrir_tresorerie()
prix = ouvrir_prix()

with st.sidebar:
    st.header("Vendre des Fruits")
    fruit_vendre = st.selectbox("Choisir un fruit à vendre", list(inventaire.keys()))
    quantite_vendre = st.number_input("Quantité à vendre", min_value=1, step=1)
    
    if st.button("Vendre"):
        inventaire, tresorerie = vendre(inventaire, fruit_vendre, quantite_vendre, tresorerie, prix)
    
    st.header("Récolter des fruits")
    fruit_recolter = st.selectbox("Choisir un fruit à récolter", list(inventaire.keys()), key="recolter")
    quantite_recolter = st.number_input("Quantité à récolter", min_value=1, step=1)
    
    if st.button("Récolter"):
        inventaire = recolter(inventaire, fruit_recolter, quantite_recolter)

st.header("Trésorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f}")

st.header("Inventaire")
st.table(inventaire)


if __name__ == "__main__":
    pass
