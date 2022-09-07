"""
Controller
"""

from state.init_state import InitState

from context import Context


class Controller:
    """
    Controller

    Controller in MVC model
    """

    def __init__(self, view, model) -> None:
        """
        Parameters
        ----------
        view : View
            View in MVC
        """
        self.view = view
        self.model = model
        self.context = Context()

        # Configure initial state
        state = InitState(controller=self, view=view, context=self.context)
        self.context.change_state(state)
        self.view.change_state_label(str(state))

        # Initialize text in change_var_text_view
        init_str = 'Please input text'
        self.context.register('text', init_str).commit()
        self.view.change_var_text(text=init_str)

    def push_button_impl(self) -> bool:
        """Callback of push button event

        Returns
        -------
        bool
            if success return True, otherwise return False
        """
        state = self.context.get_current_state()
        return state.push_button()
    
    def switch_context_impl(self) -> bool:
        """Callback of switch context event

        Returns
        -------
        bool
            if success return True, otherwise return False
        """
        state = self.context.get_current_state()
        return state.switch_context()
    
    def text_input_impl(self, text:str) -> bool:
        """Callback of text input event

        Parameters
        ----------
        text : str
            input text

        Returns
        -------
        bool
            if success return True, otherwise return False
        """

        self.context.update('text', text)

        if len(text) < 5 or len(text) > 25:
            self.context.rollback()
            self.view.change_var_text(
                text=self.context.get(key='text')
            )
            self.view.alert_error(title='Error', message='text is invalid')
            return False
        
        self.context.commit()
        self.view.change_var_text(
            text=self.context.get(key='text')
        )
        self.view.alert_info(title='Info', message='Success!!')

        return True
