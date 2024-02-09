from .interno import *
from .conexao import *
import smtplib
import email.message



def criar_conta(nome,email,senha):
    email_valido = verificar_validade_email(email)
    existe = verificar_uso_email(email)

    if (email_valido) and (existe == False):
                comando = f"INSERT INTO jogadores (nome,email,senha) VALUES ('{nome}','{email}','{senha}')"
                cursor.execute(comando)
                conexao.commit()

                acao = 'criou_conta'
                res = registrar_log(email,acao)

                return True
    else:
        return False
 

def logar_conta(email,senha):
    email_valido = verificar_validade_email(email)

    if email_valido:

        comando = f'SELECT * FROM jogadores WHERE email="{email}" AND senha="{senha}"'
        cursor.execute(comando)
        varredura = cursor.fetchall()

        if (len(varredura) == 0):
            return False
        else:
            return True
        

def alterar_conta(campo,novoDado,email):
    conexao.commit()

    email_valido = verificar_validade_email(email)
    campo_valido = verificar_validade_campo(campo)
    email_cadastrado = verificar_uso_email(email)

    if (email_valido) and (campo_valido) and (email_cadastrado):
    
            comando = f'UPDATE jogadores SET {campo}="{novoDado}" WHERE email= "{email}"'
            cursor.execute(comando)
            conexao.commit()

            acao = 'alterou_conta'
            registrar_log(email,acao)

            return True
    else:
        return False


def excluir_conta(email):
    email_valido = verificar_validade_email(email)
    email_cadastrado = verificar_uso_email(email)

    if (email_valido) and (email_cadastrado):
            id = retornar_id_usuario(email)

            comando = f'DELETE FROM jogadores WHERE email= "{email}"'
            cursor.execute(comando)
            
            comando_limpar_log = f'DELETE FROM log WHERE id_jogador={id}'
            cursor.execute(comando_limpar_log)

            conexao.commit()

            return True
    else:
        return False