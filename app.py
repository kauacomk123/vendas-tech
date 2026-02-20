import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página para o site ficar bonito
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("📊 Meu Portfólio de Análise de Dados")
st.markdown("---")

# Carregar os dados (usando o arquivo que você gerou)
df = pd.read_excel("vendas_tech_amostra.xlsx")

# Barra lateral para filtros
st.sidebar.header("Filtros do Dashboard")
# Aqui, substitua 'Produto' pelo nome exato de uma coluna de texto do seu Excel
coluna_filtro = df.columns[0] 
selecao = st.sidebar.multiselect("Selecione:", options=df[coluna_filtro].unique(), default=df[coluna_filtro].unique())

df_filtrado = df[df[coluna_filtro].isin(selecao)]

# Exibir os dados
st.subheader("Visualização dos Dados Filtrados")
st.dataframe(df_filtrado, use_container_width=True)

# Um gráfico simples para começar
st.subheader("Análise Visual")
# Substitua 'Valor' e 'Produto' pelos nomes reais das suas colunas
# Verifique no seu Excel qual o nome da coluna de texto e a de valores
# Exemplo: se for 'Produto' e 'Preço Total'
fig = px.bar(
    df_filtrado, 
    x="NOME_DA_SUA_COLUNA_AQUI",  # Ex: "Produto" ou "Item"
    y="NOME_DA_COLUNA_DE_NUMERO", # Ex: "Valor" ou "Total"
    title="Análise de Vendas por Produto"
)
st.plotly_chart(fig, use_container_width=True)