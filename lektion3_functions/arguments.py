def my_function(a, b, c="5"): #a och b är positionella argument, c är ett namngivet argument. Namngivna argument har ett default-värde 
    print("A", a)
    print("B", b)
    print("C", c)

#Kallar på my_function och skriver över värdet i c.
my_function("1", "2", c="6")

#Hur kommer det sig att print tar hur många argument som helst?
print(1, 2, 3, 4, 5)

#*args tillåter dig att ta hur många positionella argument som helst.
#**kwargs tillåter dig att ta hur många namngivna argument som helst.
#args och kwargs är godtyckliga namngivna, kan heta vad som helst så länge man har * respektive **
def my_function(a, b, c="5", *args, **kwargs): 
    print("A", a) 
    print("B", b)
    print(args)
    print(kwargs) 

# * och ** kan användas åt andra hållet också
l = [1, 2, 3, 4]
dict = {"a": 1, "b": 1}

print(*l) # print(1, 2, 3, 4)
print(my_function(**dict)) # my_function(a=1, b=1)

#positionella argument måste förekomma före namngivna.
def my_funktion(x=0, y=0, z):
    pass

"""
1. Positional Arguments
2. Default arguments
3. Keyword arguments
4. Hur många argument tar print? (*args), args är godtyckligt namngiven
5. **kwargs
6. * och ** operatorn
"""
