import argparse
import json
from datetime import datetime
from task_model import Task

parser = argparse.ArgumentParser()
parser.add_argument_group("tasks")
subparser = parser.add_subparsers(dest="task_action")

add_parser = subparser.add_parser("add", help="Добавить задачу")
add_parser.add_argument("task", type=str, help="Текст задачи")

update_parser = subparser.add_parser("update", help="Обновить задачу")
update_parser.add_argument("task_number", type=int, help="Номер задачи")
update_parser.add_argument("task", type=str, help="Текст задачи")

delete_parser = subparser.add_parser("delete", help="Удалить задачу")
delete_parser.add_argument("task_number", type=int, help="Номер задачи")

mark_in_progress_parser = subparser.add_parser("mark-in-progress", help="Отметить задачу 'В процессе'")
mark_in_progress_parser.add_argument("task_number", type=int, help="Номер задачи")

mark_done_parser = subparser.add_parser("mark-done", help="Отметить задачу 'Выполнено'")
mark_done_parser.add_argument("task_number", type=int, help="Номер задачи")

list_parser = subparser.add_parser("list", help="Вывести все задачи")
in_progress_parser = subparser.add_parser("in-progress", help="Вывести все задачи в статусе 'В прогрессе'")
done_parser = subparser.add_parser("done", help="Вывести все выполненные задачи")
todo_parser = subparser.add_parser("todo", help="Вывести все невыполненные задачи")


args = parser.parse_args()


def add_task(task):
    with open("tasks.json", "r+") as file:
        new_task_id: int = 0
        if len(file.readlines()) == 0:
            data: list = []
        else:
            file.seek(0)
            data: list = json.load(file)
            for item in data:
                if item["id"] > new_task_id:
                    new_task_id = item["id"]
        new_task_id += 1
        new_task = Task(
            id=new_task_id,
            description=task,
            status=0,
            createdAt=str(datetime.now()),
            updatedAt=str(datetime.now()))
        data.append(obj_to_dict(new_task))
        file.seek(0)
        json.dump(data, file, indent=4, separators=(",", ": "))
        file.close()
        print(f"Задача успешно добавлена (id: {new_task_id})")


def update_task(id, task):
    with open("tasks.json", "r+") as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            data: list[dict] = list(json.load(file))
            is_contains = False

            for item in data:
                if item.get("id") == id:
                    is_contains = True
                    item["description"] = task
                    continue

            if is_contains is False:
                print(f"ID: {id} не найден!")

            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
            print(f"Задача с ID:{id} была обновлена.")
        else:
            print("Файл пуст!")
            return
        file.close()


def delete_task(id):
    with open("tasks.json", "r+") as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            data: list[dict] = list(json.load(file))
            is_contains = False

            for task in data:
                if task["id"] == id:
                    data.remove(task)
                    is_contains = True
                    continue

            if is_contains is False:
                print(f"ID: {id} не найден!")
  
            file.seek(0)
            json.dump(data, file, indent=4, separators=(",", ": "))
            file.truncate()
            print(f"Задача с ID:{id} была удалена.")
        else:
            print("Файл пуст!")
            return
        file.close()


def obj_to_dict(obj):
    return {
        attr: getattr(obj, attr)
        for attr in dir(obj) if not attr.startswith('_')
    }


def mark_in_progress_task(id):
    with open("tasks.json", "r+") as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            data: list[dict] = list(json.load(file))
            is_contains = False

            for task in data:
                if task["id"] == id:
                    task["status"] = 1
                    is_contains = True
                    continue

            if is_contains is False:
                print(f"ID: {id} не найден!")

            file.seek(0)
            json.dump(data, file, indent=4, separators=(",", ": "))
            file.truncate()
            print(f"Задача с ID:{id} в процессе!")
        else:
            print("Файл пуст!")


def mark_done_task(id):
    with open("tasks.json", "r+") as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            data: list[dict] = list(json.load(file))
            is_contains = False

            for task in data:
                if task["id"] == id:
                    task["status"] = 2
                    is_contains = True
                    continue

            if is_contains is False:
                print(f"ID: {id} не найден!")

            file.seek(0)
            json.dump(data, file, indent=4, separators=(",", ": "))
            file.truncate()
            print(f"Задача с ID:{id} завершена!")
        else:
            print("Файл пуст!")


def show_all_tasks():
    with open("tasks.json", "r+") as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            data: list[dict] = list(json.load(file))

            for task in data:
                print(task)
        else:
            print("Файл пуст!")


def show_in_progress_tasks():
    with open("tasks.json", "r+") as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            data: list[dict] = list(json.load(file))

            for task in data:
                if task["status"] == 1:
                    print(task)
        else:
            print("Файл пуст!")


def show_done_tasks():
    with open("tasks.json", "r+") as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            data: list[dict] = list(json.load(file))

            for task in data:
                if task["status"] == 2:
                    print(task)
        else:
            print("Файл пуст!")


def show_todo_tasks():
    with open("tasks.json", "r+") as file:
        if len(file.readlines()) != 0:
            file.seek(0)
            data: list[dict] = list(json.load(file))

            for task in data:
                if task["status"] == 0:
                    print(task)
        else:
            print("Файл пуст!")


match args.task_action:
    case "add":
        add_task(args.task)
    case "update":
        update_task(args.task_number, args.task)
    case "delete":
        delete_task(args.task_number)
    case "mark-in-progress":
        mark_in_progress_task(args.task_number)
    case "mark-done":
        mark_done_task(args.task_number)
    case "list":
        show_all_tasks()
    case "in-progress":
        show_in_progress_tasks()
    case "done":
        show_done_tasks()
    case "todo":
        show_todo_tasks()
