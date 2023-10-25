#SyntaxError
my_variable = 123

#IndentationError
a = 1

#NameError
#print(b)

#IndexError
l = [1, 2, 3]
#print(l[3])

#KeyError
d = {"a": 1, "b": 2}
#print(d.get("c", "Hittade inte värdet"))

#kasta egen exception
#raise SyntaxError("Wrong syntax pal!")

class MyCustomError(Exception):
    pass

def fetch_data():
    raise MyCustomError("Misslyckades med att ansluta till databasen!")
    return {"name": "Kristian", "interests": "Python"}

try:
    fetch_data()    
except SyntaxError:
    print("Kunde inte hämta data!")
except MyCustomError:
    print("Custom error!")



"""
1. SyntaxError, IndentationError, NameError, IndexError, KeyError
2. raise() Exception
3. try-except fånga vissa specifika errors, fånga flera i samma handler
4. else: Om inte något error sker!
5. finally:
6. Egna exceptions.
"""