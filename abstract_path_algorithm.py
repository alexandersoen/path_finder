from abc import ABC, abstractmethod

class AbstractPathAlgorithm(ABC):

    def __init__(self):
        self.visited = []
        self.cur_position = None
        self.goal = None
        self.maze = None

        super().__init__()

    def set_maze(self, maze):
        self.maze = maze

    #def reset(self, start_pos, end_pos):
    def reset(self, maze):
        start_pos = maze.get_start()
        end_pos = maze.get_end()
        self.visited = [start_pos]
        self.cur_position = start_pos
        self.goal = end_pos
        self.maze = maze

    @abstractmethod
    def find_move(self, available_pos):
        pass

    def move(self, pos):
        self.cur_position = pos
        self.visited.append(pos)

    def get_avail_moves(self, cur_pos):
        return self.maze.get_avail_moves(cur_pos)