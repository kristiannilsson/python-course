#positionella argument kommer alltid före namngivna
# "=" anger ett default- eller fallbackvärde

def my_function(a, b, c, d="a"):
    print("A", a)
    print("B", b)
    print("C", c)
    print("D", d)

# Print tar oändligt antal argument hur kommer det sig?
# De använder sig av *args internt
print(4, 5, 6, 7, 8, 9, 10)

#*args lägger alla överflödiga positionella argument i en read-only lista (tuple)
#**kwargs lägger alla överflödiga namngivna argument i en dic
#args och kwargs kan döpas till vad som helst, men konventionen är args och kwargs.
def args_operator(*args, **kwargs):
    print(args)

def multiply(*factors):
    print(factors)
    product = 1
    for arg in factors:
        product *= arg
    return product

args_operator(1, 2, 3, first_value="a", b="b", c="c")

l = [1, 2, 3, 4]
dict = {"a": "first_value", "b": "second_value"}
#
# *l --> (1, 2, 3, 4)

print(multiply(*l, **dict)) # är ekvivalent med print(multiply(1, 2, 3, 4, a="first_value", b="second_value"))
"""
1. Positional Arguments
2. Default arguments
3. Keyword arguments
4. Hur många argument tar print? (*args), args är godtyckligt namngiven
5. **kwargs
6. * och ** operatorn
"""
