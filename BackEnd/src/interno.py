from datetime import datetime 
from .conexao import *


def verificar_uso_email(email):
    conexao.commit()

    comando = f'SELECT * FROM jogadores WHERE email = "{email}"'
    cursor.execute(comando)
    varredura = cursor.fetchall()

    if (len(varredura) == 0):
       return False
    else:
       return True
    

def retornar_hora():
    hora_atual = datetime.now()
    hora_atual = hora_atual.time()
    hora_atual = str(hora_atual)

    return hora_atual[0:8]


def retornar_data():
    data_atual = datetime.now()
    data_atual = data_atual.date()
    data_atual = data_atual.strftime("%Y-%m-%d")

    return data_atual


def retornar_id_usuario(email):
    conexao.commit()

    comando = f"SELECT id_jogador FROM jogadores WHERE email = '{email}'"
    cursor.execute(comando)
    id_usuario = cursor.fetchall()
    id_usuario = id_usuario[0][0]

    return id_usuario


# Verifica se alguma STRING É VAZIA



def verificar_ponto_negativo(ponto):
  if ponto < 0:
    return True
  else:
    return False
  

def verificar_validade_email(email):
  if '@' in email and '.' in email:
    return True
  else:
    return False
  

def verificar_validade_acao(acao):
  lista = ['criou_conta', 'logou_conta', 'deslogou_conta', 'alterou_conta']
  if acao in lista:
    return True
  else:
    return False
    

def verificar_validade_campo(campo):
   lista = ['nome','senha']
   if campo in lista:
      return True
   else:
      return False

    
def registrar_log(email,acao):
    conexao.commit()

    email_valido = verificar_validade_email(email)
    acao_valida = verificar_validade_acao(acao)

    if (email_valido == True) and (acao_valida == True):
        email_cadastrado = verificar_uso_email(email)

        if email_cadastrado == True:

            data_log = retornar_data()
            hora_log = retornar_hora()
            id_user = retornar_id_usuario(email)

            comando = f"INSERT INTO log (id_jogador,acao,data_log,hora_log) VALUES ({id_user},'{acao}','{data_log}','{hora_log}')"
            cursor.execute(comando)
            conexao.commit()

            return True
        else:
            return False
    else:
        return False