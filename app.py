import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_excel("vendas_tech_amostra.xlsx")

st.title("📊 Dashboard de Vendas Tech")

# DICA DE OURO: Isso mostra o nome real das colunas no site para você não errar
st.write("Colunas detectadas:", df.columns.tolist())

# Criar o gráfico de barras
# IMPORTANTE: No lugar de 'COLUNA_X' e 'COLUNA_Y', coloque os nomes 
# que apareceram na lista acima (ex: 'Produto' e 'Valor_Venda')
try:
    fig = px.bar(
        df, 
        x="Produto", # Pega a primeira coluna (geralmente nomes)
        y="Preco_Unitario", # Pega a segunda coluna (geralmente valores)
        title="Vendas por Produto"
    )
    st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.error(f"Erro ao criar gráfico: {e}")