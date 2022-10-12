import json
mi_json = open("datos.json","r",encoding="utf-8")
print(mi_json)
json_datos = mi_json.read()
datos = json.loads("json_datos")
print("Json_datos: ",json_datos)
print("Datos: ",datos)
print("Temperaturas: ",datos["temperaturas"])