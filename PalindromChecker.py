str = input("Enter The String :")
i=0
j=len(str)-1
flag =True
while(i!=j):
    if(not str[i]== str[j]):
        flag = False
    i+=1
    j-=1
if flag:
    print("yes")
else:
    print("not")
        