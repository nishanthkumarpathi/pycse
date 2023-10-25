import pandas as pd
import json

df = pd.read_json("simple.json", orient="values")

# with open("simple.json", "r") as json_file:
#     json_data = json.load(json_file)

# df = pd.DataFrame(json_data, index=[0])

df.to_csv("simple.csv", index=False)

# print(nishanth)
