# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# n = 5 
# print(factorial(n))


n = 5
temp = 1 
for i in range(n):
    temp = temp * n
    n = n - 1

print(temp)
