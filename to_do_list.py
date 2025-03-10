import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import images

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Create main frame
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Task label and entry
        self.task_label = ttk.Label(self.frame, text="Task:")
        self.task_label.grid(row=0, column=0, sticky=tk.W)

        self.task_entry = ttk.Entry(self.frame, width=40)
        self.task_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        # Add task button
        self.add_button = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, sticky=tk.W)

        # Treeview to display tasks
        self.tasks_treeview = ttk.Treeview(self.frame, columns=("Number", "Task", "Completed"), show="headings", height=10)
        self.tasks_treeview.heading("Number", text="Numbers")
        self.tasks_treeview.heading("Task", text="Task")
        self.tasks_treeview.heading("Completed", text="Completed")
        self.tasks_treeview.column("Number", width=50, anchor=tk.CENTER)
        self.tasks_treeview.column("Task", width=300)
        self.tasks_treeview.column("Completed", width=100)
        self.tasks_treeview.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Delete task button
        self.delete_button = ttk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, sticky=tk.W)

        # Update task button
        self.update_button = ttk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, sticky=tk.W)

        # Clear all tasks button
        self.clear_button = ttk.Button(self.frame, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=2, sticky=tk.W)

        # Search label and entry
        self.search_label = ttk.Label(self.frame, text="Search:")
        self.search_label.grid(row=3, column=0, sticky=tk.W)

        self.search_entry = ttk.Entry(self.frame, width=40)
        self.search_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

        # Search task button
        self.search_button = ttk.Button(self.frame, text="Search Task", command=self.search_task)
        self.search_button.grid(row=3, column=2, sticky=tk.W)

        # Exit button
        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=4, column=2, sticky=tk.W)

        # Labels to display task counts
        self.completed_label = ttk.Label(self.frame, text="Completed Tasks: 0")
        self.completed_label.grid(row=4, column=0, sticky=tk.W)

        self.incomplete_label = ttk.Label(self.frame, text="Incomplete Tasks: 0")
        self.incomplete_label.grid(row=4, column=1, sticky=tk.W)

        # Menu bar
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # View menu
        self.view_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Toggle Fullscreen", command=self.toggle_fullscreen)
        self.view_menu.add_command(label="Resize Window", command=self.resize_window)

        self.fullscreen = False

        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        # Bind double-click event to toggle task completion
        self.tasks_treeview.bind("<Double-1>", self.toggle_task_completion)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": tk.BooleanVar()})
            self.update_tasks_treeview()
            self.task_entry.delete(0, tk.END)
            self.update_task_counts()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        selected_item = self.tasks_treeview.selection()
        if selected_item:
            item_index = self.tasks_treeview.index(selected_item)
            self.tasks.pop(item_index)
            self.update_tasks_treeview()
            self.update_task_counts()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task(self):
        selected_item = self.tasks_treeview.selection()
        if selected_item:
            new_task = self.task_entry.get()
            if new_task:
                item_index = self.tasks_treeview.index(selected_item)
                self.tasks[item_index]["task"] = new_task
                self.update_tasks_treeview()
                self.task_entry.delete(0, tk.END)
                self.update_task_counts()
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def clear_tasks(self):
        self.tasks.clear()
        self.update_tasks_treeview()
        self.update_task_counts()

    def update_tasks_treeview(self):
        # Clear the treeview
        for item in self.tasks_treeview.get_children():
            self.tasks_treeview.delete(item)
        # Insert updated tasks
        for index, task in enumerate(self.tasks, start=1):
            completed_status = "Yes" if task["completed"].get() else "No"
            self.tasks_treeview.insert("", tk.END, values=(index, task["task"], ""), tags=("checkbox",))
            self.tasks_treeview.set(self.tasks_treeview.get_children()[-1], column="Completed", value=task["completed"].get())

    def search_task(self):
        search_term = self.search_entry.get().lower()
        # Clear previous selection
        for item in self.tasks_treeview.get_children():
            self.tasks_treeview.selection_remove(item)
        if search_term:
            # Select tasks that match the search term
            for item in self.tasks_treeview.get_children():
                task = self.tasks_treeview.item(item, "values")[1]
                if search_term in task.lower():
                    self.tasks_treeview.selection_add(item)
        else:
            messagebox.showwarning("Warning", "You must enter a search term.")

    def toggle_task_completion(self, event):
        selected_item = self.tasks_treeview.selection()
        if selected_item:
            item_index = self.tasks_treeview.index(selected_item)
            self.tasks[item_index]["completed"].set(not self.tasks[item_index]["completed"].get())
            self.update_tasks_treeview()
            self.update_task_counts()

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)

    def resize_window(self):
        self.fullscreen = False
        self.root.attributes("-fullscreen", False)
        self.root.geometry("800x600")

    def update_task_counts(self):
        completed_count = sum(task["completed"].get() for task in self.tasks)
        incomplete_count = len(self.tasks) - completed_count
        self.completed_label.config(text=f"Completed Tasks: {completed_count}")
        self.incomplete_label.config(text=f"Incomplete Tasks: {incomplete_count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()