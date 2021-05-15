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

def get_cat_spend(category):
    """This method returns the total amount that has been spent in the category and the category's max amount
    Return:
        tuple: the current amount spent
    """
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    sq1 = '''SELECT expense_amount FROM %s''' % category
    cat_expenses = cursor.execute(sq1).fetchall()
    sq2 = '''SELECT max_amount FROM categories WHERE category_name = "%s"''' % category
    max_amount_obj = cursor.execute(sq2)
    max_amount = max_amount_obj.fetchone()[0]

    cat_spend = 0
    for expense in cat_expenses:
        cat_spend = cat_spend + expense[0]
    
    conn.close()
    return cat_spend, max_amount   
        
def budget_maxed(category, amount):
    """This method checks to see if the expense being added exceeds the category's max amount
    Returns:
        tuple: the max_amount for the category, how much has been spent
    """
    cat_spend = get_cat_spend(category)
    famount = float(amount)
    
    if famount + cat_spend[0] > cat_spend[1]:
        return True
    else:
        return False

def get_expenses(category):
    """This method returns a list of expensee from a specified category
    Parameters:
        category (str): the category whose expenses are being fetched
    """
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    sq1 = '''SELECT expenseid, expense_name, expense_amount FROM %s''' % category
    expenses = cursor.execute(sq1).fetchall()
    formatted_expenses = list()
    for each in expenses:
        text = "{}.  {}, for ${}".format(each[0], each[1], each[2])
        formatted_expenses.append(text)
        
    return formatted_expenses

def delete_expense (category, expense_id):
    """This method deletes expenses for a category's table 
    Parameters:
        category (str): the category to be deleted
        expense_id (str): the expense to be deleted
    Side Effects: 
        deletes the row of 'expense_id' from 'category table
    """
    conn = sqlite3.connect('budget_tracker.db')
    cursor = conn.cursor()
    drq = '''DELETE FROM %s WHERE expenseid = (?)''' % category
    cursor.execute(drq, expense_id)
    conn.commit()
    conn.close()
    

    
