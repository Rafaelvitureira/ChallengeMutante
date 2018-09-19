# ChallengeMutante

import requests

url = "http://127.0.0.1:5000/mutant"

#json com a lista de listas do dna
payload = "{\"dna\":[\"ATGCGA\",\"CAGTGC\",\"TTACTGT\",\"AGACGG\",\"CCCCTA\",\"TCACTG\"]}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "11f1fd0b-4c81-8e25-0b9d-e2a3cbe15f15"
    }
    
 #necessario colocar data e headers gerados no postman

response = requests.request("POST", url, data=payload, headers=headers)

#para realizar a consulta de quantos mutantes e quantos humanos via get com /status conforme abaixo

response = requests.get("http://127.0.0.1:5000/status")

Banco de dados local, API local.
