import pymysql
from flask import Flask, request, jsonify

app = Flask(__name__)

nitrogen = []
matriz = []
linha = []

j = 1

def conectabanco():

    aServidor = "localhost"
    aUsuario = "root"
    aSenha = "rafaelvitureira"
    aBanco = "mutante"

    db = pymysql.connect(aServidor, aUsuario, aSenha, aBanco)
    cursor = db.cursor()
    return cursor,db

@app.route('/mutant', methods=['POST'])
def isMutante():
    cursor = conectabanco()

    data = request.get_json()

    dna = data['dna']
    print(dna)

    verificador = ''
    cont = 1
    contador = 0
    for i in range(len(dna)):
        for j in range(len(dna[i])):
            if dna[i][j] == dna[i][j - 1]:
                cont = cont + 1
            elif cont >= 3:
                verificador = True
                break
            else:
                cont = 0
                verificador = False

    for i in range(len(dna)):
        for x in range(len(dna[i])):
            if dna[x][i] == dna[x-1][i]:
                cont = cont + 1
            elif cont >= 3:
                verificador = True
                break
            else:
                cont = 0
                verificador = False


    for i in range(len(dna)):
        if dna[i][i] == dna[i-1][i-1]:
            cont = cont + 1
        elif cont >= 3:
            verificador = True
            break
        else:
            cont = 0
            verificador = False
        contador = contador + 1

    contador = 5
    for i in range(len(dna)):
        #print(dna[i][contador])
        if dna[i][contador] == dna[i+1][contador-1]:
            cont = cont + 1
        elif cont >= 3:
            verificador = True
            break
        else:
            cont = 0
            verificador = False
            break

        contador = contador-1

    print(verificador)
    if verificador==True:
        cursor,db = conectabanco()
        cursor.execute('insert into mutantes2 (mutante,humano) values ("True","False")')
        db.commit()
        cursor.close()
        print('executou')
    else:
        cursor,db = conectabanco()
        cursor.execute('insert into mutantes2 (mutante,humano) values ("False","True")')
        db.commit()
        cursor.close()
        print('executouelse')

    return jsonify({'DNA': verificador})

@app.route("/status", methods=['GET'])
def Busca_SQL():
    listamutantes = []
    listahumano = []
    try:
        cursor,db = conectabanco()
        cursor.execute('select count(mutante) from mutantes2 where mutante = "True"')
        result = cursor.fetchall()
        for row in result:
            listamutantes.append(row[0])
        cursor.execute('select count(humano) from mutantes2 where humano = "True"')
        result = cursor.fetchall()
        for row in result:
            listahumano.append(row[0])

    except:
        print("Erro: Não foi possível buscar os dados")

    return jsonify({'Mutantes': listamutantes[0],'Humanos':listahumano[0]})


if __name__ == '__main__':
    app.run()


