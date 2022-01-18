class Book:
    def __init__(self, title, author, pages,checkoutBook=None, rating=None, checkinBook=None):
        self.title = title
        self.checkinBook = checkinBook
        self.checkoutBook = checkoutBook
        self.pages = pages
        self.author = author
        
    def to_dict(self):
        if hasattr(self, '__dict__'):
            self = self.__dict__
        return self