# Display book
# Add Book
# Remove book
# Issue Book
# Return Book
# Display issued book list

import time

class LibraryManagementSystem:

    def __init__(self, libName, *books):
        self.libName = libName
        self.listBooks = list(books)
        self.issueBooks = {}
        print(f"Welcome to {self.libName}")   

    def display(self):
        print("Book available in library: ")
        for book in self.listBooks:
            print(book)

    def addBook(self):
        bName = input("Enter book name to add: ").upper()
        for book in self.listBooks:
            if book == bName:
                print("This book is already available in library!")
                return
            else:
                if self.issueBooks.get(bName)is not None:
                    print(f"Cannot add {bName} book as it is already available in library but issued to some else..")
                    return    
        self.listBooks.append(bName)
        print(f"{bName} book added!")     

    def removeBook(self):
        rBook = input("Enter book name to remove: ").upper()   
        if self.issueBooks.get(rBook) is not None:
            print(f"Cannot remove {rBook} now as it is already issued to someone else.")
            return

        if rBook in self.listBooks:
            self.listBooks.remove(rBook)
            print(f"{rBook} book removed!")
        else:
            print(f"This book is not available in our library.")    
                

    def issueBook(self):
        iBook = input("Enter book name to issue: ").upper()
        if iBook in self.listBooks:
            personName = input("Enter name of person: ").upper()
            self.issueBooks[iBook] = personName 
            self.listBooks.remove(iBook)
            print(f"{iBook} book is issued successfully at {time.ctime()}.")
        else:
            val = self.issueBooks.get(iBook)
            if val is None:
                print(f"{iBook} book is not available in our library!")    
            else:
                print(f"{iBook} book is already issued by our member {val}!")

    def returnBook(self):
        retBook = input("Enter name of the book to return: ").upper()
        if self.issueBooks.get(retBook) is not None:
            self.listBooks.append(retBook)
            self.issueBooks.pop(retBook)
            print(f"{retBook} is returned at {time.ctime()}.")
        else:
            print(f"Sorry, no book is issued to someone with the name {retBook}.")                    

    def issuedList(self):
        print("Issued books with members name list: ")
        print(self.issueBooks)        

if __name__ == '__main__':
    # This will initialize the program with few books in the library.
    myLib = LibraryManagementSystem("Library Store", "THE HEIST", "13 REASONS WHY", "EVERYTHING EVERYTHING")         
    
    while True:
        try:
            print("\nPress 1: Display Books\nPress 2: Add Book\nPress 3: Remove Book\nPress 4: issueBook\nPress 5: Return Book\nPress 6: List of Issued Books\nPress 0: Exit")
            choice = int(input("Enter key: "))
            if choice == 1:
                myLib.display()
            elif choice == 2:
                myLib.addBook()
            elif choice == 3:
                myLib.removeBook()
            elif choice == 4:
                myLib.issueBook()
            elif choice == 5:
                myLib.returnBook()
            elif choice == 6:
                myLib.issuedList()    
            elif choice == 0:
                print("Exiting from Library system...")
                break    
            else:
                print("Invalid choice!")
                continue   
        except:
            print("Enter only numbers that are instructed.")

