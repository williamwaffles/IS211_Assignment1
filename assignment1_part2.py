
class Book:
    def __init__(self, author, title):
        pass
    
    def display(self):
        print(Book)


b1 = Book('Of Mice and Men', 'written by John Steinbeck')
b2 = Book('To Kill a Mockingbird', 'written by Harper Lee')

print(b1.display())
b2.display()

if __name__ == "__main__":
    pass
