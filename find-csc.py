#This program finds the first occuracne of the string "CSC" in the input stream and prints the line number it occurs on.
#The search is case-insenstitive
import sys

lines = sys.stdin.readlines()

lineNumber = 0
for line in lines:
    lineNumber += 1
    if(line.lower().find('csc') != -1):
        print(lineNumber)
        quit()