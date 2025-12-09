import unittest
from contact import Contact
from contact_book_hash import ContactBookHash
from merge_sort import merge_sort


class TestContacts(unittest.TestCase):

    def test_add_search(self):
        book = ContactBookHash()
        c = Contact("Alice", "111")
        book.add_contact(c)

        found = book.search_contact("Alice")
        self.assertIsNotNone(found)
        self.assertEqual(found.phone, "111")

    def test_delete(self):
        book = ContactBookHash()
        book.add_contact(Contact("Bob", "222"))

        deleted = book.delete_contact("Bob")
        self.assertTrue(deleted)

        result = book.search_contact("Bob")
        self.assertIsNone(result)

    def test_merge_sort(self):
        c1 = Contact("Charlie", "333")
        c2 = Contact("Alice", "111")
        c3 = Contact("Bob", "222")

        sorted_list = merge_sort([c1, c2, c3])
        names = [c.name for c in sorted_list]

        self.assertEqual(names, ["Alice", "Bob", "Charlie"])

    def test_large_dataset(self):
        book = ContactBookHash()

        for i in range(500):
            book.add_contact(Contact(f"Person{i}", str(i)))

        self.assertEqual(len(book.get_all()), 500)


if __name__ == "__main__":
    unittest.main()
