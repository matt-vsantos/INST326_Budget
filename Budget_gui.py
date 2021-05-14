import budget_database as db
import sqlite3
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Text, TOP, BOTH, X, N, LEFT

LARGE_FONT = ("Verdana", 25)


class Main(tk.Tk):
    """This class initializes the GUI and sets up a database file where all budget information will be stored
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # initialize budget tracker database
        db.init_database()
        
        self.show_frame(StartPage)

    def get_page(self, page_class):
        return self.frames[page_class]

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    """Home page of the user interface. Users can navigate to two PageOne() and PageTwo().
    """
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Welcome to your Budget Tracker!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(
            self, text="Add new Categories or Manage your purchases within each category.")
        label.pack(pady=10, padx=10)
        
        #Navigation to 'Add a category page'
        button = tk.Button(self, text="Add a category", pady=7,
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        #Navigation to 'View and Edit your Categories' page
        button2 = tk.Button(self, text="View and Edit your Categories", pady=7,
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):
    """The user can enter the name of the category and it's associated maximum spend. This will add a row into the categories table and create a new table to store that category's expenses
    """
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        
        #Instructions Label
        label = tk.Label(
            self, text="Enter the category and the maximum amount you can spend (FORMAT EXAMPLE: \"300.00\" or  \"2000\")")
        label.pack(pady=5, padx=10)
        #Create entry box for category name
        frame1 = tk.Frame(self)
        frame1.pack()

        label = tk.Label(frame1, text="Name of Category")
        label.pack(side=LEFT, padx=10, pady=10)

        entry1 = tk.Entry(frame1)
        entry1.pack(padx=5, expand=True)

        #Create entry box for category max amount
        frame2 = tk.Frame(self)
        frame2.pack()

        label = tk.Label(frame2, text="Category Maximum")
        label.pack(side=LEFT, padx=10, pady=10)

        entry2 = tk.Entry(frame2)
        entry2.pack(padx=5, expand=True)

        frame3 = tk.Frame(self)
        frame3.pack()

        submit = tk.Button(self, text="Submit Category", pady=7,
                           command=lambda: self.cat_added(entry1.get(), entry2.get()))
        submit.pack()

        button2 = tk.Button(self, text="Edit your Categories", pady=7,
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        button1 = tk.Button(self, text="Back to Home", pady=7,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
            
    def cat_added(self, name, amount):
        """Checks if entries are valid. If so, checks if the category being added already exists. Displays that a category has been added for 5 seconds
        """
        categories = db.get_categories()
        valid = self.valid_entry(name, amount)
        
        if valid and name not in categories:
            db.add_category(name, amount)
            label = tk.Label(self, text="Category Added", bg="green")
            label.pack(padx=10, pady=10)
            label.after(3000, lambda: label.destroy())
        elif valid and name in categories:
            label = tk.Label(self, text="Category Already Exists", bg="red")
            label.pack(padx=10, pady=10)
            label.after(3000, lambda: label.destroy())

    def valid_entry(self, name, amount):
        """This method verifies that the name of the category is a valid string and the amount is a valid number
        """
        if (name == '' or type(name) != str) and (type(amount) != int or type(amount) != float):
            label = tk.Label(self, text="Invalid entry", bg="Red")
            label.pack(padx=10, pady=10)
            label.after(3000, lambda: label.destroy())
            return False
        else:
            self.cat_added(name, amount)
            return True
        
class PageTwo(tk.Frame):
    """Allows user to see their categories via a dropdown menu.
    """
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        #Dropdown creation
        category_names = db.get_categories()    #fetch category names from database
        label = tk.Label(
            self, text="Select a category from the dropdown list and either choose to edit the expenses in the category OR delete the category")
        label.pack(pady=10, padx=10)
        
        framex = tk.Frame(self)
        framex.pack()
        
        #drop down list of categories
        clicked = tk.StringVar()        # datatype of menu text
        clicked.set("Select A Category")     # initial menu text
        # Create Dropdown menu
        drop = tk.OptionMenu(framex, clicked, '', *category_names)
        drop.pack(pady=5)
        
        button = tk.Button(
            framex, text="Edit your Categories", pady=7)
        button.pack()   # Create button,changes label
        button1 = tk.Button(self, text="Delete Category", pady=7,
                            command=lambda: [self.cat_deleted(clicked.get()), db.del_category(clicked.get())])
        button1.pack()
        
        label = tk.Label(self, text="Enter the name of the expense and how much you spent on it (FORMAT EXAMPLE:  \"12.46\" or \"20\")" )      # Create Label
        label.pack(pady=5, padx=10)

        #label = tk.Label(self, text="Manage your purchases below", font=LARGE_FONT)
        frame1 = tk.Frame(self, width=100, height=100)
        frame1.pack()

        label = tk.Label(frame1, text="Name of Expense")
        label.pack(side=LEFT, padx=10, pady=15)

        entry1 = tk.Entry(frame1)
        entry1.pack(padx=5, expand=True)

        frame3 = tk.Frame(self, width=100, height=100)
        frame3.pack()

        label = tk.Label(frame3, text="Price")
        label.pack(side=LEFT, padx=10, pady=10)

        entry3 = tk.Entry(frame3)
        entry3.pack(padx=5, expand=True)


        #BUTTONS###
        frame4 = tk.Frame(self)
        frame4.pack()
        B1 = tk.Button(frame4, text="Insert Purchase", pady=7, 
                       command=lambda: self.added())
        B1.pack()

        B2 = tk.Button(frame4, text="Home", pady=7,
                       command=lambda: controller.show_frame(StartPage))
        B2.pack()

    def added(self):
        """Verifies that the category has been added to user for 5 seconds. Adds category to a global dictionary of categories
        Parameters:
            name (String): name of the category
            max_amount (int): max_amount the user can spend in that category
        """
        label = tk.Label(self, text="Expense Added", bg = "green")
        label.pack(padx=10, pady=10)
        label.after(3000, lambda: label.destroy())
        
    def cat_deleted(self,name):
        """Displays that a category has been added to user for 5 seconds
        """
        label = tk.Label(self, text="Category: %s Deleted" %name, bg="yellow")
        label.pack(padx=10, pady=10)
        label.after(3000, lambda: label.destroy())



app = Main()
app.mainloop()
