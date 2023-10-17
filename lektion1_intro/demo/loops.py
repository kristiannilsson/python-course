nums = [1, 2, 3, 4, 5]
fruits = ["Apple", "Banana", "Pear", "Pomegranate"]

#loopar igenom listan
for fruit in fruits:
    print(fruit)

#loopar igenom 5 gånger
for i in range(5):
    print(i)
counter = 0

#loopar igenom tills counter är 5
while counter < 5:
    counter += 1
    if counter == 2:
        # loopen breaker (avbryts) när python stöter på break
        # för att loopen bara ska fortsätta finns continue
        break

list_comprehension = [num*2 for num in nums]
"""
1. Loopa igenom listor
2. In range
3. While loop (infinite loops, Ctrl + C)
4. break, continue
5. List comprehension
"""