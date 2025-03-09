from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


class ContactList:
    def __init__(home, root):
        home.root = root
        home.root.title("Contact List")

        home.contacts = []

        # Create main frame
        home.frame = ttk.Frame(home.root, padding="10")
        home.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Name label and entry
        home.name_label = ttk.Label(home.frame, text="Name:")
        home.name_label.grid(row=0, column=0, sticky=tk.W)

        home.name_entry = ttk.Entry(home.frame, width=40)
        home.name_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        # Email label and entry
        home.email_label = ttk.Label(home.frame, text="Email:")
        home.email_label.grid(row=1, column=0, sticky=tk.W)

        home.email_entry = ttk.Entry(home.frame, width=40)
        home.email_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Phone label and entry
        home.phone_label = ttk.Label(home.frame, text="Phone:")
        home.phone_label.grid(row=2, column=0, sticky=tk.W)

        home.phone_entry = ttk.Entry(home.frame, width=40)
        home.phone_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

        # Add contact button
        home.add_button = ttk.Button(home.frame, text="Add Contact", command=home.add_contact)
        home.add_button.grid(row=3, column=1, sticky=tk.W)

        # Treeview to display contacts
        home.contacts_treeview = ttk.Treeview(home.frame, columns=("Name", "Email", "Phone"), show="headings", height=10)
        home.contacts_treeview.heading("Name", text="Name")
        home.contacts_treeview.heading("Email", text="Email")
        home.contacts_treeview.heading("Phone", text="Phone")
        home.contacts_treeview.column("Name", width=100, anchor=tk.CENTER)
        home.contacts_treeview.column("Email", width=150)
        home.contacts_treeview.column("Phone", width=100)
        home.contacts_treeview.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Delete contact button
        home.delete_button = ttk.Button(home.frame, text="Delete Contact", command=home.delete_contact)
        home.delete_button.grid(row=5, column=0, sticky=tk.W)

        # Update contact button
        home.update_button = ttk.Button(home.frame, text="Update Contact", command=home.update_contact)
        home.update_button.grid(row=5, column=1, sticky=tk.W)

        # Clear all contacts button
        home.clear_button = ttk.Button(home.frame, text="Clear All Contacts", command=home.clear_contacts)
        home.clear_button.grid(row=5, column=2, sticky=tk.W)

        # Search label and entry
        home.search_label = ttk.Label(home.frame, text="Search:")
        home.search_label.grid(row=6, column=0, sticky=tk.W)

        home.search_entry = ttk.Entry(home.frame, width=40)
        home.search_entry.grid(row=6, column=1, sticky=(tk.W, tk.E))

        # Search button
        home.search_button = ttk.Button(home.frame, text="Search", command=home.search_contact)
        home.search_button.grid(row=6, column=2, sticky=tk.W)

    def add_contact(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        if name and email and phone:
            self.contacts.append({"name": name, "email": email, "phone": phone})
            self.update_contacts_treeview()
            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter name, email, and phone number.")

    def delete_contact(self):
        selected_item = self.contacts_treeview.selection()
        if selected_item:
            item_index = self.contacts_treeview.index(selected_item)
            self.contacts.pop(item_index)
            self.update_contacts_treeview()
        else:
            messagebox.showwarning("Warning", "You must select a contact to delete.")

    def update_contact(self):
        selected_item = self.contacts_treeview.selection()
        if selected_item:
            name = self.name_entry.get()
            email = self.email_entry.get()
            phone = self.phone_entry.get()
            if name and email and phone:
                item_index = self.contacts_treeview.index(selected_item)
                self.contacts[item_index]["name"] = name
                self.contacts[item_index]["email"] = email
                self.contacts[item_index]["phone"] = phone
                self.update_contacts_treeview()
                self.name_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.phone_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter name, email, and phone number.")
        else:
            messagebox.showwarning("Warning", "You must select a contact to update.")

    def clear_contacts(self):
        self.contacts.clear()
        self.update_contacts_treeview()

    def update_contacts_treeview(self):
        # Clear the treeview
        for item in self.contacts_treeview.get_children():
            self.contacts_treeview.delete(item)
        # Insert updated contacts
        for contact in self.contacts:
            self.contacts_treeview.insert("", tk.END, values=(contact["name"], contact["email"], contact["phone"]))

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        # Clear previous selection
        for item in self.contacts_treeview.get_children():
            self.contacts_treeview.selection_remove(item)
        if search_term:
            # Select contacts that match the search term
            for item in self.contacts_treeview.get_children():
                name = self.contacts_treeview.item(item, "values")[0].lower()
                email = self.contacts_treeview.item(item, "values")[1].lower()
                phone = self.contacts_treeview.item(item, "values")[2].lower()
                if search_term in name or search_term in email or search_term in phone:
                    self.contacts_treeview.selection_add(item)
        else:
            messagebox.showwarning("Warning", "You must enter a search term.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactList(root)
    root.mainloop()
