from datetime import datetime
from itertools import product

class PathFinder:

    def __init__(self, maze, algorithm):
        self.maze = maze
        self.algorithm = algorithm

        self.reset()

    def reset(self):
        self.history = list()
        self.cost = 0

        self.algorithm.reset(self.maze.get_start(), self.maze.get_end())
        self.cur_position = self.algorithm.cur_position
        self.end_position = self.maze.get_end()

    def step_path_finder(self):

        if self.is_finished():
            return None

        avail_moves = dict()
        for pos in get_adjacent(*self.cur_position):
            # Check for walls
            if self.maze[pos] is None:
                continue

            avail_moves[pos] = self.maze[pos]

        start_time = datetime.now()
        next_move = self.algorithm.find_move(avail_moves)  # Find next move
        end_time = datetime.now()

        time_taken = (start_time - end_time).total_seconds()

        if next_move is None:
            raise Exception('No valid move')

        # Make sure that the move is valid
        try:
            cost = avail_moves[next_move]
        except KeyError:
            raise Exception('Next position given does is not valid')

        # Current cost
        print(cost)
        self.cost += cost

        # Timing book keeping
        self.history.append((time_taken, self.cur_position, next_move, cost))

        # Actually update positions
        self.algorithm.move(next_move)
        self.cur_position = next_move
        return next_move

    def get_current_position(self):
        return self.cur_position

    def get_current_cost(self):
        return self.cost

    def get_current_history(self):
        return self.history

    def is_finished(self):
        return self.cur_position == self.end_position
    
    def get_maze(self):
        return self.maze

    def get_algorithm(self):
        return self.algorithm

    def solve(self):
        i = 1
        while not self.is_finished():
            self.step_path_finder()
            print('Step: {}, Time: {:.2f}, From: {}, To: {}, Cost: {}'.format(i, *self.history[-1]))
            i += 1

def get_adjacent(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    #return [(i, j) for (i, j) in product(range(x-1, x+2), range(y-1, y+2)) if (x, y) != (i, j)]