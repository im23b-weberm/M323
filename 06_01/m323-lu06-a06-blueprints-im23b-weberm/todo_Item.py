"""
todoitem
"""
from dataclasses import dataclass

"""
todoitem
"""
@dataclass
class TodoItem:
    item_id: int
    title: str
    is_completed: bool
