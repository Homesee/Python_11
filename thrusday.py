print("this is a Thrusday class")
a=int(input("Enter number"))
print(a)
if(a>=0):
    if(a%2==0):
        print("this is a even number")
    elif(a==0):
        print("this is nither positive nor negative")
    else:
        print("this number is odd")
else:
    print("this number is negative")