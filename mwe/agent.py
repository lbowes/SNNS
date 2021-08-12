from typing import List, Tuple
from data import Action, Observation
import drawSvg as draw
import networkx as nx
import random


class Agent:
    def __init__(self):
        self._network = nx.Graph()
        self._num_nodes = 100

        self._build_network()


    def _build_network(self):
        r = lambda: random.random()

        # Add nodes with random positions and activations
        for n in range(self._num_nodes):
            rand_pos = (r(), r())
            rand_act = r()

            self._network.add_node(n, position=rand_pos, activation=rand_act)

        # Randomly add connections between nodes
        p_connect = 0.06
        
        for src in range(self._num_nodes):
            for dest in range(self._num_nodes):
                should_connect = r() < p_connect

                if should_connect:
                    rand_weight = r()
                    self._network.add_edge(src, dest, weight=rand_weight)
        

    def update(self, obs: Observation) -> Action:
        # todo
        return Action([0.0])


    def _pos_img(self, pos_net, size_img) -> Tuple[float]:
        return tuple(size_img * x for x in pos_net)


    def _brightness_hex(self, val: float) -> str:
        return '#%02X%02X%02Xff' % (val, val, val)


    def draw(self) -> None:
        drawing_size = 400
        node_scale = 0.02
        size = drawing_size * node_scale

        d = draw.Drawing(drawing_size, drawing_size)

        position_net = nx.get_node_attributes(self._network, "position")
        activation = nx.get_node_attributes(self._network, "activation")
        weight = nx.get_edge_attributes(self._network, "weight")

        # Draw connections
        for src, dest, data in self._network.edges(data=True):
            start = self._pos_img(position_net[src], drawing_size)
            end = self._pos_img(position_net[dest], drawing_size)

            weight = int(data['weight'] * 255)

            col = self._brightness_hex(weight)
            line = draw.Line(start[0], start[1], end[0], end[1], stroke_width=1, stroke=col)
            d.append(line)

        # Draw nodes
        for i in range(self._num_nodes):
            p = self._pos_img(position_net[i], drawing_size)
            act = int(activation[i] * 255)

            col = self._brightness_hex(act)
            circle = draw.Circle(p[0], p[1], size, fill=col, stroke_width=1, stroke='black')
            d.append(circle)

        d.saveSvg('network.svg')
