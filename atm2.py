x=int(input("Enter a withdraw amount "))
balance=10000
if(x==0):
    print("Zero amount cannot be withdrawn")
elif(x<0):
    print("Invalid amount")
elif(x<=500):
    print("Amount less than 500 cannot be taken")
elif(x==balance):
    print("Total amount cannot be withdrawn")
elif(x<balance):
    if(x%100==0):
        print(f"Here is your amount and remaining balance is {balance-x}")
    
    else:
        print("Amount must be taken that is multiply by 100")
else:
    print("Insufficient balance")