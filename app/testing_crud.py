import requests

BASE_URL = "http://127.0.0.1:8000/todos/"

new_todo = {
    "title": "Сделать задание по FastAPI",
    "description": "Не забыть протестировать CRUD операции",
    "completed": False
}

create_todo = requests.post(BASE_URL, json=new_todo)

if create_todo.status_code == 200:
    print("Задача успешно создана:", create_todo.json())
else:
    print("Ошибка при создании задачи:", create_todo.text)


todo_id = post_todo.json().get("id")

get_todo = requests.get(f"{BASE_URL}{todo_id}")

if get_todo.status_code == 200:
    print("Задача успешно получена:", get_todo.json())
else:
    print("Ошибка при получении задачи:", get_todo.text)


updated_todo = {
    "title": "Сделать задание по FastAPI",
    "description": "Обновлено: протестировать CRUD операции и деплой",
    "completed": True
}

update_todo = requests.put(f"{BASE_URL}{todo_id}", json=updated_todo)
if update_todo.status_code == 200:
    print("Задача успешно обновлена:", update_todo.json())
else:
    print("Ошибка при обновлении задачи:", update_todo.text)


get_todos = requests.get(BASE_URL)
if get_todos.status_code == 200:
    print("Все задачи:", get_todos.json())
else:
    print("Ошибка при получении всех задач:", get_todos.text)


delete_todo = requests.delete(f"{BASE_URL}{todo_id}")
if delete_todo.status_code == 200:
    print("Задача успешно удалена:", delete_todo.json())
else:
    print("Ошибка при удалении задачи:", delete_todo.text)