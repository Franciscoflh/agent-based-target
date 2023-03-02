from typing import List, Tuple
import random


class MyGoal:
    def __init__(self):
        self.actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def choose_action(self) -> Tuple[int, int]:
        return random.choice(self.actions)
