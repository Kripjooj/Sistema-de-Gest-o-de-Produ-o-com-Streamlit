import streamlit as st
from classes.producao import Producao
from utils.salvar_json import salvar_producao
from utils.relatorio import RelatorioExcel
from datetime import datetime
import os

# --- Funções de Utilitário ---
def clear_json_data():
    """Apaga o arquivo de dados JSON."""
    file_path = "database/producao.json"
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False

# --- Configuração da Página e Título ---
st.set_page_config(page_title="Sistema de dados", layout="wide")
st.title("📋 Registro de Produção")

# Inicializa o estado de sessão para a confirmação
if 'confirm_clear' not in st.session_state:
    st.session_state.confirm_clear = False

st.markdown("### Preencha os dados abaixo para registrar uma nova produção:")

# --- Formulário de Registro de Produção ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    data = st.date_input("📅 Data da produção", value=datetime.today())
with col2:
    turno = st.selectbox("🌙 Turno", ["1", "2", "3"])
with col3:
    horario_inicio = st.time_input("⏰ Hora de Início")
with col4:
    horario_termino = st.time_input("⏰ Hora de Término")

setor = st.selectbox("🏭 Setor", ["Dobra", "Serra", "Solda", "Retrabalho", "Etiquetagem"])

col5, col6 = st.columns(2)
with col5:
    cliente = st.text_input("👤 Cliente")
with col6:
    modelo = st.text_input("📦 Modelo")

of = st.text_input("📑 Ordem de Fabricação (OF)")

col7, col8 = st.columns(2)
with col7:
    qtd_aprovada = st.number_input("✅ Quantidade Aprovada", min_value=0, step=1)
with col8:
    qtd_retrabalho = st.number_input("♻️ Quantidade Retrabalhada", min_value=0, step=1)

motivo = st.text_area("⚠️ Motivo das Falhas", placeholder="Descreva o problema...")
responsavel = st.text_input("🧑‍🔧 Responsável")

# Botão para salvar a produção
if st.button("💾 Salvar Produção", use_container_width=True):
    nova_producao = Producao(
        data=str(data),
        HORA_INICIO=str(horario_inicio),
        HORA_TERMINO=str(horario_termino),
        setor=setor,
        cliente=cliente,
        modelo=modelo,
        of=of,
        qtd_aprovada=qtd_aprovada,
        qtd_retrabalho=qtd_retrabalho,
        motivo_falha=motivo,
        responsavel=responsavel,
        turno=turno
    )
    salvar_producao(nova_producao)
    st.success("✅ Produção salva com sucesso!")



st.markdown("### Relatórios")

# Botão para gerar o relatório em Excel
if st.button("📊 Gerar Relatório Excel", use_container_width=True):
    with st.spinner('Gerando relatório...'):
        relatorio = RelatorioExcel()
        relatorio.criar_base()
        relatorio.preencher_planilha()
        relatorio.formatar_planilha()
        relatorio.salvar_relatorio()
    st.success("🎉 Relatório Excel gerado com sucesso!")
    st.info("O arquivo 'base_producao.xlsx' foi salvo na pasta 'relatorios'.")



### Limpeza de Dados

# Botão principal para iniciar a limpeza
if st.button("🔴 Limpar todos os dados", use_container_width=True):
    st.session_state.confirm_clear = True

# Lógica da confirmação
if st.session_state.confirm_clear:
    st.warning("⚠️ **ATENÇÃO:** Esta ação é irreversível!")
    st.write("Tem certeza que deseja apagar **TODO** o histórico de produção?")
    
    col_yes, col_no = st.columns(2)
    with col_yes:
        if st.button("Sim, apagar tudo!", use_container_width=True):
            if clear_json_data():
                st.success("✅ Dados antigos apagados com sucesso!")
            else:
                st.error("❌ O arquivo de dados não foi encontrado. Nenhum dado foi apagado.")
            st.session_state.confirm_clear = False
            st.rerun()  # Recarrega a página para atualizar a interface
    with col_no:
        if st.button("Não, cancelar", use_container_width=True):
            st.session_state.confirm_clear = False
            st.info("Operação cancelada.")
            st.rerun()  # Recarrega a página para atualizar a interface