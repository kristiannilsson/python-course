#SyntaxError
my_variable =? 123

#IndentationError
    a = 1

#NameError
print(b)

#IndexError
l = [1, 2, 3]
print(l[3])

#KeyError
d = {"a": 1, "b": 2}
print(d["c"])

#kasta egen exception
# raise SyntaxError("Wrong syntax pal!")

# egen custom exception
class MyCustomError(Exception):
    pass

def fetch_data():
    raise MyCustomError("Misslyckades med att ansluta till databasen!")
    return {"name": "Kristian", "interests": "Python"}

#try används när du vet med dig att koden du kommer att köra inte alltid fungerar.
# Det kan exempelvis vara att ansluta till en databas.
try:
    fetch_data()
#except används sedan för att fånga upp vissa beteenden. Du kanske vet med dig att det finns en sannolikhet att 
# du inte kan ansluta till databasen och skriver kod för att hantera detta.    
except SyntaxError:
    print("Kunde inte hämta data!")
except MyCustomError:
    print("Custom error!")
else: #else körs ifall ingen exception kastas under try-blocket
    print("Data hämtades!")
finally: #finally körs alltid oavsett. Används exempelvis för att stänga en öppen connection eller unsubscriba till en service.
    pass



"""
1. SyntaxError, IndentationError, NameError, IndexError, KeyError
2. raise() Exception
3. try-except fånga vissa specifika errors, fånga flera i samma handler
4. else: Om inte något error sker!
5. finally:
6. Egna exceptions.
"""