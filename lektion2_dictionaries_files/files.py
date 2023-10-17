import json

f = open("car.json")
dict = json.load(f)
dict["color"] = "grey"
out_file = open("car2.json", "w")
json.dump(dict, out_file)

"""
1. Öppna en ny fil, open() .close()
2. .readlines(), .read()
3. write, encoding=utf-8
4. json.load()
5. json.dump()
"""