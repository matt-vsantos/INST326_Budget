import sqlite3
import tkinter as tk

def init_database():
    """Creates the database file and creates the empty 'categories'A table
    """
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    cq = "CREATE TABLE IF NOT EXISTS categories (categoryid INTEGER PRIMARY KEY NOT NULL, category_name TEXT NOT NULL, max_amount FLOAT NOT NULL);"
    cursor.execute(cq)
    conn.close() 
        
def get_categories():
    """This method returns a list of all of the categories by querying the database
    Returns:
        category_names (list): a list of strings of all the budget's categories
    """
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
        cq = '''CREATE TABLE IF NOT EXISTS %s (expenseid INTEGER PRIMARY KEY NOT NULL, expense_name TEXT NOT NULL, expense_amount FLOAT NOT NULL);''' %name
        cursor.execute(cq)
        conn.commit()
        conn.close()

def del_category(name):
    """This method removes categories from the 'categories' table and and drops the table that holds its expenses
    Side Effects:
        removes a row from database and table from database that represents the parameter's category
    """
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    dq = '''DROP TABLE %s;''' %name
    conn.commit()
    drq = '''DELETE FROM categories WHERE category_name = "%s"''' %name
    cursor.execute(dq)
    cursor.execute(drq)
    conn.commit()
    conn.close()

def insert_expense(category, name, expense):
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    with conn:
        db_tuple = name, expense
        gq = '''INSERT INTO %s (expense_name, expense_amount) VALUES (?,?)''' %category
        cursor.execute(gq, db_tuple)
    conn.commit()
    conn.close()

def budget_maxed(category, amount):
    """This method checks to see if the expense being added exceeds the category's max amount
    """
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    sq1 = '''SELECT * FROM %s''' %category
    cat_expenses = cursor.execute(sq1).fetchall()
    sq2 = '''SELECT max_amount FROM categories WHERE category_name = "%s"''' % category
    max_amount = cursor.execute(sq2)
    int(max_amount)
    
    cat_total = 0
    for expense in cat_expenses:
        cat_total = cat_total + expense[0]
    
    if float(amount) + cat_total > max_amount:
        return True
    else:
        return False
    conn.close()
