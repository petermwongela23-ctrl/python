# ============================================
# TO-DO LIST
# ============================================

# Our list to hold tasks
tasks = []

def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 35)
    print("         TO-DO LIST")
    print("=" * 35)
    print("  1. View tasks")
    print("  2. Add a task")
    print("  3. Mark task as done")
    print("  4. Remove a task")
    print("  5. Quit")
    print("=" * 35)

def view_tasks():
    """Show all tasks."""
    if not tasks:
        print("\n  No tasks yet! Add one.")
        return
    
    print("\n  Your Tasks:")
    print("  " + "-" * 33)
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"  {i}. [{status}] {task['name']}")
    print("  " + "-" * 33)

def add_task():
    """Add a new task."""
    task_name = input("\n  Enter task: ")
    if task_name.strip():
        tasks.append({"name": task_name.strip(), "done": False})
        print(f"  Added: '{task_name.strip()}'")
    else:
        print("  Task cannot be empty!")

def mark_done():
    """Mark a task as completed."""
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("\n  Enter task number to mark done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"  Done! '{tasks[task_num - 1]['name']}' completed!")
        else:
            print("  Invalid task number.")
    except ValueError:
        print("  Please enter a valid number.")

def remove_task():
    """Remove a task from the list."""
    view_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("\n  Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"  Removed: '{removed['name']}'")
        else:
            print("  Invalid task number.")
    except ValueError:
        print("  Please enter a valid number.")


# ---------- Main Program ----------
show_menu()

while True:
    choice = input("\n  Pick an option (1-5): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("\n  Goodbye! Stay productive! ✅")
        break
    else:
        print("  Invalid option. Pick 1-5.")
    
    show_menu()