#en decorator används för att modifiera beteendet hos en underliggande funktion.
# syntaxen ser ut såhär:
#@my_decorator
#def my_function():
#   pass
# och är lika med: my_function = my_decorator(my_function)
# decoratorn måste alltså returnera en funktion.


#returnerar en funktion som printar före och efter funktionen kallas.
def print_before_and_after(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} started!")
        func(*args, **kwargs) #args och kwargs gör att decoratorn skickar vidare argumenten den fick in i funktionen.
        print(f"{func.__name__} has finished!")
    return wrapper

#med en decorator binder man om referensen enligt nedan.
@print_before_and_after # say_hello = print_before_and_after(say_hello)
def say_hello(name):
    print(f"Hello {name}")

say_hello("Kristian")

#Hur exempelvis decorators kan användas i flask.
@app.route("/home")
def my_route():
    return "index.html"

# Decorators kan ta in argument. Då måste man ha ytterligare en wrapper då syntaxen vill ha ett enda argument, funktionen som den wrappar.
def repeat(times):
    def decorator_repeat(func): #Här hade vi kunnat börja ifall decoratorn inte tog några argument.
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

#Decoratorn kan förändra beteendet på vilket sätt som helst.
#Här kör vi inte ens funktionen, utan printar endast 'modified'
def modify_return(func):
    def wrapper(*args, **kwargs):
        print("modified")
    return wrapper

@repeat(5) # greet = repeat(5)(greet)
@modify_return # greet = modify_return(greet)
def greet():
    print("Greetings")

greet()

# Du kan binda funktioner till variabler.
a = greet
print(a)
a()
"""
1. Funktioner som variabel
2. Visa utan syntax
3. Visa med @
4. Visa argument
"""


