class Library:
    def __init__(self, list_of_books):
        self.available_books = list_of_books

    def display_available_books(self):
        print("\n--- Available Books ---")
        for book in self.available_books:
            print(f"- {book}")
        print("-----------------------")

    def lend_book(self, requested_book):
        if requested_book in self.available_books:
            print(f"You have successfully borrowed '{requested_book}'.")
            self.available_books.remove(requested_book)
        else:
            print(f"Sorry, '{requested_book}' is not available right now.")

    def add_book(self, returned_book):
        self.available_books.append(returned_book)
        print(f"Thank you for returning/adding '{returned_book}'.")

if __name__ == "__main__":
    college_library = Library(["Python Crash Course", "Clean Code", "The Pragmatic Programmer"])
    
    while True:
        print("\n=== Library Management System ===")
        print("1. Display available books")
        print("2. Borrow a book")
        print("3. Return/Add a book")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            college_library.display_available_books()
        elif choice == '2':
            book = input("Enter the name of the book you want to borrow: ")
            college_library.lend_book(book)
        elif choice == '3':
            book = input("Enter the name of the book you want to return/add: ")
            college_library.add_book(book)
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")