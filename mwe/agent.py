from data import Action, Observation
from network import Network


class Agent:
    def __init__(self):
        self._network = Network()

        
    def update(self, obs: Observation) -> Action:
        # todo
        self._network.update()

        return Action([0.0])


    def draw(self):
        self._network.draw()
