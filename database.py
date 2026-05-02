import mysql.connector

# Função para centralizar a conexão
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@escola2025",
        database="bd_biblioteca"
    )

def listar_livros():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM livro")
    livros = cursor.fetchall()
    conn.close()
    return livros

def cadastrar_livro(titulo, genero, autor):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO livro (titulo, genero, autor) VALUES (%s, %s, %s)"
    cursor.execute(sql, (titulo, genero, autor))
    conn.commit()
    conn.close()
    
# No ficheiro database.py

def excluir_livro(id):
    conn = conectar()
    cursor = conn.cursor()
    # Certifique-se de que o nome da coluna é 'id_livro' como no seu banco
    sql = "DELETE FROM livro WHERE id_livro = %s" 
    cursor.execute(sql, (id,))
    conn.commit()
    conn.close()