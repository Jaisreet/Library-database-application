# Library Management System

This Python-based Library Management System (LMS) is designed to facilitate the efficient management of library resources, events, and personnel. The system uses an SQLite database to store and retrieve information, providing a user-friendly interface for library staff and patrons. Here's an overview of the functions and features available in this LMS:

### Functions

1. **Find an Item**
   - Function: `find_item(title)`
   - Description: Search for library items by title.
   - Usage: Enter the title of the item you're looking for, and the system will display its details if found.

2. **Borrow an Item**
   - Function: `borrow_item(title, user_id, borrow_date, due_date)`
   - Description: Borrow a library item, specifying the user ID, borrow date, and due date.
   - Usage: Enter the item title, user ID, borrow date (in YYYY-MM-DD format), and due date (in YYYY-MM-DD format) to borrow the item.

3. **Return an Item**
   - Function: `return_item(title, user_id, return_date)`
   - Description: Return a borrowed library item, calculating fines if applicable.
   - Usage: Enter the item title, user ID, and return date (in YYYY-MM-DD format) to return the item.

4. **Donate an Item**
   - Function: `donate_item(title, item_type, author_artist, genre, available_copies)`
   - Description: Contribute a new item to the library's collection.
   - Usage: Provide details such as title, item type, author or artist, genre, and the number of available copies to donate an item.

5. **Find an Event**
   - Function: `find_event(event_name)`
   - Description: Search for library events by event name.
   - Usage: Enter the event name to find information about the event.

6. **Register for an Event**
   - Function: `register_event(title, description, audience, event_date, room_id)`
   - Description: Register for a library event by specifying event details.
   - Usage: Enter the event title, description, target audience, event date and time (in YYYY-MM-DD HH:MM:SS format), and room ID to register for the event.

7. **Volunteer**
   - Function: `volunteer(name, job_title)`
   - Description: Sign up as a volunteer to assist the library.
   - Usage: Enter your name and desired job title to volunteer.

8. **Ask Librarian**
   - Function: `add_help_request(name, contact, question)`
   - Description: Submit a help request to contact a librarian for assistance.
   - Usage: Provide your name, contact information, and your question or request.

### How to Use

1. Clone or download the project repository.

2. Ensure you have Python and SQLite installed on your system.

3. Run the `library.py` script to start the Library Management System.

4. Follow the on-screen instructions to perform various library tasks.

5. Enjoy the convenience of managing library resources and events seamlessly.
