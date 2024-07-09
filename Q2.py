class Ticket:
    def __init__(self, num_guests):
        self.num_guests = num_guests
        self.guests = []

    def add_guest(self, name, age):
        self.guests.append({'name': name, 'age': age})

    def calculate_total_price(self):
        total_price = 0
        for guest in self.guests:
            age = guest['age']
            if age <= 2:
                total_price += 0
            elif 2 < age < 18:
                total_price += 100
            elif 18 <= age < 60:
                total_price += 500
            else:
                total_price += 300
        return total_price

    def display_ticket_details(self):
        for i, guest in enumerate(self.guests, 1):
            print(f"Guest {i} :  name: {guest['name']} , age: {guest['age']}")


# Example usage:
num_guests = int(input("Enter the total number of guests: "))
ticket = Ticket(num_guests)

for i in range(1, num_guests + 1):
    name = input(f"Enter the name of guest {i}: ")
    age = int(input(f"Enter the age of guest {i}: "))
    ticket.add_guest(name, age)

total_price = ticket.calculate_total_price()
print(f"Total charges: INR {total_price}")

print("\nTicket Details:")
ticket.display_ticket_details()




