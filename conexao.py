import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="",
        database="ocorrencia"
    )
    return conexao
