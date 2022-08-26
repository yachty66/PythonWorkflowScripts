from tkinter import *

root = Tk()
root.title('Codemy.com - Auto Select/Search')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")

def body(self, master):        
    self.e1 = tk.Listbox(master, selectmode=tk.SINGLE, height = 3, exportselection=0)
    self.e1.insert(tk.END, "1")
    self.e1.insert(tk.END, "2")

    self.e1.grid(row=0, column=1)
    self.selection = 0
    self.e1.select_set(self.selection)

    self.e1.bind("<Down>", self.OnEntryDown)
    self.e1.bind("<Up>", self.OnEntryUp)

def OnEntryDown(self, event):
    if self.selection < self.e1.size()-1:
        self.e1.select_clear(self.selection)
        self.selection += 1
        self.e1.select_set(self.selection)

def OnEntryUp(self, event):
    if self.selection > 0:
        self.e1.select_clear(self.selection)
        self.selection -= 1
        self.e1.select_set(self.selection)
# Create a label
my_label = Label(root, text="Search",
	font=("Helvetica", 14), fg="grey")

my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a list of pizza toppings
toppings = ["Pepperoni", "Peppers", "Mushrooms",
	"Cheese", "Onions", "Ham", "Taco"]

# Add the toppings to our list
update(toppings)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()