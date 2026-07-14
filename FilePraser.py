import json
name = input("Enter file name :")
try:
    with open(name,"r") as file:
        re= json.load(file)
    a={}
    a["name"]= input("Enter name :")
    a["no"]= input("Enter Number :")
    re.append(a)
    with open("abc.json","w") as files:
        json.dump(re,files,indent=4)
except FileNotFoundError:
    print(f"{name} File Not Found")
except PermissionError:
    print(f"{name} for this file you have no permission")
except OSError:
    print("facing an OS or IO error")