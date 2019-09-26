
filename = 'text.txt'

#reads in file. prints all contents
with open(filename) as file:
    contents = file.read()
print(contents)