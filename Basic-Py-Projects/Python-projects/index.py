import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns    
import streamlit as st
import altair as alt
import os

csv_path = os.path.join(os.path.dirname(__file__), 'sales_data.csv')
df = pd.read_csv(csv_path)


df['Date_Sold'] = pd.to_datetime(df['Date_Sold'])  
df['Month_Year'] = df['Date_Sold'].dt.month

print(df.isnull().sum())
print(f"\nDuplicatas: {df.duplicated().sum()}")

print("\nTipos:")
print(df.dtypes)

print("\nEstatisticas:")
print(df.describe())


print(df.head()) 
df['Date_Sold'] = pd.to_datetime(df['Date_Sold'])  # Converter para datetime
df['Month_Year'] = df['Date_Sold'].dt.to_period('M') # Adiciona coluna de Mês-Ano

# Funções para visualizações (Altair)
def criar_grafico_vendas_por_categoria(df, filtro_categoria=None, filtro_mes=None):
    """
    Cria um gráfico de barras interativo mostrando as vendas totais por categoria.
    Permite filtrar por categoria e mês.
    """
    # Certifica que Total_Sales é numérico
    df['Total_Sales'] = pd.to_numeric(df['Total_Sales'], errors='coerce')

    if filtro_categoria:
        df_filtrado = df[df['Category'] == filtro_categoria]
    else:
        df_filtrado = df
    
    if filtro_mes:
        df_filtrado = df_filtrado[df_filtrado['Date_Sold'].dt.month_name() == filtro_mes]

    chart = alt.Chart(df_filtrado).mark_bar().encode(
        x=alt.X('Category', title='Categoria'),
        y=alt.Y('Total_Sales', title='Vendas Totais'),
        color='Category',
        tooltip=['Category', 'Total_Sales']
    ).properties(
        title='Vendas Totais por Categoria'
    ).interactive()
    return chart

def criar_grafico_vendas_ao_longo_do_tempo(df, filtro_categoria=None, filtro_mes=None):
    """
    Cria um gráfico de linhas interativo mostrando a evolução das vendas ao longo do tempo.
    Permite filtrar por categoria e mês.
    """
    # Certifica que Total_Sales é numérico
    df['Total_Sales'] = pd.to_numeric(df['Total_Sales'], errors='coerce')
    if filtro_categoria:
        df_filtrado = df[df['Category'] == filtro_categoria]
    else:
        df_filtrado = df
        
    if filtro_mes:
        df_filtrado = df_filtrado[df_filtrado['Date_Sold'].dt.month_name() == filtro_mes]
        
    chart = alt.Chart(df_filtrado).mark_line().encode(
        x=alt.X('Date_Sold', title='Data'),
        y=alt.Y('Total_Sales', title='Vendas Totais'),
        tooltip=['Date_Sold', 'Total_Sales']
    ).properties(
        title='Evolução das Vendas ao Longo do Tempo'
    ).interactive()
    return chart

def criar_grafico_preco_vs_quantidade(df, filtro_categoria=None, filtro_mes=None):
    """
    Cria um gráfico de dispersão interativo mostrando a relação entre preço e quantidade vendida.
    Permite filtrar por categoria e mês.
    """
    # Certifica que Price e Quantity_Sold são numéricos
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Quantity_Sold'] = pd.to_numeric(df['Quantity_Sold'], errors='coerce')

    if filtro_categoria:
        df_filtrado = df[df['Category'] == filtro_categoria]
    else:
        df_filtrado = df
        
    if filtro_mes:
        df_filtrado = df_filtrado[df_filtrado['Date_Sold'].dt.month_name() == filtro_mes]

    chart = alt.Chart(df_filtrado).mark_circle().encode(
        x=alt.X('Price', title='Preço'),
        y=alt.Y('Quantity_Sold', title='Quantidade Vendida'),
        color='Category',
        tooltip=['Product_Name', 'Price', 'Quantity_Sold', 'Category']
    ).properties(
        title='Preço X Quantidade Vendida'
    ).interactive()
    return chart

def criar_grafico_quantidade_vendida_por_categoria(df, filtro_categoria=None, filtro_mes=None):
    """
    Cria um gráfico de barras mostrando a quantidade vendida por categoria.
    Permite filtrar por categoria e mês.
    """
    # Certifica que Quantity_Sold é numérico
    df['Quantity_Sold'] = pd.to_numeric(df['Quantity_Sold'], errors='coerce')
    if filtro_categoria:
        df_filtrado = df[df['Category'] == filtro_categoria]
    else:
        df_filtrado = df
        
    if filtro_mes:
        df_filtrado = df_filtrado[df_filtrado['Date_Sold'].dt.month_name() == filtro_mes]
        
    chart = alt.Chart(df_filtrado).mark_bar().encode(
        x=alt.X('Category', title='Categoria'),
        y=alt.Y('Quantity_Sold', title='Quantidade Vendida'),
        color='Category',
        tooltip=['Category', 'Quantity_Sold']
    ).properties(
        title='Quantidade Vendida por Categoria'
    ).interactive()
    return chart
def criar_grafico_vendas_por_categoria_mes(df, filtro_categoria=None, filtro_mes=None):
    """
    Cria um gráfico de barras mostrando as vendas por categoria e mês.
    Permite filtrar por categoria.
    """
    # Certifica que Total_Sales é numérico
    df['Total_Sales'] = pd.to_numeric(df['Total_Sales'], errors='coerce')
    if filtro_categoria:
        df_filtrado = df[df['Category'] == filtro_categoria]
    else:
        df_filtrado = df
        
    if filtro_mes:
        df_filtrado = df_filtrado[df_filtrado['Date_Sold'].dt.month_name() == filtro_mes]
        
    # Agrupa os dados por categoria e mês
    df_grouped = df_filtrado.groupby(['Category', df_filtrado['Date_Sold'].dt.month_name()])['Total_Sales'].sum().reset_index()

    # Define a ordem dos meses para exibição correta
    meses_ordem = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    chart = alt.Chart(df_grouped).mark_bar().encode(
        x=alt.X('Date_Sold', title='Mês', sort=meses_ordem),  # Mostra o nome do mês e ordena
        y=alt.Y('Total_Sales', title='Vendas Totais'),
        color=alt.Color('Category', title='Categoria'),  # Usa cores diferentes para cada categoria
        column=alt.Column('Category', header=alt.Header(titleOrient="bottom", labelOrient="bottom"), title = "Categoria"), 
        tooltip=['Date_Sold', 'Category', 'Total_Sales']
    ).properties(
        title='Vendas Totais por Categoria e Mês'
    ).interactive()
    return chart

# Interface Streamlit
st.title("Análise de Vendas de Produtos")
st.write("Atividade Geraldo Streamlit - Data Science 26/04/2025")
st.write("Aluno: Luís Felipe do Carmo Costa Tavares")

# Adiciona um filtro de categoria
categorias = df['Category'].unique()
categoria_selecionada = st.sidebar.selectbox('Selecione a Categoria', ['Todas'] + list(categorias))

# Adiciona um filtro de mês
meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
mes_selecionado = st.sidebar.selectbox('Selecione o Mês', ['Todos'] + meses)


# 1. Visão geral dos dados
st.header("Visão Geral dos Dados")
st.write("A tabela abaixo mostra as primeiras linhas do dataset de vendas. Podemos observar informações como ID do produto, nome, categoria, preço, quantidade vendida, data da venda e o total de vendas.")
st.dataframe(df.head()) 

# 2. Análise das categorias de produtos
st.header("Análise das Categorias de Produtos")
st.altair_chart(criar_grafico_vendas_por_categoria(df, categoria_selecionada if categoria_selecionada != 'Todas' else None, mes_selecionado if mes_selecionado != 'Todos' else None), use_container_width=True)

# 3. Vendas ao Longo do Tempo
st.header("Vendas ao Longo do Tempo")
st.altair_chart(criar_grafico_vendas_ao_longo_do_tempo(df, categoria_selecionada if categoria_selecionada != 'Todas' else None, mes_selecionado if mes_selecionado != 'Todos' else None), use_container_width=True)

# 4. Relação entre Preço X Quantidade Vendida
st.header("Relação entre Preço X Quantidade Vendida")
st.altair_chart(criar_grafico_preco_vs_quantidade(df, categoria_selecionada if categoria_selecionada != 'Todas' else None, mes_selecionado if mes_selecionado != 'Todos' else None), use_container_width=True)

# 5. Quantidade Vendida por Categoria
st.header("Quantidade Vendida por Categoria")
st.altair_chart(criar_grafico_quantidade_vendida_por_categoria(df, categoria_selecionada if categoria_selecionada != 'Todas' else None, mes_selecionado if mes_selecionado != 'Todos' else None), use_container_width=True)

# 6. Vendas por Categoria e Mês
st.header("Vendas por Categoria e Mês")
st.altair_chart(criar_grafico_vendas_por_categoria_mes(df, categoria_selecionada if categoria_selecionada != 'Todas' else None, mes_selecionado if mes_selecionado != 'Todos' else None), use_container_width=True)


# 7. Insights e Conclusões
st.header("Insights e Conclusões")
st.write("""
Com base na análise dos dados, podemos observar alguns insights importantes:

* **Desempenho das Categorias:** A categoria 'Clothing' se destaca com as maiores vendas totais, indicando uma forte demanda por esses produtos.
* **Tendência de Vendas:** As vendas apresentam uma tendência de crescimento ao longo do tempo, o que é positivo demonstrando um crescimento sustentado no mercado.
* **Preço e Quantidade:** Não há uma relação clara e direta entre preço e quantidade vendida. Alguns produtos de preço mais alto ainda vendem bem, o que pode sugerir que outros fatores, como a popularidade do produto ou estratégias de marketing, também influenciam as vendas.
""")

# Adicionando uma seção final com recomendações
st.header("Recomendações")
st.write("""
Com base nos insights acima, aqui estão algumas recomendações:

* **Focar em Roupas:** Dada a alta demanda, a empresa pode considerar expandir a oferta de produtos eletrônicos ou investir em marketing direcionado para essa categoria.
* **Analisar Estratégias de Preços:** A relação não linear entre preço e quantidade vendida sugere que uma análise mais aprofundada das estratégias de preços pode ser benéfica.
* **Analisar Estratégias do Mês:** A maior utilização de campanhas de marketing no mês de março pode ser de grande aumento nas vendas dada a alta demanda no período.
* **Monitorar Tendências:** Continuar monitorando a tendência de vendas ao longo do tempo é crucial para identificar oportunidades de crescimento e se adaptar a mudanças no mercado.
""")
