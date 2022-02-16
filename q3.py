# f=open("file_question3.text","a")
# banks_list = ["kotak","HDFC","RBL","SBI","Baroda"]
# i=0
# while i<len(banks_list):
#     f.write(banks_list[i])
#     f.write('\n')
#     print(banks_list[i])
#     i=i+1 
# f.close()

# bank=['axis','reserve','allahbad']
# f=open("file_question3.text","a+")
# i=0
# while i<len(bank):
#     f.write(bank[i])
#     f.write("\n")
#     i=i+1
# f.close

bank='xyz\n''reserve\n''allahbad'
f=open("file_question3.text","a")
f.write(bank)
f.close
