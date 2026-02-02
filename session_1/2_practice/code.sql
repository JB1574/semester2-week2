-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here
-- 1. **List all loans**  
--Show book title, member name, and loan date.
--SELECT Books.title, members.name, Loans.loan_date  FROM Books 
--JOIN Loans ON Books.id = Loans.book_id
--JOIN Members ON Loans.member_id = Members.id;

-- 2. **Books and loans**  
--List all books and any loans associated with them.

--SELECT Books.title, COUNT(*) AS loans FROM Books
--LEFT JOIN Loans ON Books.id = Loans.book_id
--GROUP BY Loans.loan_date;

--3. **Branches and books**  
--List all library branches and the books they hold.

SELECT LibraryBranch.name, COUNT(Books.id) AS Books FROM Books
JOIN LibraryBranch ON Books.branch_id = LibraryBranch.id
GROUP BY Books.title;
