# nicegui_layout_pattern_1.py
from nicegui import ui

with ui.column().classes('min-h-screen w-full items-center justify-center'):
    with ui.card().classes('w-full max-w-md p-6 shadow-lg'):
        ui.label('Login').classes('text-2xl font-bold')
        with ui.column().classes('gap-4'):
            ui.input('Email')
            ui.input('Password', password=True)
            ui.button('Sign In').classes('w-full')
ui.run()
