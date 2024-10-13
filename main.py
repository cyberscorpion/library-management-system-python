from crud import add_book, get_book, add_member, get_member, issue_book, return_book, get_transactions_by_member, delete_book

def addNewBook():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    count = int(input("Enter number of copies: "))
    add_book(title, author, isbn, count)
    print("> New Book added")

def deleteABook():
    book_id = int(input("Enter Book Id to delete: "))
    delete_book(book_id)

def printBooks():
    books = get_book()
    for book in books:
        # available = ""
        # if book.count > 0:
        #     availabel = "Available"
        # else:
        #     available = "Not Available"
        available = "Available" if book.count > 0 else "Not Available"
        print(f"{book.id}: '{book.title}' by {book.author} (ISBN: {book.isbn}) - {available} ({book.count} copies)")

def addNewMember():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    add_member(name, email)
    print("> New member added")

def printMembers():
    members = get_member()
    for member in members:
        print(f"{member.id}: {member.name} (Email: {member.email})")

def issueABook():
    book_id = int(input("Enter book ID: "))
    member_id = int(input("Enter member ID: "))
    issue_book(book_id, member_id)

def returnABook():
    transaction_id = int(input("Enter a transaction ID: "))
    return_book(transaction_id)

def getTransactionForMember():
    member_id = int(input("Enter member ID: "))
    transactions = get_transactions_by_member(member_id)
    for transaction in transactions:
        return_state = "Returns" if transaction.return_date else "Not Returned"
        print(f"Transaction ID: {transaction.id}, Book ID: {transaction.book_id}, Issue Date: {transaction.issue_date}, Return Date: {transaction.return_date}, Status: {return_state}")
    

def main():
    while True:
        print("***************************************")
        print("1. Add Book")
        print("2. View Books")
        print("3. Add Member")
        print("4. View Member")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. View Transactions by Member")
        print("8. Delete book in stock")
        print("9. Exit")
        print("***************************************")
        choice = input("Enter your choice: ")

        if choice == "1":
            addNewBook()
        elif choice == "2":
            printBooks()
        elif choice == "3":
            addNewMember()
        elif choice == "4":
            printMembers()
        elif choice == "5":
            issueABook()
        elif choice == "6":
            returnABook()
        elif choice == "7":
            getTransactionForMember()
        elif choice == "8":
            deleteABook()
        else:
            print("> Exited")
            break
        
if __name__ == "__main__":
    main()