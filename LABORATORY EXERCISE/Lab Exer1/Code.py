tickets = []

def data():
    data = [
        ("INC1392939", "BOT-Inventory", "Failed to generate the daily report"),
        ("INC1392940", "BOT-Email", "Failed to send the scheduled notification"),
        ("INC1392941", "BOT-DataSync", "Encountered an error during data transfer"),
        ("INC1392942", "BOT-Invoice", "Failed to process an invoice"),
        ("INC1392943", "BOT-Report", "Failed to generate the weekly report"),
        ("INC1392944", "BOT-FileTransfer", "Failed to upload the required file"),
        ("INC1392945", "BOT-DataEntry", "Encountered an error while entering records"),
        ("INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"),
        ("INC1392947", "BOT-Validation", "Failed to validate the submitted records"),
        ("INC1392948", "BOT-Notification", "Failed to send the system alert"),
    ]
    for ticket_id, ticket_bot, ticket_description in data:
        tickets.append({"id": ticket_id, "bot": ticket_bot, "description": ticket_description})


def add_ticket():
    print("\nAdd a new ticket:")
    ticket_id = input("Enter ticket ID: ")
    ticket_bot = input("Enter ticket bot: ")
    ticket_description = input("Enter ticket description: ")
    tickets.append({"id": ticket_id, "bot": ticket_bot, "description": ticket_description})
    print("                                                             Ticket added successfully!   ")
    
    if input("\nPress X to exit or any other key to continue: ").lower() == 'x':
         return
    else: 
        add_ticket()

def remove_ticket():
    print("\nRemove a ticket:")
    display_tickets()
  
    ticket_id = input("Enter ticket ID to remove: ")
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            tickets.remove(ticket)
            print("                                                             Ticket removed successfully!   ")
            return
    print("                                                                     Ticket not found.")
    if input("Press X to exit or any other key to continue: ").lower() == 'x':
                return
    else:
        remove_ticket()

def search_ticket():
    print("\nSearch for a ticket:")
    ticket_id = input("Enter ticket ID to search: ")
    
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            print(f"INFO FOUND: {ticket['id']}, {ticket['bot']}, {ticket['description']}")
            return
    print("                                                                     Ticket not found.")
 
def display_tickets(display=False):
    print("")
    print("DISPLAY ALL TICKETS:")
    if not tickets:
        print("                                                                 No tickets available.")
        return
    for ticket in tickets:
        print(f"{ticket['id']}, {ticket['bot']}, {ticket['description']}")
    if display:
        if input("Press X to exit or any other key to continue: ").lower() == 'x':
            return

def ticket_count():
    print(f"\nTotal number of tickets: {len(tickets)}")
    return

def main():
    data()
    while True:
        print("")
        print("Ticket Management System")
        print("1. Add Ticket")
        print("2. Remove Ticket")
        print("3. Search Ticket")
        print("4. Display Tickets")
        print("5. Ticket Count")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_ticket()
        elif choice == '2':
            remove_ticket()
        elif choice == '3':
            search_ticket()
        elif choice == '4':
            display_tickets()
        elif choice == '5':
            ticket_count()
        elif choice == '6':
            exit = input("Are you sure do you want to exit (Y/N)? ").lower()
            if exit == 'y':
                print("Exiting the program.")
                break
            if exit == 'n':
                print("Returning to the main menu.")
                continue
            else:
                print("Invalid.")
                return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()