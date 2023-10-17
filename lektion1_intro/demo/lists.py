#lista
my_list = ["banana", "apple", "pear", "passionfruit", "grapes"]

#lägga till i lista
my_list1 = []
my_list1.append("pineapple")
print(my_list1)

#modifiera element
my_list[1] = "pineapple"

my_list.remove("banana")
my_list.pop(2)
# remove tar bort värdet, pop tar bort givet index
my_list = ["22", "1", "9", "70", "55", "grapes"]
my_list.insert(0, "grapes")
my_string = "lorem ipsum"

#sortera
my_list.sort()
print(my_list)

# längd
print(len(my_list))
print(len(my_string))

# slicing [start:stop:step]
my_list = ["22", "1", "9", "70", "55", "grapes"]
my_list2 = "apple"
print(my_list[-1:2:-1])
print(my_list + my_list2)

"""
1. Skapa en lista
2. Vad kan finnas i en lista?
3. Tomma listor
4. .append()
5. Komma åt element med l[0]
6. Modifiera en lista
7. Ta bort element med .remove()
8. .insert()
9. .pop()
10. .len()
11. .sort()
12. Slicing [1:3]
"""