print("Prints a list of integers given two integers as input")

x = int(input("Enter first number: "))
y = int(input("Enter last number:  "))


i = x
if x <= y:
    step = 1
    start = x
    stop = y + 1
else:
    step = -1
    start = x
    stop = y - 1

for i in range(start, stop, step):
    print(i)