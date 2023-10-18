

my_dict = {}

my_dict["brand"] = "Ford"
my_dict["brand"] = "Saab"
my_dict["year"] = 1990
my_dict["miles"] = 1990

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.update({"price": 2000000})
my_dict | {"price": 2000000}

print(my_dict.get("color", "red"))

"""
1. Basic syntax för en dictionary, komma åt värden
2. Skapa en tom dict och sedan lägg till nyckel
3. .update() ( | )
4. Skriva över värden
5. .get()
6. .pop()
7. .keys(), .values(), .items() loopa igenom (även bara dicten)
"""
