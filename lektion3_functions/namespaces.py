"""Demo om namespaces. 
Här lär vi oss om namespaces och dokumentation"""
import pprint
pp = pprint.PrettyPrinter(indent=4)

#Printar allt inbyggt
print(dir(__builtins__))
pp.pprint(dir(__builtins__))

#Globala variabler
a = "123"
b = "12"

def greet():
    """Greets the user"""
    #Lokalt scope
    global b #Om du inte använder denna syftar du på den lokala variabeln b.
    b = "1234"
    print(locals()) #printar alla referenser tillgängliga i det lokala scopet. Om du är i det globala scopet är det samma globals()

    print(b)
    print("Hello!")



print(greet.__doc__) #Printar doc-string som markeras med """Text""". --> Greets the user


greet()
print(globals())
print(locals())
"""
1. Allt är dictionaries!
2. Varför är print() alltid tillgänglig? dir(__builtins__)
3. Global Namespace. globals()
4. Local namesapce. locals()
5. nonlocal för nästlade funktioner
6. global för local-scope
7. LGB
"""
