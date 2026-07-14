def retry(func):
    def wrapper(*args,**kwargs):
        att = 3
        for i in range(1,att+1):
            try:
                return func(*args,**kwargs)
            except Exception as e :
                print("you are given ",e," attempt:",i)
        raise Exception("All 3 Attempt are failed")
    return wrapper
@retry            
def login():
    str = input("Enter the email")
    if len(str) <= 10 or str[-10:] != "@gmail.com":
        raise Exception("invaildemail")
    password = input("Enter password")
    print("logined succesfully")
login()