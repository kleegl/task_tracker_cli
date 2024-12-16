# Task Tracker CLI

## Использование

## Описание команд

### add
Добавить задачу

### update
Обновить задачу

### delete
Удалить задачу

### mark-in-progress
Отметить задачу 'В процессе'

### mark-done
Отметить задачу 'Выполнено'

### list
Вывести все задачи

### in-progress
Вывести все задачи в статусе 'В прогрессе'

### done
Вывести все выполненные задачи

### todo
Вывести все невыполненные задачи

## Особенности реализации

- Программа работает из командной строки.
- Принимает действия пользователя и входные данные как аргументы.
- Хранит задачи в файле JSON.

### Пользователь может:

- Добавлять новые задачи
- Обновлять существующие
- Удалять задачи
- Отмечать статус задачи как 'В процессе' или 'Выполнено'
- Выводить список всех задач
- Фильтровать задачи по статусу

## Каждая задача должна иметь следующие свойства:

- Описание
- Статус
- Дата создания
- Дата обновления

```json
{
  "id": 1,
  "description": "something",
  "status": 0,
  "createdAt": "2023-01-01T00:00:00Z",
  "updatedAt": "2023-01-01T00:00:00Z"
}