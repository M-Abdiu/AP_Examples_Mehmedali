# nicegui_layout_pattern_7.py

from nicegui import ui

with ui.header():
    ui.label('App Header')

with ui.row().classes('w-full no-wrap').style('height: calc(100vh - 64px);'):
    with ui.column().classes('w-64 p-4 bg-gray-100'):
        ui.label('Sidebar')

    with ui.column().classes('flex-grow p-4'):
        ui.label('Main Content')

ui.run()