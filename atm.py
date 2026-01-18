#x=int(input("Enter a number "))
# if(x==2):
#  print("this is a two")
# elif(x==3):
#  print("this is number three")
# elif(x==4):
#  print("this is number four")
# else:
#  print("This is a another number")
# if(x>0):
#     if(x%2==0):
#         print("this is even Number")
#     else:
#         print("this is odd number")
# elif(x==0):
#     print("this is zero Number")
# else:
#     print("this is negative number")

balance=10000
x=int(input("please enter a amount to be withdraw "))
if(x!=0 and x<500 and x<=balance):
    if(x==0):
        print("0 Amount cannot be withdrawn")
    if(x<500):
        print("less than 500 cannot be withdrawn")
    if(x%100==0):
        print(f'Successfully withdrawa and remaining amount is {balance-x}')
    else:
        print("Please enter a number divisible by 100 ")

elif(x>balance):
    print("Canot withdrawn this amount")

else:
    print("This is not valid number")
 
    













