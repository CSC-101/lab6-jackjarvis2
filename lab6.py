from data import Book
from typing import List, Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1

# Finds the index of the book with the smallest title from a starting index.
#
# Input:
# - books: a list of Book objects
# - start: an integer indicating the starting index
#
# Returns:
# - index of the book with the smallest title as an int, or None if out of bounds

def index_smallest_from_books(books: List[Book], start: int) -> Optional[int]:
    if start >= len(books) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[mindex].title:
            mindex = idx

    return mindex

# Sorts a list of books by their titles using selection sort.
#
# Input:
# - books: a list of Book objects
#
# Returns:
# - This function modifies the input list in place; no value is returned
#

def selection_sort_books(books: List[Book]) -> None:
    for idx in range(len(books) - 1):
        mindex = index_smallest_from_books(books, idx)
        books[mindex], books[idx] = books[idx], books[mindex]


# Part 2

# Swaps the case of each letter in a given string, leaving other characters unchanged.
#
# Input:
# - input_string: a string containing characters to process
#
# Returns:
# - A new string with each uppercase letter converted to lowercase and vice versa

def swap_case(input_string: str) -> str:
    result = ''
    for char in input_string:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char

    return result


# Part 3

# Replaces all occurrences of a specified character in a string with another character.
#
# Input:
# - input_string: the string to be modified
# - old_char: a character to be replaced
# - new_char: a character to replace old_char
#
# Returns:
# - A new string with the specified character replaced
#
# Example:
# str_translate("hello world", 'o', '0')  # returns "hell0 w0rld"
# str_translate("aaa", 'a', 'x')          # returns "xxx"
def str_translate(input_string: str, old_char: str, new_char: str) -> str:
    result = ''
    for char in input_string:
        if char == old_char:
            result += new_char
        else:
            result += char
    return result


# Part 4

# Counts the occurrences of each word in a given string.
#
# Input:
# - input_string: a string containing words separated by spaces
#
# Returns:
# - A dictionary where keys are words and values are their respective counts

def histogram(input_string: str) -> dict:
    word_count = {}
    words = input_string.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count
