import json

with open("simple.json", "r") as json_file:
    json_data = json.load(json_file)

print(json_data['name'])
print(json_data['age'])
print(json_data['occupation'])
