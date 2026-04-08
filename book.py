# Train Ticket Booking System

tickets = []

def book_ticket():
    name = input("Enter Passenger Name: ")
    age = input("Enter Age: ")
    source = input("Enter Source Station: ")
    destination = input("Enter Destination Station: ")

    ticket = {
        "Name": name,
        "Age": age,
        "Source": source,
        "Destination": destination
    }

    tickets.append(ticket)
    print("\n✅ Ticket Booked Successfully!\n")


def view_tickets():
    if len(tickets) == 0:
        print("\nNo tickets booked.\n")
    else:
        print("\nBooked Tickets:")
        for i, ticket in enumerate(tickets, start=1):
            print(f"\nTicket {i}")
            for key, value in ticket.items():
                print(f"{key}: {value}")


def cancel_ticket():
    name = input("Enter Passenger Name to Cancel Ticket: ")

    for ticket in tickets:
        if ticket["Name"] == name:
            tickets.remove(ticket)
            print("\n❌ Ticket Cancelled Successfully!\n")
            return

    print("\nPassenger not found.\n")


while True:
    print("\n===== Train Ticket Booking System =====")
    print("1. Book Ticket")
    print("2. View Tickets")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        book_ticket()
    elif choice == '2':
        view_tickets()
    elif choice == '3':
        cancel_ticket()
    elif choice == '4':
        print("Thank you for using system 🚆")
        break
    else:
        print("Invalid Choice")
