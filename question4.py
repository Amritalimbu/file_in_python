a=['rishabh-meerut','imtiyaz-delhi','nilima-cochin','rati-shimla','ayishah-delhi',
"raghu-shimla",'naseer-kanpur','kartikeya-delhi','salma-jaipur','pankaj-delhi',
'bjijesh-delhi']
# f=open('qtion4.txt','a')
for i in a:
    f=open("delhi.txt","a")
    if i=="delhi":
        f.append(i)
    if i=="simls.txt":
        f.append(i)
    f.close()

# i=0
# while i<len(a):
#     f.write(a[i])
#     f.write("\n")
#     print(a[i])
#     i=i+1
# # f1=open("delhi.txt","w")
# f1=open("delhi.txt",'a')
# i=0
# while i<len(a):
#     if "delhi" in a[i]:
#         f1.write(a[i])
#         f1.write("\n")
#         print(a[i])
# f1.close()
# f.close()