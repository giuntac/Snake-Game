'''
This module handles access to the database,
plus additonal functions to use it.
It allows to check for a user and his/her score,
look up the maximum score, or retrieve the whole list of
players with their scores in descending order.

Functions:
- check_score: looks for a username
- max_score: retrieves max score
- print_all_users: prints player list

'''
import sqlite3
import argparse
from colorama import Fore
from colorama import Style

conn = sqlite3.connect('scoreboard.db')
cursor = conn.cursor()

def parse_args_optional():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', help="check for a username and return the score", 
                        required=False) #optional
    parser.add_argument('-m', help="return max score", action='store_true',
                        required=False) #optional 
    parser.add_argument('-l', help="list all users and scores", action='store_true', #TODO: Work on selecting choices 
                        required=False) #optional 
    return parser.parse_args()

def check_score(username):
    """Checks for a specified username in the database to view his/her score.
    
    ----------
    Parameters
    ----------
    username : choose the verbosity level (type: srt)
    """
    global conn
    global cursor

    rows = cursor.execute("SELECT * FROM user WHERE username=?",
                          (username,)) # we need this for iteration on the rows
   
    conn.commit()
    results = rows.fetchall()
    # NOTE: this could be done more efficiently with a JOIN -- HOW?
    if results:
        b = cursor.execute("SELECT score FROM user WHERE username=?",
                           (results[0][0],))
        print(f"User {username} is present, their score is: %s" #Giulio semmai lo coloriamo come tutti gli altri testi
              % b.fetchall()[0][0])
    else:
        print(f"Oh no! Seems like {username} hasn't played yet.")

def max_score(): # view max score
    """Looks for the maximum score in the database.
    """
    global conn
    global cursor
    
    max_score = cursor.execute("SELECT username, MAX(score) FROM user") 
    conn.commit()
    results = max_score.fetchall()
    #print(results)
    print("The user with the highest score is", results[0][0], "with", results[0][1], "points.")

def print_all_users(): # Now works showing them in descending order!
    """Prints all users with respective scores present in the database
    """
    global conn
    global cursor
    rows = cursor.execute("SELECT username, score FROM user ORDER BY score DESC")
    conn.commit()
    results = rows.fetchall()
    # print(results)

    print("Here is the leaderboard:")
    for row in results:
        print(row[0], row[1]) # TO DO: Magari si può rendere più carina la scrittura

args = parse_args_optional()

if args.c: 
    check_score(args.c)
elif args.m:
    max_score()
elif args.l:
    print_all_users()

conn.close()