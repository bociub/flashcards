#https://dictionaryapi.dev/


import requests

urlbase = "https://api.dictionaryapi.dev/api/v2/entries/en/"
theword = "hello"
url = urlbase + theword

response = requests.request("GET", url)

print(response.text)