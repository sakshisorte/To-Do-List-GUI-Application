# ==========================================
# TO-DO LIST GUI APPLICATION
# Developed By : Sakshi Sorte
#
# Description:
# A simple GUI-based To-Do List application
# using Python Tkinter.
#
# Features:
# 1. Add Task
# 2. Mark Task as Completed
# 3. Delete Task
# 4. View Tasks
# ==========================================

import tkinter as tk
from tkinter import messagebox


# Function to add a task
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return

    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)


# Function to mark selected task as completed
def complete_task():
    try:
        selected_task = task_listbox.curselection()[0]

        current_task = task_listbox.get(selected_task)

        # Avoid adding check mark multiple times
        if not current_task.startswith("✔ "):
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, "✔ " + current_task)

    except IndexError:
        messagebox.showwarning(
            "Warning",
            "Please select a task to mark as completed!"
        )


# Function to delete selected task
def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)

    except IndexError:
        messagebox.showwarning(
            "Warning",
            "Please select a task to delete!"
        )


# Function to clear all tasks
def clear_tasks():
    if task_listbox.size() == 0:
        messagebox.showinfo("Info", "Task list is already empty.")
        return

    confirm = messagebox.askyesno(
        "Confirm",
        "Are you sure you want to clear all tasks?"
    )

    if confirm:
        task_listbox.delete(0, tk.END)


# =============================
# Main Window
# =============================

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")
root.resizable(False, False)

# Heading
title_label = tk.Label(
    root,
    text="TO-DO LIST",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

# Frame for Entry
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_entry = tk.Entry(
    input_frame,
    width=30,
    font=("Arial", 14)
)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(
    input_frame,
    text="Add Task",
    width=12,
    command=add_task
)
add_button.pack(side=tk.LEFT)

# Frame for Listbox
list_frame = tk.Frame(root)
list_frame.pack(pady=15)

scrollbar = tk.Scrollbar(list_frame)

task_listbox = tk.Listbox(
    list_frame,
    width=45,
    height=12,
    font=("Arial", 12),
    selectbackground="lightblue"
)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.pack(side=tk.LEFT)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

complete_button = tk.Button(
    button_frame,
    text="Mark Completed",
    width=15,
    command=complete_task
)
complete_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    width=15,
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear All",
    width=15,
    command=clear_tasks
)
clear_button.grid(row=0, column=2, padx=5)

# Run Application
root.mainloop()