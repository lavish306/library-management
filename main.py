from library.operations import show_books, issue_book, return_book, add_book

print("Welcome to the Library Management System")

while True:
    print("\n1. Show all books")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Add a book")
    print("5. Exit")

    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        show_books()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        add_book()
    elif choice == "5":
        print("Closing system. Bye.")
        break
    else:
        print("Invalid choice, try again.")
