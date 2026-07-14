import json
def reads():
    with open("contact.json","r") as file:
        re = json.load(file)
    print(re)
def writes():
    with open("contact.json","r") as files:
        re = json.load(files)
    print(type(re))
    a={}
    a["name"] =input("Enter the name :")
    a["no"] = int(input("Enter Number"))
    re.append(a)
    with open("contact.json","w") as files:
        json.dump(re,files,indent=4)
def updates():
    with open("contact.json","r") as file:
        re = json.load(file)
    a =input("Enter the name :")
    b = int(input("Enter Number"))
    for i in re:
        if i.get("name","")==a:
            i["no"]=b        
    with open("contact.json","w") as files:
        json.dump(re,files,indent=4)
def deletes():
    with open("contact.json","r") as file:
        re = json.load(file)
    a =input("Enter the name :")
    res=[]
    for i in re:
        if not i.get("name","")==a:
             res.append(i)
    with open("contact.json","w") as files:
        json.dump(res,files,indent=4)
while(True):
    print("1.read 2.write 3.update 4.delte 5.end")
    ch =int(input("Enter Number :"))
    if(ch ==1):
        reads()
    elif ch==2 :
        writes()
    elif ch==3:
        updates()
    elif ch==4:
        deletes()
    else:
        break
    
