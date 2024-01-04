from .interno import *
from os import getenv
from dotenv import load_dotenv,find_dotenv
import smtplib
import email.message
import mysql.connector


# Carregando as variáveis de ambiente
load_dotenv(find_dotenv())

db_host = getenv("db_host")
db_user = getenv("db_user")
db_password = getenv("db_password")
db_name = getenv("db_name")

email_sac = getenv("email_sac")
senha_email_sac = getenv("senha_email_sac")


# Fazendo a conexão com o banco de dados
conexao = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = conexao.cursor()


# Enviar Código De Verificação Do Email:
def src_verificarEmail(nome_recebido,email_recebido,codigo_verificacao):
    string_vazia = src_verificarStringVazia(nome_recebido,email_recebido)
    email_valido = src_verificarValidadeEmail(email_recebido)

    if (string_vazia == False) and (email_valido == True):

        corpo_email = f"""
        <body style='font-family: Arial, Helvetica, sans-serif;'>
            <h4>Conta Gatitos</h4>
            <h1 style='color: rgb(68, 24, 224);'>Código de verificação</h1>
            <h3>Olá {nome_recebido}!</h3>
            <p>Seu código é: <span style='font-weight: bolder;color: rgb(68, 24, 224)'>{codigo_verificacao}</span></p>
        </body>       
        """

        msg = email.message.Message()
        msg['Subject'] = "Verifique Sua Conta"
        msg['From'] = email_sac
        msg['To'] = f'{email_recebido}'
        password = senha_email_sac

        msg.add_header('Content-Type','text/html')
        msg.set_payload(corpo_email)

        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()

        s.login(msg['From'],password)
        s.sendmail(msg['From'],[msg['To']], msg.as_string().encode('utf-8'))
        
        return True
    else:
        return False


# Criar Conta:
def src_criarConta(nome,email,senha):
    email_valido = src_verificarValidadeEmail(email)
    existe = src_verificarUsoEmail(email)

    if (email_valido == True) and (existe == False):
            try:
                comando = f"INSERT INTO jogadores (nome,email,senha) VALUES ('{nome}','{email}','{senha}')"
                cursor.execute(comando)
                conexao.commit()

                acao = 'criou_conta'
                res = src_registrarLog(email,acao)

                return True
            except:
                return False
    else:
        return False
 

# Logar Conta:
def src_logarConta(email,senha):
    email_valido = src_verificarValidadeEmail(email)
    string_vazia = src_verificarStringVazia(senha)

    if (email_valido == True) and string_vazia == False:

        comando = f'SELECT * FROM jogadores WHERE email="{email}" AND senha="{senha}"'
        cursor.execute(comando)
        varredura = cursor.fetchall()

        if (len(varredura) == 0):
            return False
        else:
            return True
        

# Alterar Conta:
def src_alterarConta(campo,novoDado,email):
    conexao.commit()

    email_valido = src_verificarValidadeEmail(email)
    campo_valido = src_verificarCampo(campo)
    string_vazia = src_verificarStringVazia(novoDado)
    email_cadastrado = src_verificarUsoEmail(email)

    if (email_valido == True) and (campo_valido == True) and (string_vazia == False) and (email_cadastrado == True):
    
        try:
            comando = f'UPDATE jogadores SET {campo}="{novoDado}" WHERE email= "{email}"'
            cursor.execute(comando)
            conexao.commit()

            acao = 'alterou_conta'
            src_registrarLog(email,acao)

            return True
        except:
            return False
    else:
        return False


# Excluir Conta:
def src_excluirConta(email):
    email_valido = src_verificarValidadeEmail(email)
    email_cadastrado = src_verificarUsoEmail(email)

    if (email_valido == True) and (email_cadastrado == True):
        try:
            id = src_RetornoIdUsuario(email)

            comando = f'DELETE FROM jogadores WHERE email= "{email}"'
            cursor.execute(comando)
            
            comando_limpar_log = f'DELETE FROM log WHERE id_jogador={id}'
            cursor.execute(comando_limpar_log)

            conexao.commit()

            print("*"*80)
            print(id)
            print("*"*80)

            return True
        except:
            return [False,'try']
    else:
        return [False]