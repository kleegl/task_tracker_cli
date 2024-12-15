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

            if is_contains is False:
                print(f"Id {id} не найден!")

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
            for task in data:
                if task["id"] == id:
                    data.remove(task)
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


match args.task_action:
    case "add":
        add_task(args.task)
    case "update":
        update_task(args.task_number, args.task)
    case "delete":
        delete_task(args.task_number)
