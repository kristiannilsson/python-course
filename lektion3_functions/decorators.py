#en decorator används för att modifiera beteendet hos en underliggande funktion.
# syntaxen ser ut såhär:
#@my_decorator
#def my_function():
#   pass
# och är lika med: my_function = my_decorator(my_function)
# decoratorn måste alltås returnera en funktion.

#en funktion kan bindas till en variabel eller argument.
my_dict = {"a": my_function}

#en funktion kan ha en annan funktion som argument. my_other_function kan då kallas i my_function.
#my_function(my_other_function)


#decoratorn tar in en funktion som argument
def my_decorator(func):
    def wrapper(*args, **kwargs): #wrappern tar in args och kwargs, alltså alla argument som du ger till funktionen
        print("Before")
        func(*args, **kwargs) #kallar funktionen med argumenten som kommer in. Wrappern skickar bara vidare argumenten den får.
        #Viktigt att underliggande funktion kan ta emot dem.
        print("After")
    return wrapper
#Här läggs decoratorn in ovanför funktionen. Då modifierar vi my_functions beteende.
@my_decorator
def my_function(*args, **kwargs):
    pass

my_function()

# https://www.youtube.com/watch?v=BE-L7xu8pO4&ab_channel=b001





"""
1. Funktioner som variabel
2. Visa utan syntax
3. Visa med @
4. Visa argument
"""


