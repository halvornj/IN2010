from typing import Generic
from typing import TypeVar
T = TypeVar('T')
class Node(Generic[T]):
    def __init__(self, element:T, left=None, right=None):
        self.element:T = element
        self.left:Node|None = left
        self.right:Node|None = right

    def __str__(self)->str:
        return str(self.element)
