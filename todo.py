import json, os, sys

FILE = "todos.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save(todos):
    with open(FILE, "w") as f:
        json.dump(todos, f)

todos = load()
cmd = sys.argv[1] if len(sys.argv) > 1 else ""

if cmd == "add":
    todos.append({"text": " ".join(sys.argv[2:]), "done": False})
    save(todos)
elif cmd == "list":
    for i, t in enumerate(todos, 1):
        print(i, "[x]" if t["done"] else "[ ]", t["text"])
elif cmd == "done":
    todos[int(sys.argv[2]) - 1]["done"] = True
    save(todos)
else:
    print("usage: add <text> | list | done <n>")
