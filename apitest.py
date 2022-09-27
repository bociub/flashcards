#https://dictionaryapi.dev/


import requests,json

urlbase = "https://api.dictionaryapi.dev/api/v2/entries/en/"
theword = "hello"
url = urlbase + theword

response = requests.request("GET", url)
response = response.text
x = json.loads(response)
x = x[0]
#print(type(x))
#print(x)
print("this  ",x["word"], x["phonetics"][1]["text"], x["phonetics"][1]["audio"] )