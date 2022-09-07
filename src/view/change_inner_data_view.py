"""
Change Inner Data View
"""

import tkinter as tk
import tkinter.ttk as ttk


class ChangeInnerDataView(ttk.Frame):
    """
    Change inner data view
    """

    def __init__(self, master) -> None:
        """
        Parameters
        ----------
        master : tk.Frame or ttk.Frame
            Frame object
        """
        self.master = master
        self.size = (300, 150)
        self.controller = None

        super().__init__(master, width=self.size[0], height=self.size[1])

        self.text_val = tk.StringVar(self, value='')
        self.entry = tk.Entry(self, textvariable=self.text_val)
        self.entry.pack()

        self.button = tk.Button(self, text='Submit', command=self._text_input_event)
        self.button.pack()

        self.text = tk.Label(self, text='')
        self.text.pack()


    def set_controller(self, controller) -> None:
        """Set controller

        Parameters
        ----------
        controller : Controller
            Controller in MVC
        """
        self.controller = controller
    

    # Draw method
    def change_var_text(self, text:str) -> None:
        """Change var text

        Parameters
        ----------
        text : str
            new text
        """
        self.text['text'] = text


    # Event handler (wrapper)
    def _text_input_event(self):
        text = self.entry.get()
        self.controller.text_input_impl(text)
