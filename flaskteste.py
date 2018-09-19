import pymysql as pymysql
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mutant', methods=['POST'])
def mutant():
    data = request.get_json()

    dna = data['dna']

    return jsonify({'dna':dna})

@app.route("/status", methods=['GET'])
def conectabanco():
    listamutantes = []
    listahumano = []
    aServidor = "localhost"
    aUsuario = "root"
    aSenha = "rafaelvitureira"
    aBanco = "mutante"

    db = pymysql.connect(aServidor, aUsuario, aSenha, aBanco)
    cursor = db.cursor()

    def Busca_SQL(pSQL):
        try:
            cursor.execute(pSQL)
            results = cursor.fetchall()
            return results
        except:
            print("Erro: Não foi possível buscar os dados")
            return 0

    result = Busca_SQL("select count(iddna) from mutantes where mutante = 1")
    for row in result:
        listamutantes.append(row[0])
    result = Busca_SQL("select count(iddna) from mutantes where iddna = 0")
    for row in result:
        listahumano.append(row[0])

    return jsonify({'Mutantes': listamutantes,'Humanos':listahumano})


if __name__ == '__main__':
    app.run()