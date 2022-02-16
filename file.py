# file=open("pople1.txt",'r')
# for each in file:
#     print(each)

# file=open("pople1.txt","r")
# print(file.read())

# with open("pople1.txt","w") as f:
# f.write("hello world")

# with open("pople1.txt", "w") as f:
#     f.write("Hello World!!!")

with open("pople1.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)
