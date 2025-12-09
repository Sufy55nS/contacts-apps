from contact import Contact
from contact_book_hash import ContactBookHash
from merge_sort import merge_sort


def main():
    book = ContactBookHash()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Show All Contacts (Sorted)")
        print("5. Exit")

        choice = input("Enter choice: ")

  def main():
    book = ContactBookHash()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Show All Contacts (Sorted)")
        print("5. Exit")

        choice = input("Enter choice: ")

elif choice == "2":
            name = input("Enter name to search: ")
            result = book.search_contact(name)

            if result:
                print("\nFOUND:")
                print(result)
            else:
                print("Contact not found.")

  elif choice == "3":
            name = input("Enter name to delete: ")
            ok = book.delete_contact(name)

            if ok:
                print("Deleted.")
            else:
                print("Contact not found.")
