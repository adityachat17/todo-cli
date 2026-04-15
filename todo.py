import json
import os

DATA_FILE = "todos.json"

def load_todos():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_task(todos, task):
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f"✅ Added: '{task}'")

def list_tasks(todos):
    if not todos:
        print("No tasks yet! Add one with: add <task>")
        return
    print("\n📋 Your To-Do List:")
    for i, item in enumerate(todos, 1):
        status = "✔" if item["done"] else "○"
        print(f"  {i}. [{status}] {item['task']}")
    print()

def complete_task(todos, index):
    if 1 <= index <= len(todos):
        todos[index - 1]["done"] = True
        save_todos(todos)
        print(f"🎉 Marked done: '{todos[index - 1]['task']}'")
    else:
        print("Invalid task number.")

def delete_task(todos, index):
    if 1 <= index <= len(todos):
        removed = todos.pop(index - 1)
        save_todos(todos)
        print(f"🗑️  Deleted: '{removed['task']}'")
    else:
        print("Invalid task number.")

def main():
    todos = load_todos()
    print("📝 To-Do CLI — commands: add | list | done | delete | quit")
    while True:
        command = input("\n> ").strip().lower()
        if command.startswith("add "):
            add_task(todos, command[4:])
        elif command == "list":
            list_tasks(todos)
        elif command.startswith("done "):
            complete_task(todos, int(command[5:]))
        elif command.startswith("delete "):
            delete_task(todos, int(command[7:]))
        elif command in ("quit", "exit", "q"):
            print("Goodbye! 👋")
            break
        else:
            print("Unknown command. Try: add <task> | list | done <#> | delete <#> | quit")

if __name__ == "__main__":
    main()
