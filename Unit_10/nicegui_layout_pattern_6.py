# nicegui_layout_pattern_6.py
from nicegui import ui

with ui.column().classes('max-w-3xl mx-auto p-6 gap-8'):
    with ui.card().classes('p-6'):
        ui.label('Section 1')
    with ui.card().classes('p-6'):
        ui.label('Section 2')
ui.run()
