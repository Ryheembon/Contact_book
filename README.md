# 📇 Contact Book – Python + SQLite

This is a simple command-line Contact Book built with Python and SQLite.  
It lets you **add**, **view**, **search**, and **delete** contacts.

---

## 🛠 Features

- ✅ Create a local database (`contacts.db`)
- ✅ Add new contacts (name, phone, optional email)
- ✅ View all saved contacts
- ✅ Search contacts by name
- ✅ Delete contacts by ID
- ✅ Simple command-line menu

---

## 🧠 How It Works

### 1. **Database Setup**
- Uses the `sqlite3` module to create a local database.
- A table named `contacts` is created with the following fields:
  - `id`: Auto-incremented primary key
  - `name`: Required
  - `phone`: Required
  - `email`: Optional

### 2. **Add a Contact**
Prompts the user for:
- Name
- Phone number
- (Optional) Email address  
Then saves this data into the database.

### 3. **View All Contacts**
Displays a clean list of all stored contacts with their:
- ID
- Name
- Phone
- Email

### 4. **Search Contacts**
- Asks the user for a name (or part of one)
- Displays all matching results

### 5. **Delete a Contact**
- First shows all contacts so the user can choose who to delete
- Then asks for the contact ID and deletes the record if it exists

---

## 📋 Menu

The script shows a looped menu with these options:

```text
=== CONTACT BOOK MENU ===
1. Add a new contact
2. View all contacts
3. Search contacts
4. Delete a contact
5. Exit
========================
Enter your choice (1-5):
