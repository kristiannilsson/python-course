my_string = "loremipsum"

#loopa igenom sträng
for char in my_string:
    print(char)

#printar längden i strängen
print(len(my_string))

#man kan slica en sträng
#utelämnade argument default är starten av listan:slutet av listan:1
print(my_string[2:])

print('hej\"')

my_string = "LoRem ipSum"

print(my_string.lower()) #lowercase
print(my_string.upper()) #uppercase
print(my_string.title()) #titlecase

my_fruits = "apple banana grapes"
my_fruit_list = my_fruits.split()

print(my_fruits.split(" "))
print(my_fruit_list)

print(", ".join(my_fruit_list))

print(my_fruits.find("pear"))

"""
1. Strängar är listor (len())
2. Slica en sträng
3. Sätta ihop strängar
4. Escape \n
5. .lower(), .title(), .strip(), .upper()
6. .split()
7. .find()
8. .join()
"""