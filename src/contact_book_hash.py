from contact import Contact

class ContactBookHash:

def __init__(self, size=20):
        self.size = size
        self.contacts = [[] for _ in range(size)]

def _get_index(self, key):
        total = 0
        for char in key.lower():
            total += ord(char)
        return total % self.size
