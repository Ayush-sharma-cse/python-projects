print("simple calculator")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")

choice=int(input("enter your choice(1-4):"))

n=float(input("enter first number:"))
n2=float(input("enter 2nd number"))

if choice==1:
    print("result:",n+n2)
    
elif choice==2:
    print("result=",n-n2)

elif choice==3:
    print("result=",n*n2)
    
elif choice==4:
    if n2!=0:    
        print("result=",n/n2)
    else:
        print("error:division by zero")
else:
        print("invalid choice")