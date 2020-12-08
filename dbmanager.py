import sqlite3

conn = None
cursor = None

def open_and_create():
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
    global conn  
    global cursor
    # adding username and value scored
    cursor.execute("INSERT OR REPLACE INTO user VALUES (?,?)",
                   (username, score))
    conn.commit()
