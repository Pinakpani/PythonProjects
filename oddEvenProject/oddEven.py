def oddEven(num):
    if (num%2==0) or num==0:
        return ("That is an even number!")
    else:
        return ("That is an odd number!")

def userInput(trial):
    if trial==0:
        a=input("What number are you thinking?")
        if a.isnumeric():
            return (oddEven(int(a)))
        else:
            return ("Invalid input. You were suppose to input a number.")
    elif trial>0:
        a=input("What number are you thinking this time?")
        if a.isnumeric():
            return (oddEven(int(a)))
        else:
            return ("Invalid input. You were suppose to input a number.")

cnt=0
result = userInput(cnt)
ask = input(result + " Have another?(Y/N):")
cnt+=1
if ask.upper()=='Y' or ask.upper()=="YES":
    while ask.upper()=='Y' or ask.upper()=="YES":
        if cnt>0:
            result = userInput(cnt)
            ask = input(result + " Have another?(Y/N):")
        cnt += 1
        if ask.upper()=='Y' or ask.upper()=="YES":
            result = userInput(cnt)
            ask = input(result + " Have another?(Y/N):")
        elif ask.upper()=='N' or ask.upper()=="NO":
            print("Thank you for visiting. Bye!!!")
        else:
            print("Wrong choice of answer. Sorry!!!")
            break
elif ask.upper()=='N' or ask.upper()=="NO":
    print("Thank you for visiting. Bye!!!")
else:
    print("Wrong choice of answer. Sorry!!!")


