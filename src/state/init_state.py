"""
InitState
"""

import random

import state.result_state
from .base import StateBase


class InitState(StateBase):
    """
    InitState

    Initial state of App
    """

    def __init__(self, controller, view, context) -> None:
        """
        Parameters
        ----------
        controller : Controller
            Controller in MVC
        view : View
            View in MVC
        context : Context
            Application context object
        """
        super().__init__(controller=controller, view=view, context=context)
    
    def __repr__(self) -> str:
        return 'InitState'
    
    def push_button(self) -> bool:
        """implementation of push button event

        Returns
        -------
        bool
            if success return True, otherwise return False
        """
        text = str(random.randint(0, 1024))
        self.view.change_text(text)
        return True
    
    def switch_context(self) -> bool:
        """implementation of switch_context_event

        Returns
        -------
        bool
            if success return True, otherwise return False
        """
        next_state = state.result_state.ResultState(
            controller=self.controller,
            view=self.view,
            context=self.context
        )
        self.context.change_state(state=next_state)
        self.view.change_state_label(str(next_state))

        return True
