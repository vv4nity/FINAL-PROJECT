#FINAL PROJECT FOR OBJECT ORIENTED PROGRAMMING

import tkinter as tk
from tkinter import messagebox
import csv
from tkinter.ttk import Progressbar, Treeview


class LoadingScreen:
    def __init__(self):
        self.w = tk.Tk()
        self.width_of_window = 427
        self.height_of_window = 250
        self.screen_width = self.w.winfo_screenwidth()
        self.screen_height = self.w.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.w.geometry("%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.w.overrideredirect(1)

        self.a = '#249794'
        tk.Frame(self.w, width=427, height=241, bg=self.a).place(x=0, y=0)  # 249794
        self.b1 = tk.Button(self.w, width=10, height=1, text='Get Started', command=self.bar, border=0, fg=self.a, bg='white')
        self.b1.place(x=170, y=200)

        self.l1 = tk.Label(self.w, text='ADDRESS', fg='white', bg=self.a)
        self.lst1 = ('HomepageBaukasten-Bold', 18, 'bold')
        self.l1.config(font=self.lst1)
        self.l1.place(x=50, y=80)

        self.l2 = tk.Label(self.w, text='BOOK', fg='white', bg=self.a)
        self.lst2 = ('HomepageBaukasten-Book', 18)
        self.l2.config(font=self.lst2)
        self.l2.place(x=180, y=80)

        self.l3 = tk.Label(self.w, text='FINAL PROJECT FOR OOP', fg='white', bg=self.a)
        self.lst3 = ('HomepageBaukasten-Book', 13)
        self.l3.config(font=self.lst3)
        self.l3.place(x=50, y=110)

        self.s = tk.ttk.Style()
        self.s.theme_use('clam')
        self.s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
        self.progress = Progressbar(self.w, style="red.Horizontal.TProgressbar", orient=tk.HORIZONTAL, length=500, mode='determinate')

    def bar(self):
        l4 = tk.Label(self.w, text='Loading...', fg='white', bg=self.a)
        lst4 = ('Calibri (Body)', 10)
        l4.config(font=lst4)
        l4.place(x=18, y=210)

        import time
        r = 0
        for i in range(100):
            self.progress['value'] = r
            self.w.update_idletasks()
            time.sleep(0.03)
            r = r + 1

        self.w.destroy()
        AddressBookGUI()

    def run(self):
        self.progress.place(x=-10, y=235)
        self.w.mainloop()


class AddressBookGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Address Book")
        self.window.geometry("500x400")

        self.title_label = tk.Label(self.window, text="ADDRESS BOOK", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.add_button = tk.Button(self.window, text="Add Contact", command=self.open_add_contact)
        self.edit_button = tk.Button(self.window, text="Edit Contact", command=self.open_edit_contact)
        self.delete_button = tk.Button(self.window, text="Delete Contact", command=self.open_delete_contact)
        self.view_button = tk.Button(self.window, text="View Contacts", command=self.view_contacts)

        self.add_button.pack(pady=10)
        self.edit_button.pack(pady=10)
        self.delete_button.pack(pady=10)
        self.view_button.pack(pady=10)

        # Search feature
        self.search_frame = tk.Frame(self.window)
        self.search_frame.pack(pady=10)

        self.search_label = tk.Label(self.search_frame, text="Search:")
        self.search_label.grid(row=0, column=0, padx=5)

        self.search_query_entry = tk.Entry(self.search_frame)
        self.search_query_entry.grid(row=0, column=1, padx=5)

        self.search_type_var = tk.StringVar()
        self.search_type_var.set("First Name")

        self.search_type_label = tk.Label(self.search_frame, text="Search Type:")
        self.search_type_label.grid(row=0, column=2, padx=5)

        self.search_type_menu = tk.OptionMenu(
            self.search_frame, self.search_type_var, "First Name", "Last Name", "Address", "Contact Number"
        )
        self.search_type_menu.grid(row=0, column=3, padx=5)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_address_book)
        self.search_button.grid(row=0, column=4, padx=5)

        # Load data from file
        self.entries = self.load_data()

    def open_address_book(self):
        self.window.destroy()
        address_book = AddressBookGUI()
        address_book.run()

    def load_data(self):
        try:
            with open('address_book.csv', 'r') as file:
                reader = csv.reader(file)
                entries = list(reader)
            return entries
        except FileNotFoundError:
            return []

    def save_data(self):
        with open('address_book.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.entries)

    def open_add_contact(self):
        self.window.destroy()
        add_contact_window = AddContactWindow(self)
        add_contact_window.run()

    def open_edit_contact(self):
        self.window.destroy()
        edit_contact_window = EditContactWindow(self)
        edit_contact_window.run()

    def open_delete_contact(self):
        self.window.destroy()
        delete_contact_window = DeleteContactWindow(self)
        delete_contact_window.run()

    def view_contacts(self):
        self.window.destroy()
        view_contacts_window = ViewContactsWindow(self)
        view_contacts_window.run()

    def search_address_book(self):
        search_query = self.search_query_entry.get()
        search_type = self.search_type_var.get()

        # Perform the search based on the selected search type
        matches = []
        if search_type == "First Name":
            matches = [entry for entry in self.entries if entry[0].lower() == search_query.lower()]
        elif search_type == "Last Name":
            matches = [entry for entry in self.entries if entry[1].lower() == search_query.lower()]
        elif search_type == "Address":
            matches = [entry for entry in self.entries if search_query.lower() in entry[2].lower()]
        elif search_type == "Contact Number":
            matches = [entry for entry in self.entries if search_query.lower() in entry[3].lower()]

        # Display matched entries or notify user if not found
        if matches:
            contacts = "\n".join(
                [f"{i + 1}. {entry[0]} {entry[1]} - {entry[2]}, {entry[3]}" for i, entry in enumerate(matches)]
            )
            messagebox.showinfo("Search Results", contacts)
        else:
            messagebox.showinfo("Search Results", "No matches found.")

    def run(self):
        self.window.mainloop()


class AddContactWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Tk()
        self.window.title("Add Contact")
        self.window.geometry("400x400")

        self.title_label = tk.Label(self.window, text="ADDRESS BOOK", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.first_name_label = tk.Label(self.window, text="First Name:")
        self.first_name_entry = tk.Entry(self.window)
        self.last_name_label = tk.Label(self.window, text="Last Name:")
        self.last_name_entry = tk.Entry(self.window)
        self.address_label = tk.Label(self.window, text="Address:")
        self.address_entry = tk.Entry(self.window)
        self.contact_number_label = tk.Label(self.window, text="Contact Number:")
        self.contact_number_entry = tk.Entry(self.window)
        self.add_button = tk.Button(self.window, text="Add Contact", command=self.add_contact, width=15)
        self.back_button = tk.Button(self.window, text="Back to Main Page", command=self.back_to_main_page)

        self.first_name_label.pack()
        self.first_name_entry.pack()
        self.last_name_label.pack()
        self.last_name_entry.pack()
        self.address_label.pack()
        self.address_entry.pack()
        self.contact_number_label.pack()
        self.contact_number_entry.pack()
        self.add_button.pack(pady=10)
        self.back_button.pack(pady=5)

    def add_contact(self):
        # Get input from user
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        address = self.address_entry.get()
        contact_number = self.contact_number_entry.get()

        # Data validation
        if not first_name or not last_name or not address or not contact_number:
            messagebox.showerror("Error", "Please enter all fields.")
            return

        # Add the contact to the entries list
        self.parent.entries.append([first_name, last_name, address, contact_number])

        # Save data to file
        self.parent.save_data()

        messagebox.showinfo("Success", "Contact added successfully.")
        self.clear_entries()

    def back_to_main_page(self):
        self.window.destroy()
        main_menu = AddressBookGUI()
        main_menu.open_address_book()

    def clear_entries(self):
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_number_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()


class EditContactWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Tk()
        self.window.title("Edit Contact")
        self.window.geometry("400x400")

        self.title_label = tk.Label(self.window, text="ADDRESS BOOK", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.entry_number_label = tk.Label(self.window, text="Entry Number:")
        self.entry_number_entry = tk.Entry(self.window)
        self.first_name_label = tk.Label(self.window, text="First Name:")
        self.first_name_entry = tk.Entry(self.window)
        self.last_name_label = tk.Label(self.window, text="Last Name:")
        self.last_name_entry = tk.Entry(self.window)
        self.address_label = tk.Label(self.window, text="Address:")
        self.address_entry = tk.Entry(self.window)
        self.contact_number_label = tk.Label(self.window, text="Contact Number:")
        self.contact_number_entry = tk.Entry(self.window)
        self.update_button = tk.Button(self.window, text="Update Contact", command=self.update_contact, width=15)
        self.back_button = tk.Button(self.window, text="Back to Main Page", command=self.back_to_main_page)

        self.entry_number_label.pack()
        self.entry_number_entry.pack()
        self.first_name_label.pack()
        self.first_name_entry.pack()
        self.last_name_label.pack()
        self.last_name_entry.pack()
        self.address_label.pack()
        self.address_entry.pack()
        self.contact_number_label.pack()
        self.contact_number_entry.pack()
        self.update_button.pack(pady=10)
        self.back_button.pack(pady=5)

    def update_contact(self):
        # Get input from user
        entry_number = self.entry_number_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        address = self.address_entry.get()
        contact_number = self.contact_number_entry.get()

        # Data validation
        if not entry_number or not first_name or not last_name or not address or not contact_number:
            messagebox.showerror("Error", "Please enter all fields.")
            return

        # Convert entry number to index
        index = int(entry_number) - 1

        # Check if the index is valid
        if index < 0 or index >= len(self.parent.entries):
            messagebox.showerror("Error", "Invalid entry number.")
            return

        # Update the contact in the entries list
        self.parent.entries[index] = [first_name, last_name, address, contact_number]

        # Save data to file
        self.parent.save_data()

        messagebox.showinfo("Success", "Contact updated successfully.")
        self.clear_entries()

    def back_to_main_page(self):
        self.window.destroy()
        main_menu = AddressBookGUI()
        main_menu.open_address_book()

    def clear_entries(self):
        self.entry_number_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.contact_number_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()


class DeleteContactWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Tk()
        self.window.title("Delete Contact")
        self.window.geometry("400x400")

        self.title_label = tk.Label(self.window, text="ADDRESS BOOK", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.entry_number_label = tk.Label(self.window, text="Entry Number:")
        self.entry_number_entry = tk.Entry(self.window)
        self.delete_button = tk.Button(self.window, text="Delete Contact", command=self.delete_contact, width=15)
        self.back_button = tk.Button(self.window, text="Back to Main Page", command=self.back_to_main_page)

        self.entry_number_label.pack()
        self.entry_number_entry.pack()
        self.delete_button.pack(pady=10)
        self.back_button.pack(pady=5)

    def delete_contact(self):
        # Get input from user
        entry_number = self.entry_number_entry.get()

        # Data validation
        if not entry_number:
            messagebox.showerror("Error", "Please enter an entry number.")
            return

        # Convert entry number to index
        index = int(entry_number) - 1

        # Check if the index is valid
        if index < 0 or index >= len(self.parent.entries):
            messagebox.showerror("Error", "Invalid entry number.")
            return

        # Confirm deletion
        confirm = messagebox.askyesno(
            "Confirm Deletion",
            f"Do you want to delete the contact:\n{self.parent.entries[index][0]} {self.parent.entries[index][1]}"
            f"\nAddress: {self.parent.entries[index][2]}\nContact Number: {self.parent.entries[index][3]}",
        )

        if confirm:
            # Delete the contact from the entries list
            del self.parent.entries[index]

            # Save data to file
            self.parent.save_data()

            messagebox.showinfo("Success", "Contact deleted successfully.")
            self.clear_entries()

    def back_to_main_page(self):
        self.window.destroy()
        main_menu = AddressBookGUI()
        main_menu.open_address_book()

    def clear_entries(self):
        self.entry_number_entry.delete(0, tk.END)

    def run(self):
        self.window.mainloop()


class ViewContactsWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Tk()
        self.window.title("View Contacts")
        self.window.geometry("500x400")

        self.title_label = tk.Label(self.window, text="ADDRESS BOOK", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        self.contacts_treeview = Treeview(self.window)
        self.contacts_treeview["columns"] = ("First Name", "Last Name", "Address", "Contact Number")
        self.contacts_treeview.column("#0", width=0, stretch=tk.NO)
        self.contacts_treeview.column("First Name", anchor=tk.CENTER, width=100)
        self.contacts_treeview.column("Last Name", anchor=tk.CENTER, width=100)
        self.contacts_treeview.column("Address", anchor=tk.CENTER, width=150)
        self.contacts_treeview.column("Contact Number", anchor=tk.CENTER, width=150)

        self.contacts_treeview.heading("#0", text="", anchor=tk.CENTER)
        self.contacts_treeview.heading("First Name", text="First Name", anchor=tk.CENTER)
        self.contacts_treeview.heading("Last Name", text="Last Name", anchor=tk.CENTER)
        self.contacts_treeview.heading("Address", text="Address", anchor=tk.CENTER)
        self.contacts_treeview.heading("Contact Number", text="Contact Number", anchor=tk.CENTER)

        self.contacts_treeview.pack(pady=10)

        self.back_button = tk.Button(self.window, text="Back to Main Page", command=self.back_to_main_page)
        self.back_button.pack(pady=5)

    def back_to_main_page(self):
        self.window.destroy()
        main_menu = AddressBookGUI()
        main_menu.open_address_book()

    def display_contacts(self):
        for i, entry in enumerate(self.parent.entries):
            self.contacts_treeview.insert(
                parent="", index=tk.END, iid=i, text="", values=(entry[0], entry[1], entry[2], entry[3])
            )

    def run(self):
        self.display_contacts()
        self.window.mainloop()

if __name__ == "__main__":
    loading_screen = LoadingScreen()
    loading_screen.run()
