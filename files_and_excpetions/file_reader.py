
readfile = 'read.txt'

#reads in file. prints all contents
# with open(readfile) as file:
#     contents = file.read()
# print(contents)

#read in file by line. print each line
with open(readfile) as file:
    for line in file:
        print(line.rstrip())

writefile = 'write.txt'
#writing to a file
with open(writefile, 'w') as file:
    file.write("I'm writing to a file\n")
    file.write("I hope its working\n")

#append to a file
with open(writefile, 'a') as file:
    file.write("Hey, I think that worked\n")
    file.write("Now I am appending to the file\n")