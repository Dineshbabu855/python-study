class bank :
    __bankname ="SBI"
    def __init__(self,name,phone):
        self.__name=name
        self.__phone =phone
        self.__balance =0
    @property
    def name(self):
        return self.__name
    @property
    def phone(self):
        return self.__phone
    @property
    def balance(self):
        return self.__balance
    @classmethod
    def get_bankname(cls):
        return cls.__bankname
    @phone.setter
    def phone(self,phoneno):
        self.__phone = phoneno
    def deposit(self,balance):
        self.__balance+=balance
        print("deposited ")
    def withdraw(self,ammount):
        if self.__balance>=ammount:
            self.__balance-=ammount
            print("Withdraw succesfully")
        else:
            print("not enfough money")
def acc_operation(acc):
    while(True):
        print("1.get name 2.get phone number 3.get balance 4.get bankname 5.set phone number , 6.deposit 7.withdraw 8.exit")
        ch = int(input("Enter the choice :"))
        if ch ==1 :
            print(acc.name)
        elif ch ==2 :
            print(acc.phone)
        elif ch ==3 :
            print(acc.balance)
        elif ch ==4 :
            print(acc.get_bankname())
        elif ch ==5 :
            ph = int(input("Enter the phone number :"))
            acc.phone = ph
            print("seteed succesfully")
        elif ch ==6:
            am = int(input("Enter the deposit ammount :"))
            acc.deposit(am)
        elif ch ==7:
            am = int(input("Enter the withdraw ammount :"))
            acc.withdraw(am)
        else:
            break
account =[]
while(True):
    print("1.create an account \n2.delete an account \n3.enter an account \n4.exit")
    ch = int(input("Enter the choice :"))
    if 1 ==ch :
        name = input("Enter the name :")
        no = int(input("Enter the Number :"))
        ammount = int(input("Enter the intial Ammount :"))
        acc = bank(name,no)
        acc.deposit(ammount)
        account .append(acc)
    elif 2==ch:
        name = input("Enter the name :")
        flag =True
        for i in range(len(account)):
            if account[i].name ==name:
                account.pop(i)
                flag = False
                print("removed succesfully")
                break
        if flag :
            print("Not found")
    elif 3==ch :
        name = input("Enter the name :")
        flag =True
        for acc in account:
            if acc.name ==name:
                flag = False
                print(f"Entered to Account : {name}")
                acc_operation(acc)
                break
        if flag :
            print("Not found")
    else:
        break
