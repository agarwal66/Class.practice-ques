def max(a,b,c):
    if (a>b):
        if (a>c):
            print(a,"is largest")
        else:
            print(c,"is largest")
    else:
        if(b>c):
            print(b,"is larhest")
        else:
            print(c,"is largest")                
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
num3=int(input("enter a number: "))
max(num1,num2,num3)






#num1=int(input())
#num2=int(input())
#num3=int(input())
#if (num1>=num2) and (num1>=num3):
    #m=num1
#elif (num2>=num1) and (num2>=num3):
    #m=num2
#else:
    #m=num3
#print("m",m)


