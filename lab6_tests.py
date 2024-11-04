from data import Book
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_book(self):
        books = [Book(["F. Scott Fitzgerald"], "The Great Gatsby")]
        lab6.selection_sort_books(books)
        self.assertEqual(books, [Book(["F. Scott Fitzgerald"], "The Great Gatsby")])

    def test_books(self):
        books = [
            Book(["Zebra Author"], "Zebra"),
            Book(["Apple Author"], "Apple"),
            Book(["Mango Author"], "Mango")
        ]
        lab6.selection_sort_books(books)
        expected = [
            Book(["Apple Author"], "Apple"),
            Book(["Mango Author"], "Mango"),
            Book(["Zebra Author"], "Zebra")
        ]
        self.assertEqual(books, expected)

    # Part 2

    def test_swap_cases1(self):
        self.assertEqual(lab6.swap_case("Hello World!"), "hELLO wORLD!")

    def test_swap_cases2(self):
        self.assertEqual(lab6.swap_case("123 ABC xyz!"), "123 abc XYZ!")
    # Part 3
    def test_str_translate1(self):
        self.assertEqual(lab6.str_translate("Hi My Name is Jack Jarvis",'J','m'),"Hi My Name is mack marvis")

    def test_str_translate2(self):
        self.assertEqual(lab6.str_translate("Hello Everyone", 'o', '0'), "Hell0 Every0ne")
    # Part 4


    def test_histogram1(self):
        self.assertEqual(lab6.histogram("hello world "), {"hello": 1, "world": 1})


    def test_histogram2(self):
        self.assertEqual(
            lab6.histogram("Hi my name is Jack Jarvis, Jack Jarvis is my name"),
            {'Hi': 1, 'Jack': 2, 'Jarvis': 1, 'Jarvis,': 1, 'is': 2, 'my': 2, 'name': 2})



if __name__ == '__main__':
    unittest.main()
