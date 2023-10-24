"""Demo om namespaces. 
Här lär vi oss om namespaces och dokumentation"""
import pprint
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(__builtins__)
print(dir(__builtins__))

# ligger i det global namespacet
a = 123
b = "lorem ipsum"

#locals() printar det nuvarande namespacet. Här är globals samma som locals()
print(globals() == locals())

def add_two(a):
    """Function adds two to the argument a"""
    num_to_add = 2
    #b tar företräde här
    #använder du global syftar du på b i det globala namespacet.
    global b
    b = 2
    print(b)
    
    return a + num_to_add
print(add_two(5))
#print(globals())
"""
1. Allt är dictionaries!
2. Varför är print() alltid tillgänglig? dir(__builtins__)
3. Global Namespace. globals()
4. Local namesapce. locals()
5. nonlocal för nästlade funktioner
6. global för local-scope
7. LGB
"""

def enclosing_function():
  var = "value"
  print(locals())
  def nested_function():
    #nonlocal syftar på var ett steg upp
    nonlocal var
    var = "new_value"  

  nested_function()
  print(var)

enclosing_function()