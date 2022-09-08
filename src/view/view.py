"""
View
"""

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tk_mbox

from .change_text_view import ChangeTextView
from .change_inner_data_view import ChangeInnerDataView


class View(ttk.Frame):
    """
    View

    View in MVC model
    """
    def __init__(self, root) -> None:
        """
        Parameters
        ----------
        root: tk.Tk
            Root window
        """
        self.tk_root = root
        self.size = (300, 300)
        self.controller = None

        super().__init__(root, width=self.size[0], height=self.size[1])

        self.change_text_view = ChangeTextView(self)
        self.change_text_view.pack()

        ttk.Separator(self, orient=tk.HORIZONTAL).pack(fill=tk.BOTH, pady=10)

        self.change_inner_data_view = ChangeInnerDataView(self)
        self.change_inner_data_view.pack()

        self.exit_button = tk.Button(self, text='Exit', command=self.tk_root.destroy)
        self.exit_button.pack(pady=(50, 0))

        self.pack()
    
    def set_controller(self, controller):
        """Set controller

        Parameters
        ----------
        controller : Controller
            Controller in MVC
        """
        self.controller = controller
        self.change_text_view.set_controller(controller=controller)
        self.change_inner_data_view.set_controller(controller=controller)


    # Draw method
    def change_state_label(self, state_label:str) -> None:
        """Change state label

        Parameters
        ----------
        state_label : str
            State label
        """
        self.change_text_view.change_state_label(state_label=state_label)

    def change_text(self, text:str) -> None:
        """Change text

        Parameters
        ----------
        text : str
            new text
        """
        self.change_text_view.change_text(text=text)
    
    def change_var_text(self, text:str) -> None:
        """Change var text

        Parameters
        ----------
        text : str
            new text
        """
        self.change_inner_data_view.change_var_text(text=text)

    def alert_info(self, title:str, message:str) -> None:
        """Show info dialog

        Parameters
        ----------
        title : str
            Title of dialog
        message : str
            Info message
        """
        tk_mbox.showinfo(title=title, message=message)   

    def alert_error(self, title:str, message:str) -> None:
        """Show error dialog

        Parameters
        ----------
        title : str
            Title of dialog
        message : str
            Error message
        """
        tk_mbox.showerror(title=title, message=message)

    def alert_warning(self, title:str, message:str) -> None:
        """Show warning dialog

        Parameters
        ----------
        title : str
            Title of dialog
        message : str
            Warning message
        """
        tk_mbox.showwarning(title=title, message=message)
