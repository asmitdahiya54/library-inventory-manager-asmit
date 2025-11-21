📚 Library Inventory Manager

A fully object-oriented, menu-driven Library Management System built in Python.
This project manages books using classes, JSON file storage, exception handling, and logging.
It follows a modular package structure and includes optional unit tests.

🔍 Project Overview

This application helps manage a library’s book records through a simple command-line interface.
It supports adding books, issuing/returning them, searching, and storing all data persistently in JSON format.

The objective is to demonstrate:

Object-Oriented Programming

File handling and JSON persistence

Robust exception management

Logging

Modular project structure

Creating a Python package + CLI interface

🎯 Features
✔ Object-Oriented Design

Book class with encapsulated attributes & methods

LibraryInventory class to manage book records

✔ JSON File Storage

Automatic loading & saving of catalog

Handles missing/corrupt files gracefully

✔ Menu-Driven Command-Line Interface

Add book

Issue/return book

Search by title or ISBN

Display full catalog

✔ Robust Programming

Exception handling for input, file I/O, and operations

Logging with INFO + ERROR levels

✔ Clean Modular Structure

Separate folders for library package, CLI, data, tests

Project Structure:

library-inventory-manager/
│
├── library_manager/
│   ├── __init__.py
│   ├── book.py
│   ├── inventory.py
│
├── cli/
│   ├── main.py
│
├── data/
│   ├── books.json
|
|──tests
│   ├──test_app.py
|
│
├── README.md
├── requirements.txt
└── .gitignore

🚀 How to Run the Project
1️⃣ Step 1: Open Terminal / CMD

Navigate to your project directory:

cd library-inventory-manager

2️⃣ Step 2: Run the CLI Program

Use either:

python cli/main.py


or recommended:

python -m cli.main

3️⃣ Step 3: Use the Menu

You will see:

=== Library Inventory Manager ===
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search Book
6. Exit

🧩 Code Summary
📘 Book Class

Handles:

issue

return

availability check

converting to dictionary

📚 LibraryInventory Class

Handles:

adding books

saving/loading JSON

searching

listing catalog


## 🖼 Output Screenshots

### 📁 1. Project Folder Structure
![Folder Structure](images/folder.png)

### 📝 2. Program Menu
![Program Menu](images/menu.png)

### ➕ 3. Adding a Book
![Add Book](images/addbook.png)

### 📚 4. Viewing All Books
![View Books](images/view.png)

### 🧪 5. Unit Test Output (optional)
![Unit Tests](images/tests.png)