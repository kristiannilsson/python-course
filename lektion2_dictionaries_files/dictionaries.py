

my_dict = {} #skapar en tom dict

my_dict["brand"] = "Ford" #lägger till nyckeln brand me värdet ford
my_dict["brand"] = "Saab" #uppdaterar nyckeln
my_dict["year"] = 1990 #lägger till nyckel
my_dict["miles"] = 1990 # -""-

print(my_dict.keys()) #ger oss alla nycklar i en lista
print(my_dict.values()) #ger oss alla värden i en lista
print(my_dict.items()) #ger oss alla nycklar och värden i en lista
my_dict.update({"price": 2000000}) #uppdaterar my_dict
my_dict | {"price": 2000000} #returnerar en ny mergad dict

print(my_dict.get("color", "red"))
# med get får du ett fallback värde. 
# Returnerar fallback värdet om nyckeln inte finns
# default fallbackvärde är None 

"""
1. Basic syntax för en dictionary, komma åt värden
2. Skapa en tom dict och sedan lägg till nyckel
3. .update() ( | )
4. Skriva över värden
5. .get()
6. .pop()
7. .keys(), .values(), .items() loopa igenom (även bara dicten)
"""
