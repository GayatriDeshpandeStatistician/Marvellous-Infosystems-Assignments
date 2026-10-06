class BookStore:
    NoOfBooks = 0

    def __init__(self, Name ,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print("Name of the Book is", self.Name)
        print("Name of Author is",self.Author)
        print("Number of books are",BookStore.NoOfBooks)

def main():
    obj1 = BookStore("Linux System Programming","Robrt Love")
    obj1.Display()

    obj2 = BookStore("C programming","Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()