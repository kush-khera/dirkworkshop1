import streamlit as st
import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from a JSON file, returns a list of task dictionaries."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Saves the list of task dictionaries to a JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def main():
    st.title("My To-Do List Manager")
    st.write("A simple app to add, remove, and mark tasks as complete.")

    # Load existing tasks
    tasks = load_tasks()

    # -- Add a new task --
    st.subheader("Add a New Task")
    new_task = st.text_input("Enter task:")
    if st.button("Add Task"):
        if new_task.strip():
            tasks.append({"task": new_task.strip(), "completed": False})
            save_tasks(tasks)
            st.success(f"Added task: {new_task}")
        else:
            st.warning("Please enter a valid task.")

    st.write("---")

    # -- Display existing tasks --
    st.subheader("Your Tasks")
    if tasks:
        for i, task in enumerate(tasks):
            col1, col2, col3 = st.columns([0.6, 0.2, 0.2])
            
            # Show task text, with a strike-through if completed
            if task["completed"]:
                col1.write(f"~~{task['task']}~~")
            else:
                col1.write(task["task"])
            
            # 'Mark Complete' button
            if not task["completed"]:
                if col2.button("Mark Complete", key=f"complete_{i}"):
                    tasks[i]["completed"] = True
                    save_tasks(tasks)
                    st.experimental_rerun()
            else:
                col2.write("✔️")

            # 'Delete' button
            if col3.button("Delete", key=f"delete_{i}"):
                deleted_task = tasks.pop(i)
                save_tasks(tasks)
                st.warning(f"Deleted task: {deleted_task['task']}")
                st.experimental_rerun()
    else:
        st.info("No tasks found. Add one above!")

if __name__ == "__main__":
    main()
