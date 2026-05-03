import streamlit as st
import database as db
import pandas as pd # Opcional: para deixar a tabela linda

st.set_page_config(page_title="BioBiblio v1.0", layout="wide", page_icon="📚")

# CSS para melhorar a estética (Opcional, mas os alunos adoram)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("📚 Sistema de Gestão de Biblioteca")
st.subheader("Painel Administrativo - 1º Ano")

# --- CRIAÇÃO DAS ABAS ---
tab_consulta, tab_cadastro = st.tabs(["🔍 Consultar Acervo", "➕ Cadastrar Livro"])

# --- ABA DE CONSULTA ---
with tab_consulta:
    st.write("### Livros Cadastrados")
    lista_livros = db.listar_livros()
    
    if lista_livros:
        # Transformamos em DataFrame para o Streamlit mostrar uma tabela interativa
        df = pd.DataFrame(lista_livros)
        df.columns = ['ID', 'Título', 'Gênero', 'Autor'] # Renomeia colunas para o usuário
        
        # Mostra a tabela rica
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.divider()
        
        # Área de Exclusão mais segura
        st.write("#### ⚠️ Zona de Exclusão")
        col_id, col_btn = st.columns([1, 1])
        id_para_excluir = col_id.number_input("Digite o ID do livro para remover", min_value=1, step=1)
        
        if col_btn.button("Confirmar Exclusão", type="primary"):
            db.excluir_livro(id_para_excluir)
            st.toast(f"Livro #{id_para_excluir} removido!", icon="🗑️")
            st.rerun()
    else:
        st.info("O acervo está vazio.")

# --- ABA DE CADASTRO ---
with tab_cadastro:
    with st.form("form_cadastro", clear_on_submit=True):
        st.write("### Novo Registro")
        col1, col2 = st.columns(2)
        
        with col1:
            titulo = st.text_input("Título do Livro", placeholder="Ex: O Alquimista")
            autor = st.text_input("Autor", placeholder="Ex: Paulo Coelho")
        
        with col2:
            generos = ["Ficção", "Terror", "Didático", "Fantasia", "Romance", "Tecnologia"]
            genero = st.selectbox("Gênero", generos)
            st.write("") # Espaçamento
            btn_enviar = st.form_submit_button("Salvar Livro")

        if btn_enviar:
            if titulo and autor:
                db.cadastrar_livro(titulo, autor, genero)
                st.success(f"'{titulo}' adicionado com sucesso!", icon="✅")
            else:
                st.error("Por favor, preencha o Título e o Autor.")