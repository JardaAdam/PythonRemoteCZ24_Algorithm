"""Exercise 1: Stack

Write code simulating a Stack of books. The class should allow you to add and remove books from the Stack, browse titles in Stack and show the last position on the Stack. Use magic methods to allow for:

    adding Stacks together
    comparing Stack sizes
    Stack string representation
    stating Stack length
"""

from typing import List


class BooksStack:

    def __init__(self, stack_name, category):
        self.stack_name = stack_name
        self.category = category
        self.books_stack = []

    def add_new_book(self, title: str):
        self.books_stack.append(title)

    def get_book(self):
        return self.books_stack.pop()

    def all_books(self) -> List[str]:
        return self.books_stack

    def __add__(self, second_stack):
        new_stack = BooksStack(self.stack_name, self.category)
        new_stack.books_stack = self.books_stack + second_stack.books_stack
        return new_stack

    # comparison
    def __gt__(self, second_stack):
        return len(self) > second_stack

    def __lt__(self, second_stack):
        return len(self) < second_stack

    def __ge__(self, second_stack):
        return len(self) >= second_stack

    def __le__(self, second_stack):
        return len(self) <= second_stack

    def __str__(self):
        return f"Stack: {self.stack_name} with category of books: {self.category}"

    def __repr__(self):
        result = f"stack_name: {self.stack_name}\n"
        result += f"category: {self.category}\n"
        result += f"books: {self.books_stack}"
        return result

    def __len__(self):
        return len(self.books_stack)


if __name__ == '__main__':
    my_books = BooksStack("My Stack of Books", "Natural")

    my_books.add_new_book("Cheetahs")
    my_books.add_new_book("Elephants")
    my_books.add_new_book("Cats")

    print(my_books.all_books())
    print(my_books.get_book())
    print(my_books.all_books())

    her_books = BooksStack("Her Stack of Books", "Natural")
    her_books.add_new_book("Horses")

    my_books = my_books + her_books
    print(my_books.all_books())

    print(my_books > her_books)
    print(my_books <= her_books)

    print(my_books)
    print(repr(my_books))

    print(len(my_books))
