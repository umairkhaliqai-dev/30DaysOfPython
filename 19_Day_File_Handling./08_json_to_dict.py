# json.loads() parses JSON string → Python dict.
import json 
json_str = '{"name": "Python"}'
dict_obj = json.loads(json_str)
print(dict_obj["name"])