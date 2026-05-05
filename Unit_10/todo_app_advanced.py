from nicegui import ui


# -------------------------
# Business Logic
# -------------------------
class TaskService:
    def __init__(self) -> None:
        self.tasks: list[dict] = []

    def normalize_task_text(self, text: str) -> str:
        return ' '.join(text.strip().lower().split())

    def get_open_task_count(self) -> int:
        return sum(not task['done'] for task in self.tasks)

    def exists(self, text: str) -> bool:
        normalized = self.normalize_task_text(text)
        return any(
            self.normalize_task_text(task['text']) == normalized
            for task in self.tasks
        )

    def validate_new_task(self, text: str) -> str | None:
        if not text:
            return 'Please enter a task.'
        if self.exists(text):
            return 'That task already exists.'
        return None

    def add_task(self, text: str) -> str | None:
        cleaned = text.strip()
        error = self.validate_new_task(cleaned)

        if error:
            return error

        self.tasks.append({
            'text': cleaned,
            'done': False,
        })
        return None

    def delete_task(self, task: dict) -> None:
        if task in self.tasks:
            self.tasks.remove(task)

    def toggle_task(self, task: dict, done: bool) -> None:
        task['done'] = done


# -------------------------
# UI / Orchestration
# -------------------------
class TodoApp:
    def __init__(self, service: TaskService) -> None:
        self.service = service

        self.ui_state = {
            'new_task': '',
        }
        self.feedback_message = ''
        self.task_list = None

    # -------------------------
    # UI Event Logic
    # -------------------------
    def set_feedback(self, message: str = '') -> None:
        self.feedback_message = message
        self.render_feedback.refresh()

    def clear_feedback(self) -> None:
        self.set_feedback()

    def add_task(self) -> None:
        error = self.service.add_task(self.ui_state['new_task'])

        if error:
            self.set_feedback(error)
            return

        self.ui_state['new_task'] = ''
        self.clear_feedback()
        self.refresh_ui()

    def delete_task(self, task: dict) -> None:
        self.service.delete_task(task)
        self.refresh_ui()

    def toggle_task(self, task: dict, done: bool) -> None:
        self.service.toggle_task(task, done)
        self.refresh_ui()

    def refresh_ui(self) -> None:
        self.render_feedback.refresh()
        self.render_status.refresh()
        self.render_tasks.refresh()

    # -------------------------
    # UI Rendering
    # -------------------------
    def build_header(self) -> None:
        with ui.column().classes('items-center gap-2 text-center'):
            ui.label('Todo List').classes('text-4xl font-bold tracking-tight text-slate-800')
            ui.label('OOP approach with separation of concerns').classes(
                'text-sm text-slate-500'
            )

    def build_input_section(self) -> None:
        with ui.card().classes(
            'w-full max-w-2xl rounded-2xl border border-slate-200 bg-white/90 p-4 shadow-sm'
        ):
            with ui.row().classes('w-full items-center gap-3'):
                ui.input(
                    placeholder='Add a new task',
                    on_change=lambda _: self.clear_feedback(),
                ).classes(
                    'flex-grow rounded-xl'
                ).props(
                    'outlined clearable'
                ).bind_value(self.ui_state, 'new_task')

                ui.button('Add task', on_click=self.add_task).classes(
                    'rounded-xl bg-slate-800 px-5 py-3 text-white hover:bg-slate-700'
                )

    @ui.refreshable
    def render_feedback(self) -> None:
        if self.feedback_message:
            ui.label(self.feedback_message).classes('text-sm font-medium text-rose-600')
        else:
            ui.label(' ').classes('text-sm')

    @ui.refreshable
    def render_status(self) -> None:
        open_count = self.service.get_open_task_count()
        total_count = len(self.service.tasks)

        with ui.row().classes('items-center justify-center'):
            with ui.element('div').classes(
                'inline-flex items-center gap-3 rounded-full border border-slate-200 '
                'bg-white px-5 py-3 shadow-sm'
            ):
                ui.label(f'{open_count} open').classes('text-base font-semibold text-slate-800')
                ui.label('•').classes('text-slate-300')
                ui.label(f'{total_count} total').classes('text-sm text-slate-500')

    @ui.refreshable
    def render_tasks(self) -> None:
        self.task_list.clear()

        with self.task_list:
            if not self.service.tasks:
                with ui.card().classes(
                    'w-full rounded-2xl border border-dashed border-slate-300 bg-white/70 p-8 shadow-sm'
                ):
                    with ui.column().classes('items-center gap-2 text-center'):
                        ui.label('No tasks yet').classes('text-lg font-semibold text-slate-700')
                        ui.label('Add your first task above to get started.').classes(
                            'text-sm text-slate-500'
                        )
                return

            for task in self.service.tasks:
                card_classes = (
                    'w-full rounded-2xl border p-4 shadow-sm transition hover:shadow-md'
                )
                card_classes += (
                    ' border-slate-200 bg-white'
                    if not task['done']
                    else ' border-slate-100 bg-slate-50'
                )

                with ui.card().classes(card_classes):
                    with ui.row().classes('w-full items-center gap-4'):
                        ui.checkbox(
                            value=task['done'],
                            on_change=lambda e, t=task: self.toggle_task(t, e.value),
                        ).props('color=positive')

                        label_classes = 'flex-grow text-base'
                        label_classes += (
                            ' text-slate-800 font-medium'
                            if not task['done']
                            else ' text-slate-400 line-through'
                        )

                        ui.label(task['text']).classes(label_classes)

                        ui.button(
                            icon='delete',
                            on_click=lambda t=task: self.delete_task(t),
                        ).props('flat round color=negative').classes('shrink-0')

    def build(self) -> None:
        with ui.column().classes(
            'min-h-screen w-full items-center bg-gradient-to-b from-slate-50 to-slate-100 px-6 py-10'
        ):
            with ui.column().classes('w-full max-w-3xl items-center gap-6'):
                self.build_header()
                self.build_input_section()
                self.render_feedback()
                self.render_status()

                self.task_list = ui.column().classes('w-full gap-3')
                self.render_tasks()


# -------------------------
# App Startup
# -------------------------
service = TaskService()
app = TodoApp(service)
app.build()

ui.run()