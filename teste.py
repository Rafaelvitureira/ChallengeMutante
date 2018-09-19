import requests

url = "http://127.0.0.1:5000/mutant"

payload = "{\"dna\":[\"ATGCGA\",\"CAGTGC\",\"TTACTGT\",\"AGACGG\",\"CCCCTA\",\"TCACTG\"]}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "11f1fd0b-4c81-8e25-0b9d-e2a3cbe15f15"
    }

response = requests.request("POST", url, data=payload, headers=headers)

response2 = requests.get("http://127.0.0.1:5000/status")

print(response.text)
print(response2.text)