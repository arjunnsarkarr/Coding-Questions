# def fibonnaachi(n):
#     if n <= 1:
#         return n
#     else :
#         return (fibonnaachi(n-1) + fibonnaachi(n-2))
# a = 5
# if a <= 0: 
#     print("Enter a positive number")
# else:
#     print("Fibonacci sequence:")
#     for i in range(a):
#         print(fibonnaachi(i))



previous_num = 0
next_num = 1

input = 5
if(input <= 0  ):
    print("Enter a positive number")
else:
    print("Fibonacci sequence:")
    print("0")
    print("1")

for i in range(input):
    temp = previous_num + next_num
    previous_num = next_num
    next_num = temp
    print(temp)










