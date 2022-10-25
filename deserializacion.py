import json

with open("data_file.json", mode='r', encoding='utf8') as file:
    data = json.load(file)

print(data)

json_str = """
{
   "eBooks":[
      {
         "language":"Pascal",
         "edition":"third"
      },
      {
         "language":"Python",
         "edition":"four"
      },
      {
         "language":"SQL",
         "edition":"second"
      }
   ]
}
"""
data = json.loads(json_str)
print(data)
