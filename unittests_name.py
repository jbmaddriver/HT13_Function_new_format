import unittest


def formatted_name(first_name, last_name, middle_name=""):
    if len(middle_name) > 0:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


class TestName(unittest.TestCase):
    #   Positive test cases "Not Equal"
    def test_edge_cases_empty(self):
        self.assertEqual(formatted_name("", "", ""), " ")

    def test_edge_cases_whitespaces(self):
        self.assertEqual(formatted_name("   ", "   ", "   "), "           ")

    def test_with_capitalization(self):
        self.assertEqual(formatted_name("jack", "spenser"), "Jack Spenser")

    def test_length_of_full_name(self):
        self.assertEqual(
            len(formatted_name("John", "Doe", "James")), len("John James Doe")
        )

    #   Negative test cases "Not Equal"
    def test_whitespaces_name(self):
        self.assertEqual(formatted_name("  John ", "  Doe"), "  John    Doe")
        self.assertEqual(formatted_name("John", " ", ""), "John  ")
        self.assertEqual(formatted_name(" ", "Doe", "Jr."), "  Jr. Doe")

    def test_whitespace_middle_name(self):
        self.assertNotEqual(formatted_name("John", "Doe", "     "), "John Doe")

    def test_wrong_data_type(self):
        with self.assertRaises(TypeError):
            formatted_name((0, 1), "Doe")
        with self.assertRaises(TypeError):
            formatted_name(
                1,
                "Doe",
            )

    def test_wrong_data_type_none(self):
        with self.assertRaises(TypeError):
            formatted_name("John", None)


if __name__ == "__main__":
    unittest.main()
