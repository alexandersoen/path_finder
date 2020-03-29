from abc import ABC, abstractmethod

class AbstractPathAlgorithm(ABC):

    def __init__(self):
        self.visited = []
        self.cur_position = None
        self.goal = None

        super().__init__()

    def reset(self, start_pos, end_pos):
        self.visited = [start_pos]
        self.cur_position = start_pos
        self.goal = end_pos

    @abstractmethod
    def find_move(self, available_pos):
        pass

    def move(self, pos):
        self.cur_position = pos
        self.visited.append(pos)