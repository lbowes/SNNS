from typing import List
from data import Action, Observation
import drawSvg as draw
import networkx as nx
import random


class Agent:
    def __init__(self):
        self._network = nx.Graph()
        self._num_nodes = 50

        self._build_network()


    def _build_network(self):
        r = lambda: random.random()

        for n in range(self._num_nodes):
            rand_pos = (r(), r())
            rand_act = r()

            self._network.add_node(n, position=rand_pos, activation=rand_act)


    def update(self, obs: Observation) -> Action:
        # todo
        return Action([0.0])


    def draw(self) -> None:
        drawing_size = 200
        node_scale = 0.03
        size = drawing_size * node_scale

        d = draw.Drawing(drawing_size, drawing_size)

        position = nx.get_node_attributes(self._network, "position")
        activation = nx.get_node_attributes(self._network, "activation")

        for i in range(self._num_nodes):
            p = tuple(drawing_size * x for x in position[i])
            act = int(activation[i] * 255)

            col = '#%02X%02X%02Xff' % (act, act, act)
            d.append(draw.Circle(p[0], p[1], size, fill=col, stroke_width=1, stroke='black'))

        d.saveSvg('network.svg')
