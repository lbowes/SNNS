from typing import List
from dataclasses import dataclass


@dataclass
class Action:
    state: List[float]


@dataclass
class Observation:
    state: List[float]
