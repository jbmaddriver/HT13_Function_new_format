import unittest


def formatted_name(first_name, last_name, middle_name=""):
    if len(middle_name) > 0:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.strip().title()


class TestName(unittest.TestCase):
    def setUp(self):
        """Setting up for test"""
        pass

    def tearDown(self):
        """Tearing down function not required for this test case"""
        pass

    #   Positive test cases "Not Equal"
    def test_edge_cases(self):
        self.assertEqual(formatted_name("", "", ""), "")
        self.assertEqual(formatted_name("   ", "   ", "   "), "")

    def test_with_capitalization(self):
        self.assertEqual(formatted_name("jack", "spenser"), "Jack Spenser")
        self.assertEqual(formatted_name("Jack", "spenser"), "Jack Spenser")
        self.assertEqual(formatted_name("Jack", "Spenser"), "Jack Spenser")
        self.assertEqual(formatted_name("jack", "Spenser"), "Jack Spenser")

    def test_with_middle_name(self):
        self.assertEqual(formatted_name("Jack", "Spenser", "jr."), "Jack Jr. Spenser")
        self.assertEqual(formatted_name("Jack", "Spenser", "Jr."), "Jack Jr. Spenser")
        self.assertEqual(
            formatted_name("Jack", "Spenser", "Junior"), "Jack Junior Spenser"
        )

    def test_length_of_full_name(self):
        self.assertEqual(
            len(formatted_name("John", "Doe", "James")), len("John James Doe")
        )

    def test_with_empty_middle_name(self):
        self.assertEqual(formatted_name("John", "Doe", ""), "John Doe")

    #   Negative test cases "Not Equal"
    def test_whitespaces_name(self):
        self.assertNotEqual(formatted_name("  John ", "  Doe"), "John Doe")
        self.assertNotEqual(formatted_name("John", " ", ""), "John Doe")
        self.assertNotEqual(formatted_name(" ", "Doe", "Jr."), "John Jr. Doe")

    def test_whitespace_middle_name(self):
        self.assertNotEqual(formatted_name("John", "Doe", "     "), "John Doe")

    def test_unaccepted_symbols(self):
        self.assertNotEqual(formatted_name("John2", "@Doe|/", "#$"), "John Doe")


if __name__ == "__main__":
    unittest.main()
