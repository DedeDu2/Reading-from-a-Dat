import sqlite3

def count_books_from_database():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM books')
    total_books = cursor.fetchone()[0]
    conn.close()
    return total_books

# Example usage:
total_books = count_books_from_database()
print("Total books from database:", total_books)
