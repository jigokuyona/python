import json

def load_todos(filename: str) -> list[dict]:
    try:
        with open(filename) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: File not found.")

def print_todos(data: list[dict]):
    for todo in data:
        print(todo)

def count_todos(filename: str) -> int:
    return len(load_todos(filename))

def add_todo(filename: str, todo: dict):
    try:
        data = load_todos(filename)
        data.append(todo)
        todo["id"] = count_todos(filename) + 1
        with open(filename, "w") as file:
            json.dump(data, file, indent=4, separators=(',', ': '), ensure_ascii=False)
    except FileNotFoundError:
        print("Error: File not found.")

def remove_todo(filename: str, id: int):
    try:
        data = load_todos(filename)
        for todo in data:
            if todo["id"] == id:
                data.remove(todo)
        update_indexes(filename)
                
        with open(filename, "w") as file:
            json.dump(data, file, indent=4, separators=(',', ': '), ensure_ascii=False)
    except FileNotFoundError:
        print("Error: File not found.")

def update_indexes(filename: str):
    data = load_todos(filename)
    i = 1
    for todo in data:
        todo["id"] = i
        i += 1
    with open(filename, "w") as file:
        json.dump(data, file, indent=4, separators=(',', ': '), ensure_ascii=False)

todo = {
    "id" : 0,
    "deadline" : "2027-10-25T14:30:00",
    "description": "Learn data structers and algorithms",
    "alarm": True,
    "priority": 1,
    "tags": ["school", "urgent", "important"]
}

add_todo("todos.json", todo)
remove_todo("todos.json", 3)