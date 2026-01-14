"""
student
"""

from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Student:
    """
    student
    """

    name: str
    grades: List[int] = field(default_factory=list)
    graduated: bool = False
