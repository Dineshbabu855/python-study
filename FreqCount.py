str = input("Enter The String :")
l = str.split(" ")
dic={}
for i in l:
    dic[i] =dic.get(i,0)+1
for i in dic.keys():
    print(f"keys :{i} ,values :{dic.get(i)}")