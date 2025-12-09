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

def add_contact(self, contact):
        index = self._get_index(contact.name)
        bucket = self.contacts[index]

        for i in range(len(bucket)):
            if bucket[i].name.lower() == contact.name.lower():
                bucket[i] = contact
                return

        bucket.append(contact)

def search_contact(self, name):
        index = self._get_index(name)
        bucket = self.contacts[index]

        for contact in bucket:
            if contact.name.lower() == name.lower():
                return contact

        return None

def delete_contact(self, name):
        index = self._get_index(name)
        bucket = self.contacts[index]

        for i, contact in enumerate(bucket):
            if contact.name.lower() == name.lower():
                del bucket[i]
                return True
        return False


    def get_all(self):
        all_contacts = []
        for bucket in self.contacts:
            for contact in bucket:
                all_contacts.append(contact)
        return all_contacts

