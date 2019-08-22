# Reads from user, 2 numbers (x & y). 
# Then prints the sequence of integers (one per line) going from x to y (including both )

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x >= y:
    while y <= x:
        print(x)
        x -= 1
else:
    while x <= y:
        print(x)
        x += 1



