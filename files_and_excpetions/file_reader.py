
filename = 'read.txt'

#reads in file. prints all contents
# with open(filename) as file:
#     contents = file.read()
# print(contents)

#read in file by line. print each line
with open(filename) as file:
    for line in file:
        print(line.rstrip())