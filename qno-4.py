a = int(input(""))  
for i in range(0,a+1):  
    for j in range(a-i,0,-1):  
        print(j, end=' ')  
    print('\r')  