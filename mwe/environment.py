from typing import List
from data import Action, Observation
import drawSvg as draw
import random


class Environment:
    def __init__(self):
        self._board_size = 5
        self._agent_pos = (0, 0)
        self._colours = {
            "agent": "#ff0000ff",
            "wall": "#333333ff",
            "air": "#ffffffff"
        }
        self._board = [
            '#', '.', '#', '#', '#',
            '.', '.', '#', '.', '#',
            '#', '.', '#', '.', '#',
            '#', '.', '.', '.', '.',
            '.', '.', '#', '#', '#'
        ]


    def reset(self) -> Observation:
        # todo
        return Observation([0.0])
        

    def update(self, act: Action) -> Observation:
        # todo
        return Observation([0.0])
        

    def draw(self) -> None:
        drawing_size = 400
        tile_size = drawing_size / self._board_size

        d = draw.Drawing(drawing_size, drawing_size)

        for x in range(self._board_size):
            for y in range(self._board_size):
                idx = (self._board_size - y - 1) * self._board_size + x
                tile = self._board[idx]
                
                stroke_width = 0

                if (x, y) == self._agent_pos:
                    col = self._colours["agent"]
                elif tile == '#':
                    col = self._colours["wall"]
                    stroke_width = 1
                else:
                    col = self._colours["air"]
                
                r = draw.Rectangle(x * tile_size, y * tile_size, tile_size, tile_size, fill=col, stroke_width=stroke_width, stroke='black')
                d.append(r)

        d.saveSvg('environment.svg')
