from typing import List
from data import Action, Observation
import drawSvg as draw
import random


def rand_hex_col() -> str:
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X%02X' % (r(), r(), r(), 255)


class Environment:
    def __init__(self):
        self._size = 5
        self._board = [
            '#', '.', '#', '#', '#',
            '#', '.', '#', '.', '#',
            '#', '.', '#', '.', '#',
            '#', '.', '.', '.', '.',
            '#', '.', '#', '#', '#'
        ]

    def reset(self) -> Observation:
        # todo
        return Observation([0.0])
        

    def update(self, act: Action) -> Observation:
        # todo
        return Observation([0.0])
        

    def draw(self) -> None:
        drawing_size = 200
        tile_size = drawing_size / self._size

        d = draw.Drawing(drawing_size, drawing_size)

        for x in range(self._size):
            for y in range(self._size):
                idx = (self._size - y - 1) * self._size + x
                tile = self._board[idx]
                
                col = rand_hex_col() if tile == '#' else "#00000000"
                r = draw.Rectangle(x * tile_size, y * tile_size, tile_size, tile_size, fill=col)
                d.append(r)

        d.saveSvg('example.svg')

        # todo
        return Observation([0.0])
