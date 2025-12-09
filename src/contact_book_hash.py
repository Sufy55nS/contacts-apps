from contact import Contact

class ContactBookHash:

def __init__(self, size=20):
        self.size = size
        self.contacts = [[] for _ in range(size)]
