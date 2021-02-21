def wordCount(sent):
    if len(sent)>0:
        wcount=sent.split(' ')
        return ("oh nice, you just told me what's on your mind in "+str(len(wcount))+" words!")


user=input("What's on your mind today?")
cnt=0
ask = ''
while True:
    if cnt==0 and len(user)>0:
        res=wordCount(user)
        ask=input(res+" Would you like to say something now?(Yes/No)")
    elif ask.upper()=='Y' or ask.upper()=="YES":
        user = input("What's on your mind this time?")
        res = wordCount(user)
        ask = input(res + " Would you like to say something now?(Yes/No)")
    elif ask.upper()=='N' or ask.upper()=="NO":
            print("Thank you for visiting. Bye!!!")
            break
    else:
        ask=input("You entered nothing. Would you like to say something now?(Yes/No)")
    cnt+=1