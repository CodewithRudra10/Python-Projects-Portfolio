sum=0
while(True):
    UserInput=input("enter the price: ")
    if(UserInput!="q"):
        sum = sum+ int(UserInput)
        print(f"Order Total So Far {sum}")
    else:
        print("Thanks for Using our service kindly visit us again! /n your total bill is: ",sum)
        break
    

