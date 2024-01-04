from src import *
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


# Criar Log
@cross_origin
@app.route('/log/criarLog/<string:email>,<string:acao>', methods=['GET'])
def registrarLog(email,acao):
    lista = ['deslogou_conta']
    if (acao in lista):
        return jsonify(src_registrarLog(email,acao))
    else:
        return jsonify(False)


# Criar Conta
@cross_origin
@app.route('/conta/criarConta/<string:nome>,<string:email>,<string:senha>', methods=['GET'])
def criarConta(nome,email,senha):
    return jsonify(src_criarConta(nome,email,senha))


# Logar Conta
@cross_origin
@app.route('/conta/logarConta/<string:email>,<string:senha>', methods=['GET'])
def logarConta(email,senha):
    return jsonify(src_logarConta(email,senha))


# Alterar Conta
@cross_origin
@app.route('/conta/alterarConta/<string:campo>,<string:novoDado>,<string:email>', methods=['GET'])
def alterarConta(campo,novoDado,email):
    return jsonify(src_alterarConta(campo,novoDado,email))


# Excluir Conta
@cross_origin
@app.route('/conta/excluirConta/<string:email>', methods=['GET'])
def excluirConta(email):
    return jsonify(src_excluirConta(email))


# Verificar Email
@cross_origin
@app.route('/conta/verificarEmail/<string:nome>,<string:email>,<codigo>')
def verificarEmail(nome,email,codigo):
    return jsonify(src_verificarEmail(nome,email,codigo))


#app.run(host='localhost',port=5000, debug=True)