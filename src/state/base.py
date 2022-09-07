"""
StateBase

Base class of state
"""

import abc


class StateBase(abc.ABC):
    """
    StateBase

    Base class of app state
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
        super().__init__()

        self.controller = controller
        self.view = view
        self.context = context
    
    @abc.abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError
    
    @abc.abstractmethod
    def push_button(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def switch_context(self) -> bool:
        raise NotImplementedError
