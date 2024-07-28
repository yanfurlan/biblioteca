import sqlite3
import os

# Função para deletar o banco de dados existente
def deletar_banco_de_dados():
    if os.path.exists('biblioteca.db'):
        os.remove('biblioteca.db')

# Funções de criação de tabelas
def criar_tabelas():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS autores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor_id INTEGER,
                        ano_publicacao INTEGER,
                        FOREIGN KEY (autor_id) REFERENCES autores(id))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS emprestimos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        livro_id INTEGER,
                        usuario_id INTEGER,
                        data_emprestimo DATE,
                        data_devolucao DATE,
                        FOREIGN KEY (livro_id) REFERENCES livros(id),
                        FOREIGN KEY (usuario_id) REFERENCES usuarios(id))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        livro_id INTEGER,
                        usuario_id INTEGER,
                        data_reserva DATE,
                        FOREIGN KEY (livro_id) REFERENCES livros(id),
                        FOREIGN KEY (usuario_id) REFERENCES usuarios(id))''')
    
    conn.commit()
    conn.close()

# Funções de inserção de dados
def inserir_autor(nome):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO autores (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()

def inserir_livro(titulo, autor_id, ano_publicacao):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (titulo, autor_id, ano_publicacao) VALUES (?, ?, ?)",
                   (titulo, autor_id, ano_publicacao))
    conn.commit()
    conn.close()

def inserir_usuario(nome, email):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()

def inserir_emprestimo(livro_id, usuario_id, data_emprestimo, data_devolucao):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)",
                   (livro_id, usuario_id, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

def inserir_reserva(livro_id, usuario_id, data_reserva):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservas (livro_id, usuario_id, data_reserva) VALUES (?, ?, ?)",
                   (livro_id, usuario_id, data_reserva))
    conn.commit()
    conn.close()

# Funções de consulta de dados
def consultar_livros():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("SELECT livros.titulo, autores.nome, livros.ano_publicacao FROM livros JOIN autores ON livros.autor_id = autores.id")
    livros = cursor.fetchall()
    conn.close()
    return livros

def livros_emprestados_por_usuario():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT usuarios.nome, livros.titulo, emprestimos.data_emprestimo, emprestimos.data_devolucao
                      FROM emprestimos
                      JOIN livros ON emprestimos.livro_id = livros.id
                      JOIN usuarios ON emprestimos.usuario_id = usuarios.id
                      ORDER BY usuarios.nome''')
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def usuarios_com_mais_emprestimos():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT usuarios.nome, COUNT(emprestimos.id) AS total_emprestimos
                      FROM usuarios
                      JOIN emprestimos ON usuarios.id = emprestimos.usuario_id
                      GROUP BY usuarios.nome
                      HAVING total_emprestimos > 1
                      ORDER BY total_emprestimos DESC''')
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def relatorio_livros_reservados():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT livros.titulo, usuarios.nome, reservas.data_reserva
                      FROM reservas
                      JOIN livros ON reservas.livro_id = livros.id
                      JOIN usuarios ON reservas.usuario_id = usuarios.id
                      ORDER BY reservas.data_reserva DESC''')
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# Deletar o banco de dados existente (se houver)
deletar_banco_de_dados()

# Criação das tabelas
criar_tabelas()

# Inserção de dados para teste
inserir_autor("J.K. Rowling")
inserir_autor("George R.R. Martin")

inserir_livro("Harry Potter e a Pedra Filosofal", 1, 1997)
inserir_livro("Harry Potter e a Câmara Secreta", 1, 1998)
inserir_livro("A Game of Thrones", 2, 1996)

inserir_usuario("João Silva", "joao@example.com")
inserir_usuario("Maria Oliveira", "maria@example.com")

inserir_emprestimo(1, 1, '2023-07-01', '2023-07-15')
inserir_emprestimo(3, 2, '2023-07-10', '2023-07-25')

inserir_reserva(2, 1, '2023-07-20')

# Consultas e relatórios
print("Livros na biblioteca:")
print(consultar_livros())

print("\nLivros emprestados por usuário:")
print(livros_emprestados_por_usuario())

print("\nUsuários com mais de um empréstimo:")
print(usuarios_com_mais_emprestimos())

print("\nRelatório de livros reservados:")
print(relatorio_livros_reservados())
