
class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def display(self):
        pass

b1 = Book('Of Mice and Men', 'written by John Steinbeck')
b2 = Book('To Kill a Mockingbird', 'written by Harper Lee')

print(b1.author,b1.title)
print(b2.author,b2.title)

if __name__ == "__main__":
    pass
