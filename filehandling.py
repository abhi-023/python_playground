# f = open(filename, mode)
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
# a:  open an existing file for append operation. It won’t override existing data.
#  r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.
# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)
# Python code to illustrate read() mode
file = open("file.txt", "r")
print (file.read())
# Python code to illustrate read() mode character wise
file = open("file.txt", "r")
print (file.read(5))
# Python code to create a file
file = open('file.name','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()
# Python code to illustrate append() mode
file = open('file.name','a')
file.write("This will add this line")
file.close()
# Python code to illustrate with()
with open("file.txt") as file:
    data = file.read()
# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
    f.write("Hello World!!!")
# Python code to illustrate split() function
with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
# tell
# define the location of the File Handle in the file.
fp = open("file.name", "mode")
print(fp.tell())
# seek
# seek() function is used to change the position of the File Handle to a given specific position.
# Opening "GfG.txt" text file
f = open("file.name", "r")
# Second parameter is by default 0
# sets Reference point to twentieth
# index position from the beginning
f.seek(20)
# prints current position
print(f.tell())
print(f.readline())
f.close()