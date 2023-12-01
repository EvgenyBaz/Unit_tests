import unittest
from unittest.mock import Mock
from book_service import BookService, Book, BookRepository

#
# class TestBookService(unittest.TestCase):
#     def setUp(self) -> None:
#         self.service = BookService(Mock())
#
#     def test_find_by_id(self):
#         book_id = 3
#         self.service.find_by_id(book_id)
#         self.service.book_repository.find_by_id.assert_called_with(book_id)
#
#     def test_find_all(self):
#         self.service.find_all()
#         self.service.book_repository.find_all.assert_called_once()

# import unittest
# from unittest.mock import Mock
# from book import BookService, Book, BookRepository
import unittest
from unittest.mock import Mock
from book_service import BookService


class BookServiceTest(unittest.TestCase):

    def setUp(self):
        self.bookRepository = Mock()
        self.bookService = BookService(self.bookRepository)

    def test_find_book_by_id(self):
        id = 1
        book = Book(id, "Book1", "Author1")
        self.bookRepository.find_by_id.return_value = book
        result = self.bookService.find_by_id(id)
        self.bookRepository.find_by_id.assert_called_once_with(id)
        self.assertEqual(book, result)

    def test_find_all_books(self):
        books = [
            Book(1, "Book1", "Author1"),
            Book(2, "Book2", "Author2")
        ]
        self.bookRepository.find_all.return_value = books
        result = self.bookService.find_all()
        self.bookRepository.find_all.assert_called_once()
        self.assertEqual(books, result)


if __name__ == '__main__':
    unittest.main()
