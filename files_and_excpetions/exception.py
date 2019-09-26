# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("HEY! You cant divide by zero")


# filename = 'this_file_doesnt_exist.txt'
# try:
#     with open(filename) as file:
#         lines = file.readlines()
# except FileNotFoundError:
#     message = "Can't find file {0}.".format(file)

print("Enter two numbers. I'll divide them")

x = input("First Number: ")
y = input("Second Number: ")

try:
    result = int(x) / int(y)
except ZeroDivisionError:
    print("Hey! You cant divide by zero")
else:
    print(result)