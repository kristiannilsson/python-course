import json  # importerar json modulen

# öppnar filen car.json i read-mode. Encoding används om du exempelvis har åäö
# w är writemode
f = open("car.json", mode="r", encoding="utf-8")
contents = json.load(f) #laddar in filen som en python dict
f.close()
print(contents)
new_car = {"brand": "Volvo", "year": 2008}
contents["cars"] = contents["cars"] + [new_car] #uppdaterar vår nya dict

#öppnar filen för att skrivas
f = open("car.json", "w", encoding="utf-8")
json.dump(contents, f) #dumpar ner content i file

#alternativ och mer "pythonic" syntax
#här slipper du stänga filen
with open("poem.txt") as f:
    contents = f.read()
    print(contents)


"""
1. Öppna en ny fil, open() .close()
2. .readlines(), .read()
3. write, encoding=utf-8
4. json.load()
5. json.dump()
"""
