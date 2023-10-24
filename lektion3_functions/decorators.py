def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(kwargs)
        print("Before")
        func(*args, **kwargs)
        func("1234", a="1")
        print("After")
    return wrapper

@my_decorator
def my_function(*args, **kwargs):
    pass

#my_function = my_decorator(my_function)

my_function()

def my_other_function(str_to_print):
    print(str_to_print)



#my_dict = {"a": my_function}

#my_function(my_other_function)



"""
1. Funktioner som variabel
2. Visa utan syntax
3. Visa med @
4. Visa argument
"""


