from aifc import Error

import mysql.connector

try:
    conexao = mysql.connector.connect(
        host='localhost',    database='netflix',    user='root',    password='')

    inserir_filmes = """INSERT INTO filmes(filme, plano, descricao, class)
    values
    ('Matrix', 'basic', 'djfhsdfhsdj', 12),
    ('Interestelar', 'medium', 'djfhsdfhsdj', 10);"""
    cursor = conexao.cursor()
    cursor.execute(inserir_filmes)
    conexao.commit()

    sql = 'SELECT * from filmes'
    cursor.execute(sql)
    linhas = cursor.fetchall()

    print('-'*20)
    for linha in linhas:
        print(linha[0], '\t')
        print(linha[1], '\t')
        print(linha[2], '\t')
        print(linha[3])
    print('-'*20)

except Error as e:
    print(f'Erro: {e}')

finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print('Conexão encerrada...')