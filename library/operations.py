from library.data import books, issued_records
from library.utils import get_date_input, days_between
from library.fine import calculate_fine


def get_book_choice(prompt):
    titles = list(books.keys())
    print("\n--- Book List ---")
    for i, title in enumerate(titles, 1):
        info = books[title]
        status = "Available" if info["available"] else f"Issued to {info['issued_to']}"
        print(f"  {i}. {title} by {info['author']} — {status}")
    print()

    try:
        choice = int(input(prompt).strip())
        if 1 <= choice <= len(titles):
            return titles[choice - 1]
        else:
            print("Number out of range.")
            return None
    except ValueError:
        print("Enter a valid number.")
        return None


def show_books():
    print("\n--- Book List ---")
    titles = list(books.keys())
    for i, title in enumerate(titles, 1):
        info = books[title]
        status = "Available" if info["available"] else f"Issued to {info['issued_to']}"
        print(f"  {i}. {title} by {info['author']} — {status}")
    print()


def add_book():
    print("\n--- Add Book ---")
    title = input("Book title: ").strip()
    if not title:
        print("Title can't be empty.")
        return

    if title in books:
        print("This book already exists in the library.")
        return

    author = input("Author name: ").strip()
    if not author:
        print("Author name can't be empty.")
        return

    books[title] = {"author": author, "available": True, "issued_to": None}
    print(f"\n'{title}' by {author} added successfully.")


def issue_book():
    print("\n--- Issue Book ---")
    title = get_book_choice("Enter book number to issue: ")
    if not title:
        return

    if not books[title]["available"]:
        print(f"Sorry, this book is already issued to {books[title]['issued_to']}.")
        return

    student = input("Student name: ").strip()
    if not student:
        print("Student name can't be empty.")
        return

    issue_date = get_date_input("Issue date (DD-MM-YYYY): ")

    try:
        allowed_days = int(input("Allowed days: ").strip())
        if allowed_days <= 0:
            raise ValueError
    except ValueError:
        print("Enter a valid number of days.")
        return

    books[title]["available"] = False
    books[title]["issued_to"] = student

    issued_records[title] = {
        "student": student,
        "issue_date": issue_date,
        "allowed_days": allowed_days,
    }

    print(f"\nBook issued to {student}. Must return within {allowed_days} days.")


def return_book():
    print("\n--- Return Book ---")

    issued_titles = [t for t in books if not books[t]["available"]]
    if not issued_titles:
        print("No books are currently issued.")
        return

    print("\nCurrently issued books:")
    for i, title in enumerate(issued_titles, 1):
        print(f"  {i}. {title} — issued to {books[title]['issued_to']}")
    print()

    try:
        choice = int(input("Enter book number to return: ").strip())
        if not (1 <= choice <= len(issued_titles)):
            print("Number out of range.")
            return
        title = issued_titles[choice - 1]
    except ValueError:
        print("Enter a valid number.")
        return

    record = issued_records.get(title)
    if not record:
        print("No issue record found for this book.")
        return

    return_date = get_date_input("Return date (DD-MM-YYYY): ")

    issue_date = record["issue_date"]
    allowed_days = record["allowed_days"]
    total_days = days_between(issue_date, return_date)
    delay = total_days - allowed_days

    books[title]["available"] = True
    books[title]["issued_to"] = None
    del issued_records[title]

    print(f"\nBook returned by {record['student']}.")
    print(f"Days used: {total_days}, Allowed: {allowed_days}")

    if delay > 0:
        fine = calculate_fine(delay)
        print(f"Delay: {delay} days — Fine: Rs. {fine}")
    else:
        print("Returned on time. No fine.")
