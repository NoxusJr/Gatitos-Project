from .interno import *
from .conexao import *
import smtplib
import email.message


# Enviar Código De Verificação Do Email:
def verificar_email(nome_recebido,email_recebido,codigo_verificacao):
    string_vazia = verificar_string_vazia(nome_recebido,email_recebido)
    email_valido = verificar_validade_email(email_recebido)

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
def criar_conta(nome,email,senha):
    email_valido = verificar_validade_email(email)
    existe = verificar_uso_email(email)

    if (email_valido == True) and (existe == False):
            try:
                comando = f"INSERT INTO jogadores (nome,email,senha) VALUES ('{nome}','{email}','{senha}')"
                cursor.execute(comando)
                conexao.commit()

                acao = 'criou_conta'
                res = registrar_log(email,acao)

                return True
            except:
                return False
    else:
        return False
 

# Logar Conta:
def logar_conta(email,senha):
    email_valido = verificar_validade_email(email)
    string_vazia = verificar_string_vazia(senha)

    if (email_valido == True) and string_vazia == False:

        comando = f'SELECT * FROM jogadores WHERE email="{email}" AND senha="{senha}"'
        cursor.execute(comando)
        varredura = cursor.fetchall()

        if (len(varredura) == 0):
            return False
        else:
            return True
        

# Alterar Conta:
def alterar_conta(campo,novoDado,email):
    conexao.commit()

    email_valido = verificar_validade_email(email)
    campo_valido = verificar_validade_campo(campo)
    string_vazia = verificar_string_vazia(novoDado)
    email_cadastrado = verificar_uso_email(email)

    if (email_valido == True) and (campo_valido == True) and (string_vazia == False) and (email_cadastrado == True):
    
        try:
            comando = f'UPDATE jogadores SET {campo}="{novoDado}" WHERE email= "{email}"'
            cursor.execute(comando)
            conexao.commit()

            acao = 'alterou_conta'
            registrar_log(email,acao)

            return True
        except:
            return False
    else:
        return False


# Excluir Conta:
def excluir_conta(email):
    email_valido = verificar_validade_email(email)
    email_cadastrado = verificar_uso_email(email)

    if (email_valido == True) and (email_cadastrado == True):
        try:
            id = retornar_id_usuario(email)

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