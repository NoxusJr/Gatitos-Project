from src import *
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


# Criar Log
@cross_origin
@app.route('/log/criarLog', methods=['POST'])
def rota_registrar_log():
    dados = request.get_json()
    email = dados['email']
    acao = dados['acao']

    lista = ['deslogou_conta']
    if (acao in lista):
        return jsonify(registrar_log(email,acao))
    else:
        return jsonify(False)


# Criar Conta
@cross_origin
@app.route('/conta/criarConta', methods=['POST'])
def criarConta():
    dados = request.get_json()
    nome = dados['nome']
    email = dados['email']
    senha = dados['senha']

    return jsonify(criar_conta(nome,email,senha))


# Logar Conta
@cross_origin
@app.route('/conta/logarConta', methods=['POST'])
def logarConta():
    dados = request.get_json()
    email = dados['email']
    senha = dados['senha']

    return jsonify(logar_conta(email,senha))


# Alterar Conta
@cross_origin
@app.route('/conta/alterarConta', methods=['PUT'])
def alterarConta():
    dados = request.get_json()
    campo = dados['campo']
    novo_dado = dados['novoDado']
    email = dados['email']

    return jsonify(alterar_conta(campo,novo_dado,email))


# Excluir Conta
@cross_origin
@app.route('/conta/excluirConta/<string:email>', methods=['DELETE'])
def excluirConta(email):
    return jsonify(excluir_conta(email))


# Verificar Email
@cross_origin
@app.route('/conta/verificarEmail', methods=['POST'])
def verificarEmail():
    dados = request.get_json()
    nome = dados['nome']
    email = dados['email']
    codigo = dados['codigo']

    return jsonify(verificar_email(nome,email,codigo))


# Salvar Ponto
@cross_origin
@app.route('/pontos/salvarPonto/', methods=['POST'])
def salvarPonto():
    dados = request.get_json()
    email = dados['email']
    id_jogo = dados['id_jogo']
    pontos = dados['pontos']

    return jsonify(salvar_ponto(email,id_jogo,pontos))


# Retornar Ponto
@cross_origin
@app.route('/pontos/retornarPonto/', methods=['POST'])
def retornarPonto():
    dados = request.get_json()
    email = dados['email']
    id_jogo = dados['id_jogo']

    return jsonify(retornar_ponto(email,id_jogo))

# Retornar Ranking
@cross_origin
@app.route('/pontos/retornarRanking/', methods=['POST'])
def retornarRanking():
    dados = request.get_json()
    id_jogo = dados['id_jogo']
    
    return jsonify(retornar_ranking(id_jogo))