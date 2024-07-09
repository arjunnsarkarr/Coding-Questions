# input 
a = int(input("Enter 1st value "))
b = int(input("Enter 2nd value "))
sum=0
if(a>b):
    print("Wrong input")
else:
    for i in range(a,b+1):
        sum = sum + i ** 3

print(sum)

