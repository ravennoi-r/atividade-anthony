import requests

resposta = requests.get("https://example.com")

print(resposta.status_code)