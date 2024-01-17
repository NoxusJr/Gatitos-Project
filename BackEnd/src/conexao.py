from os import getenv
from dotenv import load_dotenv,find_dotenv
import mysql.connector

# Carregando as variáveis de ambiente
load_dotenv(find_dotenv())

DB_HOST = getenv("db_host")
DB_USER = getenv("db_user")
DB_PASSOWRD = getenv("db_password")
DB_NAME = getenv("db_name")

email_sac = getenv("email_sac")
senha_email_sac = getenv("senha_email_sac")


# Fazendo a conexão com o banco de dados
conexao = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSOWRD,
    database=DB_NAME
)

cursor = conexao.cursor()