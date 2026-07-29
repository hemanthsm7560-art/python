class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        print("-" * 40)
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", "Issued" if self.issued else "Available")


books = []


def add_book():
    try:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        if not title or not author:
            print("Title and author cannot be empty.")
            return

        book = Book(book_id, title, author)
        books.append(book)
        print("Book Added successfully!")
    except ValueError:
        print("Invalid Input!")


def view_books():
    if not books:
        print("No books available.")
        return

    for book in books:
        book.display()


def search_book():
    try:
        book_id = int(input("Enter your Book ID: "))
    except ValueError:
        print("Invalid Input!")
        return

    for book in books:
        if book.book_id == book_id:
            book.display()
            return
    print("Book not found.")


def issue_book():
    try:
        book_id = int(input("Enter your Book ID: "))
    except ValueError:
        print("Invalid Input!")
        return

    for book in books:
        if book.book_id == book_id:
            if book.issued:
                print("Book Already Issued")
            else:
                book.issued = True
                print("Book issued successfully!")
            return
    print("Book not found.")


def return_book():
    try:
        book_id = int(input("Enter your Book ID: "))
    except ValueError:
        print("Invalid Input!")
        return

    for book in books:
        if book.book_id == book_id:
            if book.issued:
                book.issued = False
                print("Book returned successfully!")
            else:
                print("Book was not issued.")
            return
    print("Book not found.")


def delete_book():
    try:
        book_id = int(input("Enter your Book ID: "))
    except ValueError:
        print("Invalid Input!")
        return

    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            print("Book deleted successfully!")
            return

    print("Book not found.")


while True:
    print("\n ========= LIBRARY MANAGEMENT SYSTEM =========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
