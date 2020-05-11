#%%
from abstract_path_algorithm import AbstractPathAlgorithm

class ExamplePathAlgorithm(AbstractPathAlgorithm):

    def __init__(self):
        super().__init__()

        self.visited = self.visited        # Updated automatically
        self.cur_position = self.position  # Updated automatically
	self.goal = self.goal              # Fixed for you to work towards

    def find_move(self, available_pos):
        # For you to do
        return None # You need to return an element of `available_pos`
