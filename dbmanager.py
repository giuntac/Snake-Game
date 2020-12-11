"""
This module handles access to the database.
It allows to open or create a database and add new users.

Functions:
- open_and_create: connects to the database
- save_new_username: adds new username and score

"""
import sqlite3

conn = None
cursor = None


def open_and_create():
    """Connects to the database and creates user table.

    In case it doesn't exist yet, the database is created.
    """
    global conn
    global cursor
    conn = sqlite3.connect('scoreboard.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user")
    except sqlite3.OperationalError:
        # create table (if necessary)
        cursor.execute('''CREATE TABLE user
                     (username TEXT, score INTEGER,
                      PRIMARY KEY (username))''')


def save_new_username(username, score):
    """Save a new username with his/her score in the user table.

    ----------
    Parameters
    ----------
    username : the username typed by the player (type: str)
    score : the player's final score after game over (type: int)
    """
    global conn
    global cursor
    # adding username and value scored
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?)",
                   (username, score))
    conn.commit()
