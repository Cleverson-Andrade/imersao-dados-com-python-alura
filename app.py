import streamlit as st
import pandas as pd
import plotly.express as px

# --- Página: Configurações Iniciais | Page: Initial Settings ---
# Configura o layout da página para ocupar a largura total
# Sets the page layout to occupy the full width
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados | Data Salary Dashboard",
    page_icon="📊",
    layout="wide",
)

# --- Carga de Dados | Data Loading ---
# Carrega o CSV processado diretamente do repositório
# Loads the processed CSV directly from the repository
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

# --- Barra Lateral: Filtros | Sidebar: Filters ---
st.sidebar.header("🔍 Filtros | Filters")

# Filtro de Ano | Year Filter
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano | Year", anos_disponiveis, default=anos_disponiveis)

# Filtro de Senioridade | Seniority Filter
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade | Seniority", senioridades_disponiveis, default=senioridades_disponiveis)

# Filtro por Tipo de Contrato | Employment Type Filter
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato | Employment Type", contratos_disponiveis, default=contratos_disponiveis)

# Filtro por Tamanho da Empresa | Company Size Filter
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa | Company Size", tamanhos_disponiveis, default=tamanhos_disponiveis)

# --- Lógica de Filtragem | Filtering Logic ---
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# --- Conteúdo Principal | Main Content ---
st.title("🎲 Dashboard: Análise de Salários (Data Science)")
st.markdown("""
Explore os dados salariais globais nos últimos anos. Utilize os filtros à esquerda para refinar sua análise.
Explore global salary data from recent years. Use the filters on the left to refine your analysis.
""")

# --- Métricas Principais (KPIs) | Key Performance Indicators ---
st.subheader("Métricas Gerais | General Metrics (USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, "N/A"

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário Médio | Avg Salary", f"${salario_medio:,.0f}")
col2.metric("Salário Máximo | Max Salary", f"${salario_maximo:,.0f}")
col3.metric("Total de Registros | Total Records", f"{total_registros:,}")
col4.metric("Cargo Frequente | Most Common Role", cargo_mais_frequente)

st.markdown("---")

# --- Análises Visuais | Visual Analytics (Plotly) ---
st.subheader("Visualizações Interativas | Interactive Visualizations")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos, x='usd', y='cargo', orientation='h',
            title="Top 10 Cargos por Salário Médio | Top 10 Roles by Avg Salary",
            labels={'usd': 'Média Salarial (USD)', 'cargo': ''}
        )
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Sem dados para exibir | No data to display.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado, x='usd', nbins=30,
            title="Distribuição Salarial | Salary Distribution",
            labels={'usd': 'Faixa Salarial (USD)', 'count': 'Frequência'}
        )
        st.plotly_chart(grafico_hist, use_container_width=True)

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem, names='tipo_trabalho', values='quantidade',
            title='Modelo de Trabalho | Work Model Proportion',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        st.plotly_chart(grafico_remoto, use_container_width=True)

with col_graf4:
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(
            media_ds_pais, locations='residencia_iso3', color='usd',
            color_continuous_scale='rdylgn',
            title='Média Salarial por País (DS) | Avg Salary by Country (DS)',
            labels={'usd': 'Salário (USD)', 'residencia_iso3': 'País'}
        )
        st.plotly_chart(grafico_paises, use_container_width=True)

# --- Tabela de Dados | Data Table ---
st.subheader("Dados Detalhados | Detailed Data")
st.dataframe(df_filtrado, use_container_width=True)
