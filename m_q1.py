a=["priyanka-shimla","neela-delhi","sashi-jaipur","sarika-delhi","deepti-shimla","haeshad-delhi","trishna-delhi"
,"pradeep-jaipur","sekha-delhi","anoop-delhi","balwinder-jaipur","i am amrita"]
f=open("pople1.txt","r+")
i=0
while i<len(a):
    f.write(a[i])
    f.write("\n")
    print(a[i])
    i=i+1
f.close()

# file=open('pople1.txt')
# data=file.read()
# print(data)
# file.close