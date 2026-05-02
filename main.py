import streamlit as st
import database as db

# Configuração da página
st.set_page_config(page_title="Sistema de Biblioteca", layout="centered")

st.title("📚 Piloto: Biblioteca Escolar")
st.markdown("---")

# --- SEÇÃO 1: CADASTRO ---
st.subheader("Cadastrar Novo Livro")
col1, col2 = st.columns(2)

with col1:
    input_titulo = st.text_input("Título do Livro")
    # Agora como uma lista de seleção (selectbox)
    lista_generos = ["Ficção", "Terror", "Didático", "Fantasia", "Romance", "Outros"]
    input_genero = st.selectbox("Gênero", lista_generos)

with col2:
    input_autor = st.text_input("Autor")
    botao_cadastrar = st.button("Adicionar ao Acervo")

if botao_cadastrar:
    if input_titulo and input_autor:
        db.cadastrar_livro(input_titulo, input_autor, input_genero)
        st.success(f"Livro '{input_titulo}' cadastrado!")
        st.rerun() # Atualiza a tela para mostrar o novo livro
    else:
        st.warning("Título e Autor são obrigatórios!")

st.markdown("---")

# --- SEÇÃO 2: LISTAGEM E EXCLUSÃO ---
st.subheader("Livros Disponíveis")
lista_livros = db.listar_livros()

if lista_livros:
    # Adicionamos uma coluna pequena (0.5) para o ID no início
    for livro in lista_livros:
        c_id, c1, c2, c3, c4 = st.columns([0.5, 3, 2, 2, 1])
        
        c_id.write(f"#{livro['id_livro']}") # Exibe o ID com um # na frente
        c1.write(livro['titulo'])
        c2.write(livro['autor'])
        c3.write(livro['genero'])
        
        if c4.button("🗑️", key=f"del_{livro['id_livro']}"):
            db.excluir_livro(livro['id_livro'])
            st.rerun()
else:
    st.info("Nenhum livro cadastrado no momento.")