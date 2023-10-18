import json


def spam():
    return "Eggs"


my_dict = {"my_function": spam}
# print(my_dict["my_function"]())

f = open("car.json", mode="r", encoding="utf-8")
contents = json.load(f)
print(contents)
new_car = {"brand": "Volvo", "year": 2008}
contents["cars"] = contents["cars"] + [new_car]
print(contents)
f.close()

f = open("car.json", "w", encoding="utf-8")
json.dump(contents, f)

""" with open("poem.txt") as f:
    contents = f.read()
    print(contents) """


"""
1. Öppna en ny fil, open() .close()
2. .readlines(), .read()
3. write, encoding=utf-8
4. json.load()
5. json.dump()
"""
