# INST326_Budget

Our project will enable users to create a categorical budget. Using the income, users will be able to list their monthly expenses such as rent and car payments. With the remaining money, users will be able to set budget amounts for other categories such as food, gas, self care, and entertainment. They will be able to insert expenses into any category and the program will tell them when they’ve exceeded their listed budget. 

TESTING:
Make sure all of the files are in the same folder. From the command line, run the following:

    python3 Budget_gui.py

Once the frame shows up, navigate to 'Add a Category' to add categories and their associated spending limits:
    TO TEST ERROR HANDLING:
      Adding any symbols or numbers or spaces in the first entry field should not add a category. An error notification should pop up.
      Adding anything but numbers in the second entry field should not add a category. An error notification should pop up.
      
To view categories and insert purchases, click on and navigate to the 'View and Edit Categories' page:
    Click the 'Select A Category' button to view your categories. Select a category from the dropdown list and click it.
      Click on 'Delete A Category' to delete the category in the dropdown menu. A message should pop up saying it has been deleted.
      Click on 'See How Much You've Spent' to view how much you've spent compared to the spending limit. A message should pop up telling you and disappear within       seconds.
      Enter expenses or purchases and click 'Insert Purchase' to insert the purchase into it's respective category

To Verify a purchase/expense has been added, click on and navigate to 'Edit Category Expenses'
    Click the 'Select A Category' button to view your categories: 
      Select a category from the dropdown list and click 'Select this category' to edit.
      Click the arrows to view expenses in the dropdown list.
        Click 'Delete This Expense' to delete the expense, or simply navigate back to any of the other pages
