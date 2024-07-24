print("WE HAVE THREE GOLDEN NUMBERS FROM 1 TO 200")
print("TRY YOUR LUCK")

n=5
for i in range (n):
    print("YOU HAVE",n," CHANCES")
    print("TRY AGAIN!!!")
    n=n-1
    k=int(input("ENTER THE NUMBER :"))
    if(k==61 and k<200):
        print("YOU WON")
        exit()
    elif(k<61 and k<200):
        print("HINT:::::::::GREATER")
    elif(k>61 and k<200):
        print("HINT::::::::::: LESSER")
    else:
        print("WRONG CHOICE!!! (NUMBER SHOUD BE BETWEEN 1 TO 200)")
        

