# json.dump() writes dict to .json file. 

import json 
data = {"topic": "File Handling"}
with open("output.json", "w") as f:
    json.dump(data, f)