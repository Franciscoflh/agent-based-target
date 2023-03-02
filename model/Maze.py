class Maze:
    def __init__(self, start_pos, end_pos, maze):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.maze = [[max(0, x) for x in row] for row in maze]

    def is_valid_position(self, pos):
        row, col = pos
        return 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0]) and self.maze[row][col] == 0

    def get_reward(self, pos):
        return 1 if pos == self.end_pos else 0
