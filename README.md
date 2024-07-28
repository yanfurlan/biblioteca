## Sistema de Gerenciamento de Biblioteca

Este é um sistema simples de gerenciamento de biblioteca desenvolvido em Python com SQLite. Ele permite gerenciar autores, livros, usuários, empréstimos e reservas de uma biblioteca.

## Funcionalidades

- **Autores**: Inserção e consulta de autores.
- **Livros**: Inserção e consulta de livros.
- **Usuários**: Inserção e consulta de usuários.
- **Empréstimos**: Inserção e consulta de empréstimos de livros.
- **Reservas**: Inserção e consulta de reservas de livros.

## Como Executar

1. Certifique-se de ter o Python instalado em seu ambiente.
2. Certifique-se de ter o SQLite3 instalado e disponível em seu ambiente.
3. Baixe o código do projeto e salve em um arquivo, por exemplo, `biblioteca.py`.
4. Execute o arquivo Python em seu terminal ou ambiente de desenvolvimento:

```bash
python biblioteca.py
```

## Estrutura do Código

- **Criação de Tabelas**: As funções para criar as tabelas `autores`, `livros`, `usuarios`, `emprestimos` e `reservas`.
- **Inserção de Dados**: As funções para inserir dados nas tabelas.
- **Consultas**: As funções para consultar dados das tabelas e gerar relatórios.

## Exemplo de Uso

O código inclui exemplos de inserção de dados para teste e geração de relatórios:

```python
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

print("
Livros emprestados por usuário:")
print(livros_emprestados_por_usuario())

print("
Usuários com mais de um empréstimo:")
print(usuarios_com_mais_emprestimos())

print("
Relatório de livros reservados:")
print(relatorio_livros_reservados())
```

## Autor

Desenvolvido por Yan.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
