import sqlite3 as sql
import ***first script***

class Budget:
  """This class creates a list to store budget category objects using information inputted from the GUI. Additionally, it will create a 
  corresponding table in SQL
    Attributes:
    	budget_name (String): the name of the person's budget
    	category (Category): represents a category in the budget
      income (int): total income that the user can create the budget with
    Side Effects:
    	Create table in SQL for current user's budget
      Create a list to store budget category objects
  """
	def __init__(self, budget_name, income):
  	budget = list()
    self.budget_name = budget_name
    self.income = income
    sql_create_budget()	
  
  def add_category(category):
   """This method adds a budget category object to the list; verify that the sum of the categories' max_amounts don't exceed total income;
   will print message telling the user how much of their income they have left to budget (calls 'update_user' method
    Parameters:
    	category (Category): represents the budget category
    Side Effects:
    	updates budget list with new category
   """
  
  def update_category(category_name, new_amount):
  """This method allows users to update the max_amount of a category; will verify that the new amount does not exceed income
  Parameters:
  	category_name (String): this is the name of the category whose max_amount will be changed
    new_amount (int): the new max_amount for the specified category
  Side Effects:
  	updates specific index within the budget list
  """
  
  def del_category(category_name):
  """This method allows users to remove categories from the budget list one at a time
  Parameters:
  	category_name (String): the category to be removed from the budget list
  Side Effects:
  	budget list will be modified
  """
  
  def update_user():
  """This method prints a message to the user telling them the remainder of their income they have left to budget
  """
  
  def print_budget():
  """This method prints the budget list for the user
  """
  
  #If we add the 'report expense' functionality, we will need another create method with columns specific to the table storing expenses
  def sql_create_budget():
    """
    :functionality: Create a blank database
    """
    conn = sql.connect(':memory:')
    click = conn.cursor()

    cq = '''CREATE TABLE budget (
          #column DATATYPE
          )'''
          cursor.execute(cq)
    return cq
  
  def sql_insert():
	"""
  :functionality: This will insert the data from the list into the table
  """

class Category:
    """This class creates a budget category object using information inputted
    Attributes:
    	category_name (String): name of 
			max_amount (int): max amount 
    Side Effects:
    	Create table in SQL for current user's budget
      Create a dictionary to store budget categories
  """
	def __init__(self, category_name, max_amount):
  	self.category_name = category_name
    self.max_amount = max_amount
