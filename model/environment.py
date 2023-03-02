from Maze import Maze
from typing import Tuple


class MyEnvironment:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.agent_pos = maze.start_pos
        self.goal_pos = maze.end_pos

    def is_valid_position(self, pos: Tuple[int, int]) -> bool:
        return self.maze.is_valid_position(pos)

    def get_reward(self, pos: Tuple[int, int]) -> int:
        return self.maze.get_reward(pos)

    def perform_action(self, agent_pos: Tuple[int, int], action: Tuple[int, int]) -> Tuple[Tuple[int, int], int]:
        # Calcula a nova posição do agente com base na ação escolhida
        new_agent_pos = (agent_pos[0] + action[0], agent_pos[1] + action[1])

        # Verifica se a nova posição é válida e atualiza a posição do agente
        if self.is_valid_position(new_agent_pos):
            self.agent_pos = new_agent_pos

        # Calcula a recompensa associada à nova posição
        reward = self.get_reward(self.agent_pos)

        return new_agent_pos, reward
