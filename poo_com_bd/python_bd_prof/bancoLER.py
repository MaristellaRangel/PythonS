import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='netflix',
    user='root',
    password=''
)
# Fazer Conexão
if conexao.is_connected():
    db_info = conexao.get_server_info()
    print(f'Você se conectou a {db_info}')

# Imprimir nome do banco de dados
cursor =conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()
print(f'Banco = {linha[0]}')

sql = 'SELECT * from usuarios'
cursor.execute(sql)
linhas = cursor.fetchall()
for linha in linhas:
    print(linha[0], end='\t')
    print(''*(10-len(linha[1])), linha[1], end='\t')
    print(linha[2], end='\t')
    print(linha[3], end='\t')
    print(linha[4])
