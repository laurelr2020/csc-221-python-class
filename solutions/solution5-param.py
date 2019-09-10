import sys

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

print(sys.argv)
printListOfInts(int(sys.argv[1]), int(sys.argv[2]))