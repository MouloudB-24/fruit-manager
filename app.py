import streamlit as st
from fruit_manager import *


st.title("Dashboard de la Plantation")

inventaire = ouvrir_inventaire()
tresorerie = ouvrir_tresorerie()
prix = ouvrir_prix()

st.header("Trésorerie")
st.metric(label="Montant disponible", value=f"{tresorerie:.2f}")

st.header("Inventaire")
st.table(inventaire)


if __name__ == "__main__":
    pass
