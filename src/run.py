"""
Entry Point
"""

import tkinter as tk

from model.model import Model
from view.view import View
from controller.controller import Controller

def main() -> None:
    root = tk.Tk()
    root.geometry('300x300')

    view = View(root=root)
    controller = Controller(view=view, model=Model())
    view.set_controller(controller)

    view.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
