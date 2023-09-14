import sqlite3
from datetime import datetime

# Find an item in the library
def find_item(title):

    # Connect to the SQLite database
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Item WHERE Title = ?', (title,))
    item = c.fetchone()
    if item:
        print(f'Item found: {item}')
    else:
        print('Item not found')
    
    # Close the connection
    conn.close()

# Borrow an item from the library
def borrow_item(title, user_id, borrow_date, due_date):

     # Connect to the SQLite database
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute('SELECT Item_ID FROM Item WHERE Title = ?', (title,))
    item_id = c.fetchone()
    if item_id:
        item_id = item_id[0]
        c.execute('INSERT INTO Loan (Item_ID, User_ID, BorrowDate, DueDate, Fine) VALUES (?, ?, ?, ?, 0)', (item_id, user_id, borrow_date, due_date))
        conn.commit()
        print('Item borrowed successfully')
    else:
        print('Item not found')

    # Close the connection
    conn.close()

# Return a borrowed item
def return_item(title, user_id, return_date):

    # Connect to the SQLite database
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute('SELECT Item_ID FROM Item WHERE Title = ?', (title,))
    item_id = c.fetchone()

    if item_id:
        item_id = item_id[0]

        # Calculate the fine
        c.execute('SELECT DueDate FROM Loan WHERE Item_ID = ? AND User_ID = ? AND ReturnDate IS NULL', (item_id, user_id))
        due_date = c.fetchone()

        if due_date:
            due_date = due_date[0]

            due_date = datetime.strptime(due_date, '%Y-%m-%d')
            return_date = datetime.strptime(return_date, '%Y-%m-%d')

            days_late = (return_date - due_date).days
            # Calculate the fine
            fine = max(0, days_late) * 1

            # Update Loan table with ReturnDate and Fine
            c.execute('UPDATE Loan SET ReturnDate = ?, Fine = ? WHERE Item_ID = ? AND User_ID = ? AND ReturnDate IS NULL', (return_date, fine, item_id, user_id))
            conn.commit()
            print('Item returned successfully.')

            if fine>0:
                print("You returned the item late. Your fine is : $", fine)

        else:
            print('Item not found for the user or already returned.')
    else:
        print('Item not found')

    # Close the connection
    conn.close()

# Donate an item to the library
def donate_item(title, item_type, author_artist, genre, available_copies):

     # Connect to the SQLite database8

    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute('INSERT INTO Item (Title, Type, Author_Artist, Genre, Available_Copies) VALUES (?, ?, ?, ?, ?)', (title, item_type, author_artist, genre, available_copies))
    conn.commit()
    print('Item donated successfully')

    # Close the connection
    conn.close()

# Find an event in the library
def find_event(event_name):

     # Connect to the SQLite database
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute('SELECT * FROM Event WHERE Title = ?', (event_name,))
    event = c.fetchone()
    if event:
        print(f'Event found: {event}')
    else:
        print('Event not found')

    # Close the connection
    conn.close()

# Register for an event in the library
def register_event(Title, Description, Audience, Event_date, Room_ID):

    # Connect to the SQLite database
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute('INSERT INTO Event (Title, Description, Audience, Event_date, Room_ID) VALUES (?, ?, ?, ?, ?)', (Title, Description, Audience, Event_date, Room_ID))
    conn.commit()
    print('Event registered successfully')

    # Close the connection
    conn.close()

# Volunteer for the library
def volunteer(Name, Job_Titl):

     # Connect to the SQLite database
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute('INSERT INTO Personnel (Name, Job_Title) VALUES (?, ?)', (Name, Job_Titl))
    conn.commit()
    print('Volunteering record added successfully')

    # Close the connection
    conn.close()

# Add a help request to the database
def add_help_request(name, contact, question):
    # Connect to the SQLite database
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute('INSERT INTO Help_Request(Name, Contact, Question) VALUES (?, ?, ?)', (name, contact, question))
    conn.commit()
    print('Help request submitted successfully')

    # Close the connection
    conn.close()


while True:
    print("\nInstructions:")
    print("1. Find an item")
    print("2. Borrow an item")
    print("3. Return an item")
    print("4. Donate an item")
    print("5. Find an event")
    print("6. Register for an event")
    print("7. Volunteer")
    print("8. Ask Librarian")
    print("9. Exit")

    choice = input("Enter the number of the instruction (1-9): ")

    if choice == '1':
        item_title = input("Enter the title of the item to find: ")
        find_item(item_title)
    elif choice == '2':
        item_title = input("Enter the title of the item to borrow: ")
        user_id = int(input("Enter your user ID: "))
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        borrow_item(item_title, user_id, start_date, end_date)
    elif choice == '3':
        item_title = input("Enter the title of the item to return: ")
        user_id = int(input("Enter your user ID: "))
        return_date = input("Enter the return date (YYYY-MM-DD): ")
        return_item(item_title, user_id, return_date)
    elif choice == '4':
        item_title = input("Enter the title of the item to donate: ")
        item_type = input("Enter the type of the item: ")
        author = input("Enter the author of the item: ")
        category = input("Enter the category of the item: ")
        quantity = int(input("Enter the quantity of the item: "))
        donate_item(item_title, item_type, author, category, quantity)
    elif choice == '5':
        event_title = input("Enter the title of the event to find: ")
        find_event(event_title)
    elif choice == '6':
        event_title = input("Enter the title of the event to register for: ")
        description = input("Enter the description of the event: ")
        audience = input("Enter the target audience for the event: ")
        date_time = input("Enter the date and time of the event (YYYY-MM-DD HH:MM:SS): ")
        capacity = int(input("Enter the capacity of the event: "))
        register_event(event_title, description, audience, date_time, capacity)
    elif choice == '7':
        name = input("Enter your name: ")
        role = input("Enter your role as a volunteer: ")
        volunteer(name, role)
    elif choice == '8':
        name = input("Enter your name: ")
        contact = input("Enter your contact information: ")
        question = input("Enter your question or request: ")
        add_help_request(name, contact, question)
    elif choice == '9':
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid number (1-8).")
