class Contact:
    def __init__(self, name, phone, email=None, address=None, company=None, birthday=None):
         self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.company = company
        self.birthday = birthday

def __str__(self):
        return (
            f"{self.name} | Phone: {self.phone} | Email: {self.email or 'N/A'} | "
            f"Address: {self.address or 'N/A'} | Company: {self.company or 'N/A'} | "
            f"Birthday: {self.birthday or 'N/A'}"
        )

