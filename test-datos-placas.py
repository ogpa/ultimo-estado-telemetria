import ast
import json
#f = open('placas.txt', 'r', encoding="utf-8")
dict_temp = f.replace('\\', "")
dict_temp = dict_temp.replace('"{', "{")
dict_temp = dict_temp.replace('}"', "}")
dict_temp = dict_temp.replace('"[', "[")
dict_temp = dict_temp.replace(']"', "]")

dict = json.loads(dict_temp)
lista_ids = []
lista_placas = []

for d in dict:
    for sd in d:
        try:
            lista_placas.append(sd["d"]["nm"])
            lista_ids.append(sd["i"])
        except Exception as e:
            pass
print(len(lista_ids))
print(lista_ids)
print(len(lista_placas))
print(lista_placas)