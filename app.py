import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Projeto veiculos")

st.write("Olá, Streamlit!")

dados = pd.DataFrame({
    "Mes": ["Jan", "Fev", "Mar"],
    "Vendas": [100, 200, 150]
})

fig = px.bar(
    dados,
    x="Mes",
    y="Vendas",
    title="Vendas por Mês"
)

st.plotly_chart(fig)
