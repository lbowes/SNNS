from typing import List
from data import Action, Observation


class Environment:
    def __init__(self):
        pass

    def reset(self) -> Observation:
        # todo
        return Observation([0.0])
        

    def update(self, act: Action) -> Observation:
        # todo
        return Observation([0.0])
