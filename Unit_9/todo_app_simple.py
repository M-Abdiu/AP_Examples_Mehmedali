from nicegui import ui

tasks = []  # app state


def refresh_tasks():
    task_list.clear()
    with task_list:
        for i, task in enumerate(tasks):
            with ui.row():
                ui.checkbox(
                    value=task['done'],
                    on_change=lambda e, i=i: toggle_task(i, e.value)
                )
                ui.label(task['text'])
                ui.button(
                    'Delete',
                    on_click=lambda i=i: delete_task(i)
                )


def add_task():
    text = task_input.value.strip()
    if not text:
        ui.notify('Please enter a task', type='warning')
        return

    # check if task already exists (case-insensitive)
    already_exists = any(task['text'].lower() == text.lower() for task in tasks)
    if already_exists:
        ui.notify(f'Task "{text}" already exists!', type='warning')
        return

    tasks.append({'text': text, 'done': False})
    task_input.value = ''
    refresh_tasks()
    ui.notify(f'Task "{text}" added', type='positive')


def toggle_task(index, done):
    tasks[index]['done'] = done
    refresh_tasks()


def delete_task(index):
    deleted = tasks.pop(index)
    refresh_tasks()
    ui.notify(f'Task "{deleted["text"]}" deleted', type='negative')


ui.label('Todo List App').classes('text-2xl font-bold')

with ui.row():
    task_input = ui.input('New task')
    ui.button('Add', on_click=add_task)

task_list = ui.column()

refresh_tasks()

ui.run()