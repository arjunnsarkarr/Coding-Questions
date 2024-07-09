highest_selling_fruit = None
total_selling = 0
average_selling = 0 
max_quantity = 0
data = []

# for taking inputs
n  = int(input("Enter number"))
for _ in range(n):
    name = input("Name: ")
    quantity = int(input("Quantity: "))
    price = int(input("Price: "))
    data.append([name,quantity,price])


for fruit, quantity, price in data:
    total_selling += quantity * price
    if quantity > max_quantity:
        max_quantity = quantity
        highest_selling_fruit = fruit
    average_selling = total_selling / len(data)

# Print the results
print(f"Highest Selling Fruit : {highest_selling_fruit}")
print(f"Total Selling : {total_selling}")
print(f"Average Selling : {average_selling}")





# input type
# n - total numbers
# [{Fruit,Quantity,Selling_price}]
# input
# [{apple,2,10},{orange,5,10},{grapes,10,5}]

# output
# Highest Selling Fruit : Grapes
# Total Selling : 120
# Average Selling : 40
