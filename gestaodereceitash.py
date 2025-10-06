import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
st.set_page_config(page_title="Dashboard Hoteleiro", layout="wide")

# Título do Dashboard
st.title("📊 Dashboard de Inteligência de Mercado Hoteleiro")

# ---------- Seção Interativa para Inserir Dados dos Hotéis ----------
st.subheader("📝 Inserir/Editar Dados dos Concorrentes")

# Lista inicial de hotéis
if "df_hotéis" not in st.session_state:
    st.session_state.df_hotéis = pd.DataFrame({
        "Hotel": ["Hotel A", "Hotel B", "Hotel C", "Hotel D", "Hotel E"],
        "Preço Médio (R$)": [250, 220, 270, 300, 200],
        "Ocupação (%)": [80, 75, 90, 60, 85]
    })

# Editor de tabela interativo
st.session_state.df_hotéis = st.data_editor(
    st.session_state.df_hotéis,
    num_rows="dynamic",
    use_container_width=True
)

# ---------- Layout dos Gráficos ----------
col1, col2 = st.columns(2)

# Gráfico de Comparação de Preços
with col1:
    st.subheader("💰 Comparação de Preços dos Concorrentes")
    fig = px.bar(
        st.session_state.df_hotéis, 
        x="Hotel", 
        y="Preço Médio (R$)", 
        color="Preço Médio (R$)",
        labels={"Preço Médio (R$)": "Preço Médio (R$)"},
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de Ocupação
with col2:
    st.subheader("🏨 Taxa de Ocupação dos Concorrentes")
    fig2 = px.line(
        st.session_state.df_hotéis, 
        x="Hotel", 
        y="Ocupação (%)", 
        markers=True, 
        line_shape="linear"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---------- Eventos Locais ----------
st.subheader("📅 Eventos Locais e Impacto na Demanda")

# Dados dos eventos (podem ser editáveis também)
if "df_eventos" not in st.session_state:
    st.session_state.df_eventos = pd.DataFrame({
        "Evento": ["Festival de Música", "Congresso de Turismo", "Feriado Prolongado"],
        "Data": ["10/04", "15/04", "21/04"],
        "Impacto Estimado (%)": [15, 20, 30]
    })

st.session_state.df_eventos = st.data_editor(
    st.session_state.df_eventos,
    num_rows="dynamic",
    use_container_width=True
)

# ---------- Dica Estratégica ----------
st.markdown("**📌 Dica:** Ajuste suas tarifas com base na concorrência e eventos próximos para maximizar a receita!")
