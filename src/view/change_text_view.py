"""
Change Text View
"""

import tkinter as tk
import tkinter.ttk as ttk


class ChangeTextView(ttk.Frame):
    """
    Change text view
    """

    def __init__(self, master):
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

        # State text
        self.state_label = tk.Label(self, text='')
        self.state_label.pack()

        # Result text (variable)
        self.label = tk.Label(self, text='Sample text')
        self.label.pack()

        # Button for changing text (result text)
        self.button_1 = tk.Button(self, text='Change text', command=self._push_button_event)
        self.button_1.pack(side=tk.LEFT)

        # Button for switching state (InitState <-> ResultState)
        self.button_2 = tk.Button(self, text='Switch state', command=self._switch_context_event)
        self.button_2.pack(side=tk.LEFT)

    def set_controller(self, controller):
        """Set controller

        Parameters
        ----------
        controller : Controller
            Controller in MVC
        """
        self.controller = controller
    
    def change_state_label(self, state_label:str) -> None:
        """Change state label

        Parameters
        ----------
        state_label : str
            State label
        """
        text = f'State: {state_label}'
        self.state_label['text'] = text

    def change_text(self, text:str) -> None:
        """Change text

        Parameters
        ----------
        text : str
            new text
        """
        self.label['text'] = text
    

    # Event handler (wrapper)
    def _push_button_event(self) -> None:
        self.controller.push_button_impl()
    
    def _switch_context_event(self) -> None:
        self.controller.switch_context_impl()