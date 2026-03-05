"""
CLI-based To-Do List Application
=================================
A simple command-line tool that lets users manage their daily tasks.
Users can add, view, mark as complete, and remove tasks.
Tasks are stored in a list of dictionaries for easy management.
"""


# ──────────────────────────────────────────────
#  Data Store
# ──────────────────────────────────────────────
# Each task is a dictionary: {"id": int, "task": str, "done": bool}
tasks: list[dict] = []

# Auto-incrementing counter so every task gets a unique ID
_next_id: int = 1


# ──────────────────────────────────────────────
#  Helper – horizontal rule for formatting
# ──────────────────────────────────────────────
def _separator() -> str:
    """Return a decorative line used to separate sections in the console."""
    return "─" * 50


# ──────────────────────────────────────────────
#  Core Functions
# ──────────────────────────────────────────────

def add_task(description: str) -> None:
    """
    Add a new task to the list.

    Parameters
    ----------
    description : str
        A short description of the task to add.
    """
    global _next_id
    # Create a task dictionary and append it to the list
    task = {"id": _next_id, "task": description.strip(), "done": False}
    tasks.append(task)
    print(f"\n  [+] Task #{_next_id} added: \"{description.strip()}\"")
    _next_id += 1  # Increment the ID counter for the next task


def view_tasks() -> None:
    """
    Display all tasks in a clean, formatted table.
    Shows task ID, completion status, and description.
    """
    print(f"\n{_separator()}")
    print("  YOUR TO-DO LIST")
    print(_separator())

    if not tasks:
        # Inform the user when there are no tasks
        print("  (no tasks yet – add one!)")
    else:
        # Print each task with a status indicator
        for t in tasks:
            status = "Done" if t["done"] else "Pending"
            marker = "[x]" if t["done"] else "[ ]"
            print(f"  {marker}  #{t['id']:>3}  |  {t['task']:<30}  ({status})")

    print(_separator())


def mark_done(task_id: int) -> None:
    """
    Mark a task as completed by its ID.

    Parameters
    ----------
    task_id : int
        The unique ID of the task to mark as done.
    """
    # Search for the task with the matching ID
    for t in tasks:
        if t["id"] == task_id:
            if t["done"]:
                print(f"\n  [i] Task #{task_id} is already marked as done.")
            else:
                t["done"] = True
                print(f"\n  [✓] Task #{task_id} marked as done!")
            return

    # If we reach here, no task matched the given ID
    print(f"\n  [!] Task #{task_id} not found.")


def remove_task(task_id: int) -> None:
    """
    Remove a task from the list by its ID.

    Parameters
    ----------
    task_id : int
        The unique ID of the task to remove.
    """
    # Search for the task with the matching ID
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            removed = tasks.pop(i)  # Remove the task from the list
            print(f"\n  [-] Removed task #{task_id}: \"{removed['task']}\"")
            return

    # If we reach here, no task matched the given ID
    print(f"\n  [!] Task #{task_id} not found.")


# ──────────────────────────────────────────────
#  Menu Display
# ──────────────────────────────────────────────

def show_menu() -> None:
    """Print the main menu options to the console."""
    print("\n╔════════════════════════════════════╗")
    print("║      TO-DO LIST  –  MAIN MENU      ║")
    print("╠════════════════════════════════════╣")
    print("║  1. Add a task                      ║")
    print("║  2. View all tasks                  ║")
    print("║  3. Mark a task as done             ║")
    print("║  4. Remove a task                   ║")
    print("║  5. Exit                            ║")
    print("╚════════════════════════════════════╝")


# ──────────────────────────────────────────────
#  Main Loop
# ──────────────────────────────────────────────

def main() -> None:
    """
    Entry point – runs an interactive loop that presents the menu,
    reads the user's choice, and dispatches to the appropriate function.
    """
    print("\n  Welcome to the CLI To-Do List App!")
    print("  Type a menu number to get started.\n")

    while True:
        show_menu()
        choice = input("\n  Enter your choice (1-5): ").strip()

        if choice == "1":
            # ── Add a task ──────────────────────
            description = input("  Enter the task description: ").strip()
            if description:
                add_task(description)
            else:
                print("\n  [!] Task description cannot be empty.")

        elif choice == "2":
            # ── View all tasks ──────────────────
            view_tasks()

        elif choice == "3":
            # ── Mark a task as done ─────────────
            view_tasks()  # Show tasks first so user can pick an ID
            try:
                task_id = int(input("  Enter the task ID to mark as done: "))
                mark_done(task_id)
            except ValueError:
                print("\n  [!] Please enter a valid numeric ID.")

        elif choice == "4":
            # ── Remove a task ───────────────────
            view_tasks()  # Show tasks first so user can pick an ID
            try:
                task_id = int(input("  Enter the task ID to remove: "))
                remove_task(task_id)
            except ValueError:
                print("\n  [!] Please enter a valid numeric ID.")

        elif choice == "5":
            # ── Exit ────────────────────────────
            print("\n  Goodbye! Have a productive day!\n")
            break

        else:
            # ── Invalid input ───────────────────
            print("\n  [!] Invalid choice. Please select 1-5.")


# Run the app only when executed directly (not when imported)
if __name__ == "__main__":
    main()
