import sqlite3



def connect():
    con = sqlite3.connect("books_database.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    con.commit()
    con.close()


def insert(title, author, year, isbn):
    con = sqlite3.connect("books_database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO books VALUES(NULL, ?, ?, ?,?)",
                (title, author, year, isbn))
    con.commit()
    con.close()


def view():
    con = sqlite3.connect("books_database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    con.close()
    return rows


def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect("books_database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books WHERE title=? or author=? or year=? or isbn=?",
                (title, author, year, isbn))
    rows = cur.fetchall()
    con.close()
    return rows


def delete(id):
    con = sqlite3.connect("books_database.db")
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    con.commit()
    con.close()


def update(id, title, author, year, isbn):
    con = sqlite3.connect("books_database.db")
    cur = con.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",
                (title, author, year, isbn, id))
    con.commit()
    con.close()


connect()
# insert("The sea", "John Dee", 1921, 985467589)
# update(5, "The moon", "John Dee", 1921, 985467589)
# delete(4)
print(view())
# print(search(author = 'John Dee'))
