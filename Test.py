# input type
# n - total numbers
# [{Fruit,Quantity,Selling_price}]
# input
# [{apple,2,10},{orange,5,10},{grapes,10,5}]

# output
# Highest Selling Fruit : Grapes
# Total Selling : 120
# Average Selling : 40

def output(data):
    sorted_data = sorted(data,key=lambda x : x[1],reverse=True)
    total = 0
    for obj in sorted_data:
        total += obj[1] * obj[2]
    print("higest ", sorted_data[0][0])
    print("total : ",total)
    print("avg: ",total/ len(data))


data = []
n  = int(input())
for _ in range(n):
    name = input("Name: ")
    quantity = int(input("Quantity: "))
    price = int(input("Price: "))
    data.append([name,quantity,price])
print(data,"data")
output(data)





