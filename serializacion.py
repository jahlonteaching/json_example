import json


data = {
    "nombre": "Pedro",
    "apellido": "Pérez",
    "pasatiempos": ["correr", "parapente", "cantar"],
    "edad": 35,
    "hijos": [
        {
            "nombre": "Max",
            "edad": 6
        },
        {
            "nombre": "Alicia",
            "edad": 8
        }
    ]
}


with open("data_file.json", mode='w', encoding='utf8') as file:
    json.dump(data, file)

json_str = json.dumps(data, indent=4)
print(json_str)
