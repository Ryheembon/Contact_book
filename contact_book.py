import sqlite3

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT
)
''')

conn.commit()
conn.close()

print("Database and table created successfully")
print("About to call add_contact function...")


def add_contact():
    name = input("Enter name:")
    phone = input("Enter phone: ")
    email = input("Enter email (optional): ")

    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    cursor.execute('''
                   INSERT INTO contacts (name, phone, email)
                   VALUES (?, ? , ?)
            ''', (name, phone, email))
    
    conn.commit()
    conn.close()

    print(f"Contact '{name}' added successfully!")

add_contact()


def view_all_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    # Get all contacts
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    conn.close()

    # Add this part to display the contacts
    if contacts:
        print("\nALL Contacts:")
        print("_" * 30)
        for contact in contacts:
            print(f"ID: {contact[0]}")
            print(f"Name: {contact[1]}")
            print(f"Phone: {contact[2]}")
            print(f"Email: {contact[3]}")
            print("_" * 30)
    else:
        print("\nNo contacts found.")

def search_contact():
    search_name = input("enter name to search: ")
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contacts WHERE name LIKE ?', (f'%{search_name}%',))
    contacts = cursor.fetchall()

    conn.close()

    if contacts:
        print("\nALL Contacts:")
        print("_" * 30)
        for contact in contacts:
            print(f"ID: {contact[0]}")
            print(f"Name: {contact[1]}")
            print(f"Phone: {contact[2]}")
            print(f"Email: {contact[3]}")
            print("_" * 30)
    else:
        print("\nNo contacts found.")

def delete_contact():
    # First show all contacts so user can see what to delete
    view_all_contacts()

    contact_id = input("Enter the ID of the contact to delete: ")

    try:
        conn = sqlite3.connect('contacts.db')
        cursor = conn.cursor()

        # First check if the contact exists
        cursor.execute('SELECT name FROM contacts WHERE id = ?', (contact_id,))
        contact = cursor.fetchone()

        if contact:
            # Delete the contact
            cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
            conn.commit()
            print(f"Contact '{contact[0]}' deleted successfully!")
        else:
            print(f"No contact found with ID {contact_id}")

        conn.close()

    except ValueError:
        print("Please enter a valid number for the ID.")

view_all_contacts()

def show_menu():
    print("\n=== CONTACT BOOK MENU ===")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search contacts")
    print("4. Delete a contact")
    print("5. Exit")
    print("========================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_all_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()
