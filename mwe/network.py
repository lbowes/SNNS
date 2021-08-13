from typing import List, Tuple
import networkx as nx
import random
import drawSvg as draw


class Network:
    def __init__(self):
        self._node_count = {
            "input": 4,
            "hidden": 10, 
            "output": 20
        }

        self._network = nx.Graph()
        self._build()


    def update(self):
        # todo: responsible for one update cycle
        pass


    def _synaptic_update(self, src_node, edge, dest_node):
        # todo: responsible for performing an update
        pass


    def _build(self):
        r = lambda: random.random()
        pad = 0.1 # Vertical space at the top and bottom of the graph

        # Add input nodes
        num_inputs = self._node_count["input"]
        for inp in range(num_inputs):
            pos = (pad, pad + (inp / (num_inputs - 1)) * (1 - 2 * pad))
            rand_act = r()
            self._network.add_node(inp, position=pos, activation=rand_act)

        # Add output nodes
        num_outputs = self._node_count["output"]
        for output in range(num_outputs):
            pos = (1.0 - pad, pad + (output / (num_outputs - 1)) * (1 - 2 * pad))
            rand_act = r()
            self._network.add_node(num_inputs + output, position=pos, activation=rand_act)
        
        # Add nodes with random positions and activations
       # for n in range(self._num_nodes):
       #     rand_pos = (r(), r())
       #     rand_act = r()

       #     self._network.add_node(n, position=rand_pos, activation=rand_act)

       # # Randomly add connections between nodes
       # p_connect = 0.06
       # 
       # for src in range(self._num_nodes):
       #     for dest in range(self._num_nodes):
       #         should_connect = r() < p_connect

       #         if should_connect:
       #             rand_weight = r()
       #             self._network.add_edge(src, dest, weight=rand_weight)


    def _pos_canvas(self, pos_net, size_canvas) -> Tuple[float]:
        return tuple(size_canvas * x for x in pos_net)


    def _brightness_hex(self, val: float) -> str:
        return '#%02X%02X%02Xff' % (val, val, val)


    def draw(self) -> None:
        canvas_size = 400

        d = draw.Drawing(canvas_size, canvas_size)

        position_net = nx.get_node_attributes(self._network, "position")
        activation = nx.get_node_attributes(self._network, "activation")
        weight = nx.get_edge_attributes(self._network, "weight")

        # Draw connections
       # for src, dest, data in self._network.edges(data=True):
       #     start = self._pos_canvas(position_net[src], canvas_size)
       #     end = self._pos_canvas(position_net[dest], canvas_size)

       #     weight = int(data['weight'] * 255)

       #     col = self._brightness_hex(weight)
       #     line = draw.Line(start[0], start[1], end[0], end[1], stroke_width=1, stroke=col)
       #     d.append(line)

        # Draw nodes
       # for i in range(self._num_nodes):
       #     p = self._pos_canvas(position_net[i], canvas_size)
       #     act = int(activation[i] * 255)

       #     col = self._brightness_hex(act)
       #     node = draw.Circle(p[0], p[1], size, fill=col, stroke_width=1, stroke='black')
       #     d.append(node)

        # Draw inputs
        for i in range(self._node_count["input"]):
            idx = self._node_idx("input", i)
            pos = self._pos_canvas(position_net[idx], canvas_size)
            act = int(activation[idx] * 255)
            col = self._brightness_hex(act)

            node = self._draw_node(pos, col, canvas_size)
            d.append(node)

        # Draw outputs
        for out in range(self._node_count["output"]):
            idx = self._node_idx("output", out)
            pos = self._pos_canvas(position_net[idx], canvas_size)
            act = int(activation[idx] * 255)
            col = self._brightness_hex(act)

            node = self._draw_node(pos, col, canvas_size)
            d.append(node)

        d.saveSvg('network.svg')


    def _node_idx(self, node_type: str, node_num: int) -> int:
        output_idx = node_num

        if node_type == "output":
            output_idx += self._node_count["input"] 

        return output_idx


    def _draw_node(self, pos: Tuple[float, float], col: str, canvas_size: int):
        node_scale = 0.02
        size = canvas_size * node_scale
        node = draw.Circle(pos[0], pos[1], size, fill=col, stroke_width=1, stroke='black')

        return node
