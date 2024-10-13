from crud import add_book

def main():
    print("***************************************")
    print("1. Add Book")
    print("2. View Book")
    print("***************************************")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        count = int(input("Enter number of copies: "))
        add_book(title, author, isbn, count)

    elif choice == "2":
        print("Write code to view books")


if __name__ == "__main__":
    main()