a=[]
size = int(input("Enter the size of the list: "))
prod=1
for i in range(size):
    x=int(input())
    a.append(x)
    prod*=x
    
print(a)
print(prod)












#import numpy
#list = [57,99,108,90]
#result = numpy.prod(list)
#print(result)