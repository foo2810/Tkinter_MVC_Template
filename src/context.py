"""
Context
"""

from typing import Any

from state.base import StateBase


class Context:
    """
    Context
    """

    def __init__(self) -> None:
        self.state = None

        self.data = dict()
        self.transactions = list()
    
    # methods for state
    def get_current_state(self) -> StateBase:
        """Return current state

        Returns
        -------
        StateBase
            state object
        """

        return self.state

    def change_state(self, state:StateBase) -> None:
        """Change state

        Parameters
        ----------
        state : StateBase
            state object set to context
        """
        self.state = state
    
    # methods for data
    def register(self, key:str, obj:Any):
        """Register object (staging)

        Parameters
        ----------
        key : str
            kye
        obj : Any
            registered obejct

        See Also
        --------
        This method stages registering object. 
        To complete registration, you must call `commit` method.
        """
        self.transactions += [{'op': 'register', 'key': key, 'obj': obj}]

        return self

    def get(self, key:str) -> Any:
        """Return data

        Parameters
        ----------
        key : str
            key corresponded object

        Returns
        -------
        Any
            corresponding object

        Raises
        ------
        KeyError
            Raise this exception, if key is not found
        """
        if key not in self.data:
            raise KeyError(str(key))
        
        return self.data[key]
    
    def update(self, key:str, obj:Any):
        """Update object (staging)

        Parameters
        ----------
        key : str
            key
        obj : Any
            New object
        
        Returns
        -------
        Self

        Raises
        ------
        KeyError
            Raise this exception, if key is not found
        
        See Also
        --------
        This method stages updating object. To complete updating, you must call `commit` method.
        """
        if key not in self.data:
            raise KeyError(str(key))
        
        self.transactions += [{'op': 'update', 'key': key, 'obj': obj}]

        return self
    
    def delete(self, key:str):
        """Delete object (staging)

        Parameters
        ----------
        key : str
            key

        Returns
        -------
        Self
        """
        self.transactions += [{'op': 'delete', 'key': key, 'obj': None}]

        return self
    
    def commit(self) -> None:
        """Complete updating

        Raises
        ------
        RuntimeError
        """
        for transaction in self.transactions:
            op = transaction['op']
            if op == 'register' or op == 'update':
                self.data[transaction['key']] = transaction['obj']
            elif op == 'delete':
                del self.data[transaction['key']]
            else:
                raise RuntimeError(f'Operation, "{op}" unknown')

        self.transactions = list()
    
    def rollback(self) -> None:
        """Rollback updating
        """
        self.transactions = list()

