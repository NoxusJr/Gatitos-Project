from datetime import datetime 
from os import getenv
from dotenv import load_dotenv,find_dotenv
import mysql.connector


# Carregando as variáveis de ambiente
load_dotenv(find_dotenv())

db_host = getenv("db_host")
db_user = getenv("db_user")
db_password = getenv("db_password")
db_name = getenv("db_name")


# Fazendo a conexão com o banco de dados
conexao = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = conexao.cursor()


# Verificar Disponibilidade Do Email:
def src_verificarUsoEmail(email):
    conexao.commit()

    comando = f'SELECT * FROM jogadores WHERE email = "{email}"'
    cursor.execute(comando)
    varredura = cursor.fetchall()

    if (len(varredura) == 0):
       return False
    else:
       return True
    
# Retorna A HORA ATUAL
def src_RetornoHora():
    hora_atual = datetime.now()
    hora_atual = hora_atual.time()
    hora_atual = str(hora_atual)

    return hora_atual[0:8]


# Retorna A DATA ATUAL
def src_RetornoData():
    data_atual = datetime.now()
    data_atual = data_atual.date()
    data_atual = data_atual.strftime("%Y-%m-%d")

    return data_atual


# Retorna o ID DO USUÁRIO
def src_RetornoIdUsuario(email):
    conexao.commit()

    comando = f"SELECT id_jogador FROM jogadores WHERE email = '{email}'"
    cursor.execute(comando)
    id_usuario = cursor.fetchall()
    id_usuario = id_usuario[0][0]

    return id_usuario


# Verifica se alguma STRING É VAZIA
def src_verificarStringVazia(*strings):
  for string in strings:
     if len(string) <=0:
        return True
  else:
     return False
  

# Verifica se o PONTO É NEGATIVO
def src_verificarPontoNegativo(ponto):
  if ponto < 0:
    return True
  else:
    return False
  

# Verifica a VALIDADE DO EMAIL
def src_verificarValidadeEmail(email):
  if '@' in email and '.' in email:
    return True
  else:
    return False
  

# Verifica a VALIDADE DA AÇÃO
def src_verificarAcao(acao):
  lista = ['criou_conta', 'logou_conta', 'deslogou_conta', 'alterou_conta']
  if acao in lista:
    return True
  else:
    return False
    

# Verifica a VALIDADE DO CAMPO
def src_verificarCampo(campo):
   lista = ['nome','senha']
   if campo in lista:
      return True
   else:
      return False

    
# Registrar LOG
def src_registrarLog(email,acao):
    conexao.commit()

    string_vazia = src_verificarStringVazia(acao)
    email_valido = src_verificarValidadeEmail(email)
    acao_valida = src_verificarAcao(acao)

    if (string_vazia == False) and (email_valido == True) and (acao_valida == True):
        email_cadastrado = src_verificarUsoEmail(email)

        if email_cadastrado == True:

            data_log = src_RetornoData()
            hora_log = src_RetornoHora()
            id_user = src_RetornoIdUsuario(email)

            comando = f"INSERT INTO log (id_jogador,acao,data_log,hora_log) VALUES ({id_user},'{acao}','{data_log}','{hora_log}')"
            cursor.execute(comando)
            conexao.commit()

            return True
        else:
            return False
    else:
        return False