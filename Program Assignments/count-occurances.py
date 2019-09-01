# Write a Python program named count-occurrences.py that will take one command-line argument 
# and count the number of times that argument occurs on the standard input, 
# then print the count to standard output.

import sys

lines = sys.stdin.readlines()

lineNumber = 0
count = 0
for line in lines:
        lineNumber += 1
        if(line.lower().find(sys.argv[1]) != -1):
                count +=1

sys.stdout.write("That occured " + str(count) + " times\n")