class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books Present In This Library Are:  ")
        for book in  self.books:
            print ("\t *" +book)

    def borroeBOOK(self, bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}. Kindly keep it safe & return it within one month")
            self.books.remove(bookName)
            return True
        else:
            print("soory, this book has been issued to someone else")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("thanks for returning this book!")

class Student:
    def __init__(self):
        self.bookList = []

    def requestBook(self):
        reqBook = input("Enter the name of the book")
        self.bookList.remove(reqBook)

    def returnBook (self):
        returnBook = input("enter the book name that you want to return")
        self.bookList.append(returnBook)

if __name__ == "__main__":
    centralLibrary = Library(["manat", "Deh zala chandanacha", "amrutvel", "kota Factory", "yayati", "mrutunjay","rajram mohan roy","chava","shreeman yogi","Panipaat","swami"])
    centralLibrary.displayAvailableBooks() 