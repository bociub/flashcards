import requests,json

def fetch(theword = "hello"):
    urlbase = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    url = urlbase + theword
    
    response = requests.request("GET", url)
    response = response.text
    x = json.loads(response)
    return x

def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)
            
            
fetched = fetch("yes")

x = item_generator(fetched, "audio")
for item in x:
    print(item)
    
x = item_generator(fetched, "text")
for item in x:
    print(item)
    
    
x = item_generator(fetched, "definition")
for item in x:
    print(item)
print()    
x = item_generator(fetched, "example")
for item in x:
    print(item)