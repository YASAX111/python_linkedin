# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setDiscount(self, amount):
        self._discount = amount

# TODO: create some book instances
b1 = Book("War and Peace", "Leo", 1225, 39.95)

# TODO: print the price of book1
print("The price of",  b1.title, "is")
print(b1.getPrice())

# TODO: try setting the discount
print(b1.getPrice())
b1.setDiscount(0.25)
print(b1.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
