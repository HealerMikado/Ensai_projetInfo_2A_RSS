class Book:

    def __init__(self, name, author, id=0):
        self.id = id
        self.name = name
        self.author = author

    def __str__(self):
        return '%s : "%s" écrit par %s' % (self.id, self.name, self.author)

    def __repr__(self):
        return '(id=%s, name=%s, author= %s)' % (self.id, self.name, self.author)
