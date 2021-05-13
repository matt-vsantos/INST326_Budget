import sqlite3
import tkinter as tk

def init_database():
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    cq = "CREATE TABLE IF NOT EXISTS categories (categoryid INTEGER PRIMARY KEY, category_name TEXT, max_amount INTEGER);"
    cursor.execute(cq)
    conn.close() 
        
def get_categories():
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    sq = '''SELECT category_name FROM categories'''
    sq_names = cursor.execute(sq).fetchall()
    conn.close()

    # following line and loop gets categories from the database and puts them in a list
    category_names = list()
    for tup in sq_names:
        category_names.append(tup[0])

    return category_names

def add_category(name, max_amount):
    """Verifies that the category has been added to user. Adds category to a database and creates table for that category
        Parameters:
            name (String): name of the category
            max_amount (int): max_amount the user can spend in that category
    """
    if name not in get_categories():
        conn = sqlite3.connect('budget_tracker.db')
        cursor = conn.cursor()
        db_tuple = name, max_amount
        
        iq = '''INSERT INTO categories(category_name, max_amount) VALUES (?,?)'''
        cursor.execute(iq, db_tuple)
        conn.commit()
        cq = '''CREATE TABLE IF NOT EXISTS %s (expenseid INTEGER PRIMARY KEY, expense_name TEXT, expense_amount INTEGER);''' %name
        cursor.execute(cq)
        conn.commit()
        conn.close()

def del_category(name):
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    dq = '''DROP TABLE %s;''' %name
    conn.commit()
    drq = '''DELETE FROM categories WHERE category_name = "%s"''' %name
    cursor.execute(dq)
    cursor.execute(drq)
    conn.commit()
    conn.close()
