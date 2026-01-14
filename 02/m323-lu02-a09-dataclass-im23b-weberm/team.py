"""
team
"""
from dataclasses import dataclass, field


@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)
