"""
car
"""

from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Car:
    """
    car
    """

    brand: str
    mileage: int
    service_dates: List[str] = field(default_factory=list)

