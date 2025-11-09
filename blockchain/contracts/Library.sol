// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract LibrarySystem {
struct Book {
string title;
bool isAvailable;
}
Book[] private books;
/// @notice Add a new book to the library.
/// @param _title The title of the book.
function addBook(string memory _title) public {
books.push(Book(_title, true));
}
/// @notice Borrow a book by its index.
/// @param _index Index of the book to borrow.
function borrowBook(uint256 _index) public {
require(_index < books.length, "Invalid book index");
require(books[_index].isAvailable, "Book not available");
books[_index].isAvailable = false;
}
/// @notice Return a borrowed book.
/// @param _index Index of the book to return.
function returnBook(uint256 _index) public {
require(_index < books.length, "Invalid book index");
require(!books[_index].isAvailable, "Book is already available");
books[_index].isAvailable = true;
}
/// @notice Get all books in the library.
/// @return Array of all books with title and availability.
function getBooks() public view returns (Book[] memory) {
return books;
}
/// @notice Get total number of books in the library.
function getBookCount() public view returns (uint256) {
return books.length;
}
}