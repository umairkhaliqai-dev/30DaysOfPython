# json.dumps() converts Python dict → JSON string.
import json 
dict_obj = {"course": "30DaysOfPython"}
json_str = json.dumps(dict_obj)
print(json_str)