# Task 1: Customer Service Ticket Tracker 
# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
# Problem Statement: Develop a program that:
#   Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#   Implement functions to:
#           Open a new service ticket.
#           Update the status of an existing ticket.
#           Display all tickets or filter by status.
#           Initialize with some sample tickets and include functionality for additional ticket entry.

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(tickets, ticket_id, customer_name, issue_description):
    if ticket_id not in tickets:
        tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
        print(f"Ticket '{ticket_id}' added.")
    else:
        print(f"Ticket '{ticket_id}' already exists.")

def update_status(tickets, ticket_id, status):
    if ticket_id in tickets:
        tickets[ticket_id]["Status"] = status
        print(f"Ticket '{ticket_id}' status updated to {status}.")
    else:
        print(f"Ticket '{ticket_id}' does not exist.")

def display_tickets(tickets):
    for tid, ticket in tickets.items():
        print(f"Ticket ID: {tid}, Customer: {ticket['Customer']}, Issue: {ticket['Issue']}, Status: {ticket['Status']}")



while True:
    print("\nCustomer Service Ticket Tracker")
    print("1: Add Ticket\n2: Update Ticket Status\n3. Display Tickets\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        tid = input("Enter ticket ID: ")
        customer_name = input("Enter customer name: ")
        issue_description = input("Enter issue description: ")
        add_ticket(service_tickets, tid, customer_name, issue_description)
    elif choice == "2":
        tid = input("Enter ticket ID: ")
        status = input("Enter status (open/closed): ")
        update_status(service_tickets, tid, status)
    elif choice == "3":
        display_tickets(service_tickets)
    elif choice == "4":
        print("Exiting Program.")
        break
    else:
        print("Invalid choice. Please try again.")  