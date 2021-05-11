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

        self.init_db()  # initializae budget tracker database
        # initializes dictionary of categories (key: name, values: max_amount)
        self.categories = dict()

        self.show_frame(StartPage)

    def get_page(self, page_class):
        return self.frames[page_class]

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def init_db(self):
        conn = sqlite3.connect('budget_tracker.db')  # initializes database
        cursor = conn.cursor()
        global cq
        cq = "CREATE TABLE IF NOT EXISTS categories (categoryid INTEGER PRIMARYKEY, category_name TEXT, max_amount INTEGER)"
        cursor.execute(cq)
        conn.close()


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

        button2 = tk.Button(self, text="View your Categories",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

    def added(self, name, max_amount):
        """Verifies that the category has been added to user. Adds category to a global dictionary of categories
        Parameters:
            name (String): name of the category
            max_amount (int): max_amount the user can spend in that category
        """
        self.controller.categories[name] = {
            max_amount}  # access categories dictionary from Main

        label = tk.Label(self, text="Category Added")
        label.pack(padx=10, pady=10)


class PageTwo(tk.Frame):
    """Allows user to see their categories via a dropdown menu.
    """

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        #Dropdown creation
        #dp = self.controller.categories.keys()
        framex = tk.Frame(self)
        framex.pack()
        clicked = tk.StringVar()        # datatype of menu text
        clicked.set("Category")     # initial menu text
        # Create Dropdown menu
        drop = tk.OptionMenu(framex, clicked, "groceries")
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
        #entry1.pack(padx=5, expand=True)

        #Create entry box for category max amount
        frame2 = tk.Frame(self, width=100, height=100)
        frame2.pack()

        label = tk.Label(frame2, text="Date Bought")
        label.pack(side=LEFT, padx=10, pady=10)

        entry2 = tk.Entry(frame2)
        entry2.pack(padx=5, expand=True)

        frame3 = tk.Frame(self, width=100, height=100)
        frame3.pack()

        label = tk.Label(frame3, text="Price")
        label.pack(side=LEFT, padx=10, pady=10)

        entry3 = tk.Entry(frame3)
        entry3.pack(padx=5, expand=True)

        frame3 = tk.Frame(self)
        frame3.pack()

        entry3 = tk.Entry(frame1)
        entry3.pack(padx=5, expand=True)

        #BUTTONS###
        frame4 = tk.Frame(self)
        frame4.pack()
        B1 = tk.Button(frame4, text="Insert Purchases")
        B1.pack()

        '''B2 = tk.Button(frame4, text="Select All")
        B2.pack()
        
        B3 = tk.Button(frame4, text="Find value")
        B3.pack()'''

        B4 = tk.Button(frame4, text="Delete expense")
        B4.pack()
        B5 = tk.Button(frame4, text="Home",
                       command=lambda: controller.show_frame(StartPage))
        B5.pack()

    def show(self):
        tk.label.config(text=tk.clicked.get())

    def add_category_button(self, controller, name):
        Button1 = tk.Button(self, text=name.upper())


app = Main()
app.mainloop()
