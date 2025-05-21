Welcome to the **To-Do List App** – a simple command-line application to manage your daily tasks using Python. This project demonstrates Python fundamentals such as lists, functions, control structures, user input handling, and error management.

---

## Features

- **Add Task:** Add new items to your to-do list.
- **View Tasks:** Display all current tasks.
- **Delete Task:** Remove tasks by selecting their number.
- **Quit:** Exit the application gracefully.
- **Input Validation:** Handles invalid menu choices and improper deletions.
- **Error Handling:** Uses `try/except` blocks for robust, user-friendly experience.
- **Organized Code:** All functionality is split into clear, well-documented functions.

---

## How to Run

### Prerequisites

- Python 3.x installed ([Download here](https://www.python.org/downloads/))

### Steps

1. **Clone this repository or download the code:**

   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. **Run the application:**

   ```bash
   python todo.py
   ```

---

## Usage

1. On running, you’ll see a welcome message and menu options:
    ```
    Welcome to "To Do List App"
    Here you can add, view, and delete tasks.

    Select 1 to add a task
    Select 2 to view tasks
    Select 3 to delete a task
    Select Q to quit
    ```
2. Enter `1` to add a task (you’ll be prompted for the description).
3. Enter `2` to view all current tasks.
4. Enter `3` to delete a task (you’ll be asked for the task number).
5. Enter `Q` to quit the app.

### Example Session

```
Welcome to "To Do List App"
Here you can add, view, and delete tasks.

Select 1 to add a task
Select 2 to view tasks
Select 3 to delete a task
Select Q to quit

Please enter your option  1
Please enter what task you want to add to the To Do List apps?  Buy groceries
Task "Buy groceries" added successfully!
here is your tasks summary ['Buy groceries']

Please enter your option  2
Your tasks:
1. Buy groceries

Please enter your option  3
1. Buy groceries
Select the number of the task you want to delete  1
Task "Buy groceries" deleted.
your remaining tasks is []
```

---

## Code Structure

- **`todo.py`**: Main Python file with all logic.
  - `show_menu()`: Displays the menu.
  - `add_task(tasks)`: Adds a task.
  - `view_task(tasks)`: Lists tasks.
  - `delete_task(tasks)`: Deletes a task by number.
  - `main()`: Main loop and user interaction.

---

## Notes

- Tasks are stored in memory only and will reset when you exit.
- Input is validated and errors are handled with helpful messages.
- You can further enhance this app by adding persistent storage (e.g., saving to a file).

---

## License

This project is for educational use.

---

## Author

[Suryadi Zhang]

---

Enjoy managing your tasks!
