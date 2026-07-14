import random
rn = random.randint(1,100)
print("Start guess number from 1 to 100")
while(True):
    guess = int(input("Enter Number :"))
    if(guess>rn):
        print(f"{guess} is high")
    elif(guess<rn):
        print(f"{guess} is low")
    else:
        print("guessed Number")
        break