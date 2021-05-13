import sqlite3
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import Text, TOP, BOTH, X, N, LEFT

LARGE_FONT = ("Verdana", 25)


class Main(tk.Tk):
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

        conn = sqlite3.connect('budget_tracker.db')  # initializes database
        cursor = conn.cursor()
        cq = "CREATE TABLE IF NOT EXISTS categories (categoryid INTEGER PRIMARY KEY, category_name TEXT, max_amount INTEGER);"
        cursor.execute(cq)
        conn.close()  # initialize budget tracker database

        self.show_frame(StartPage)

    def get_page(self, page_class):
        return self.frames[page_class]

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(
            self, text="Welcome to your Budget Tracker!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        label = tk.Label(
            self, text="Add new Categories or Manage your purchases within each category.")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Add a category",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="View your Categories",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

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

        submit = tk.Button(self, text="Submit Category",
                           command=lambda: self.added(entry1.get(), entry2.get()))
        submit.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Edit your Categories",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

    def added(self, name, max_amount):
        """Verifies that the category has been added to user. Adds category to a global database 'categories' table
        Parameters:
            name (String): name of the category
            max_amount (int): max_amount the user can spend in that category
        """

        conn = sqlite3.connect('budget_tracker.db')
        cursor = conn.cursor()
        db_tuple = name, max_amount
        iq = '''INSERT INTO categories(category_name, max_amount) VALUES (?,?)'''
        cursor.execute(iq,db_tuple)
        cq = '''CREATE TABLE IF NOT EXISTS {name} (categoryid INTEGER PRIMARY KEY, category_name TEXT, max_amount INTEGER);'''
        conn.commit()
        conn.close()
        
        label = tk.Label(self, text="Category Added")
        label.pack(padx=10, pady=10)

class PageTwo(tk.Frame):
    """Allows user to see their categories via a dropdown menu.
    """
    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        #Dropdown creation
        conn = sqlite3.connect('budget_tracker.db')
        cursor = conn.cursor()
        sq = '''SELECT category_name FROM categories'''
        sq_names = cursor.execute(sq).fetchall()
        conn.close()
        
        category_names = list() #following line and loop gets categories from the database and puts them in a list
        for tup in sq_names:
            category_names.append(tup[0])
        
        framex = tk.Frame(self)
        framex.pack()
        clicked = tk.StringVar()        # datatype of menu text
        clicked.set("Category")     # initial menu text
        # Create Dropdown menu
        drop = tk.OptionMenu(framex, clicked, category_names)
        drop.pack()
        button = tk.Button(framex, text="Edit Category")
        button.pack()   # Create button,changes label
        label = tk.Label(self, text=" ")        # Create Label
        label.pack(pady=10, padx=10)

        #label = tk.Label(self, text="Manage your purchases below", font=LARGE_FONT)
        frame1 = tk.Frame(self, width=100, height=100)
        frame1.pack()

        label = tk.Label(frame1, text="Name of Good")
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
        B1 = tk.Button(frame4, text="Insert Purchase",
                       command=lambda: self.added())
        B1.pack()

        '''B2 = tk.Button(frame4, text="Select All")
        B2.pack()
        
        B3 = tk.Button(frame4, text="Find value")
        B3.pack()'''

        #B4 = tk.Button(frame4, text="Delete expense")
        #B4.pack()
        B5 = tk.Button(frame4, text="Home",
                       command=lambda: controller.show_frame(StartPage))
        B5.pack()
    
    def added(self):
        """Verifies that the category has been added to user. Adds category to a global dictionary of categories
        Parameters:
            name (String): name of the category
            max_amount (int): max_amount the user can spend in that category
        """
        label = tk.Label(self, text="Expense Added")
        label.pack(padx=10, pady=10)
    def show(self):
        tk.label.config(text=tk.clicked.get())

    def add_category_button(self, controller, name):
        Button1 = tk.Button(self, text=name.upper())


app = Main()
app.mainloop()
