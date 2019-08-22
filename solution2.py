# Reads from user, 2 numbers (x & y). 
# Then prints the sequence of integers (one per line) going from x to y (including both )

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

if x >= y :
    for index in reversed(range(y, x+1)):
        print(index)
else:
    for index in range(x, y+1):
        print(index)
