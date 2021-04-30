
from tkinter import *
from tkinter.ttk import *

LARGE_FONT = ("Verdana", 32)


class BudgetTracker:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.main_window()

    #grid, labels, buttons windows will come shortly after

### display function calls for database update deletion and listing added or deleted#
    def added(self, boxaile):
        myLabel = Label(boxaile, text="The purchase has been inserted")
        myLabel.grid(row=4, column=0)

    def delete(self, boxaile):
        myLabel = Label(boxaile, text="The purchase was deleted")
        myLabel.grid(row=4, column=0)

    def display_all(self, database):
        select_all = database
        return select_all

    def insert(self, database, val1, val2, val3):
        goods = val1.get()
        price = val2.get()
        date = val3.get()
        insertion = database(goods, price, date)
        return insertion

    def find_expense(self, database, val1, val2):
        goods = val1.get()
        price = val2.get()
        find = database(goods, price)
        return find

    def delete_expense(self, database, val1, val2):
        goods = val1.get()
        price = val2.get()
        delete = database(goods, price)
        return delete

    def groceries(self):

        top = Toplevel(self.frame)
        top.title('Groceries budget')
        l1 = Label(top, text="Name of good").grid(
            row=1, column=0, sticky=W, pady=2)
        l2 = Label(top, text="Price").grid(row=2, column=0, sticky=W, pady=2)
        l3 = Label(top, text="Date of purchase").grid(
            row=3, column=0, sticky=W, pady=2)

        e1 = Entry(top)
        e1.grid(row=1, column=1, sticky=W, pady=2)
        e2 = Entry(top)
        e2.grid(row=2, column=1, sticky=W, pady=2)
        e3 = Entry(top)
        e3.grid(row=3, column=1, sticky=W, pady=2)

        text = Text(top, width=40, height=10)
        text.grid(row=5, column=1, columnspan=2)

        #BUTTONS###

        B1 = Button(top, text="Insert Purchases", command=lambda: (
            self.insert(db.insert_groceries, e1, e2, e3), self.added(top)))
        B1.grid(row=1, column=2)

        B2 = Button(top, text="Select All", command=lambda: (text.delete(
            1.0, END), text.insert(END, self.display_all(db.select_all_groceries()))))
        B2.grid(row=2, column=2)

        B3 = Button(top, text="Find value", command=lambda: (text.delete(
            1.0, END), text.insert(END, self.find_expense(db.select_grocery, e1, e2))))
        B3.grid(row=2, column=3)

        B3 = Button(top, text="Delete expense", command=lambda: (
            self.delete_expense(db.delete_grocery, e1, e2), self.delete(top)))
        B3.grid(row=4, column=2)

        B5 = Button(top, text="Exit", command=exit)
        B5.grid(row=4, column=3)
     ###MAIN WINDOW###

    def main_window(self):
        button1 = Button(self.frame, text="Groceries Budget",
                         command=self.groceries)
        button1.pack()

        button5 = Button(self.frame, text="EXIT", command=exit)
        button5.pack()

# the main function will be at the end of the script


def main():
    #db.create_tables(connection)
    root = Tk()
    root.geometry('250x200')
    root.title("Budget Tracker")
    tracker = BudgetTracker(root)

    root.mainloop()


if __name__ == '__main__':
    main()
