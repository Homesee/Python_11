a=7
# if(a%2==0):
#     print(f'{a} is a even number')
# else:
#     print(f'{a} is odd')

a=int(input("Enter a your percentage "))
if(a>=80 and a<=100):
   #print("Distinction")
   if(a==85):
       print("Medium Distinction")
   elif(a==82):
       print("Just Distinction")
   else:
       print("Distinction Holder")
elif(a>=60 and a<80):
    print("you got a first division")
elif(a<60 and a>=50):
    print("you got a second division")
elif(a<50 and a>=40):
    print("you got a third division")
else:
    print("you are a fail")
     
    

