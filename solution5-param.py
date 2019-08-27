
def printListOfInts(x, y):
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

# print("Prints a list of integers given two integers as input")
# printListOfInts(int(input("Enter first number: ")), int(input("Enter last number:  ")))

