#%%
import pygame

#%%
class Visualiser:

    def __init__(self, display_width, display_height):

        self.X_BORDER_RATIO = 0.05 * 2
        self.Y_BORDER_RATIO = 0.05 * 2

        self.X_BORDER = display_width * self.X_BORDER_RATIO / 2
        self.Y_BORDER = display_height * self.Y_BORDER_RATIO / 2

        self.X_SIZE = display_width
        self.Y_SIZE = display_height

        self.Y_CONTROL_RATIO = 0.2

        pygame.init()
        self.display = pygame.display.set_mode((display_width, display_height))

        self.clock = pygame.time.Clock()
        self.crashed = False

        self.maze = None
        self.algorithm = None
        self.path_finder = None

    def load_path_finder(self, path_finder):
        self.maze = path_finder.maze
        self.algorithm = path_finder.algorithm
        self.path_finder = path_finder

        self.maze_x_size, self.maze_y_size = self.maze.dimensions

        x_space = (self.X_SIZE - self.X_BORDER * 2) / self.maze_x_size
        y_space = (self.Y_SIZE * (1 - self.Y_CONTROL_RATIO) - self.Y_BORDER * 2) / self.maze_y_size

        element_space = min(x_space, y_space)

        self.element_border = element_space * 0.1
        self.element_size = element_space * 0.8

    def draw_maze(self):

        colours = {'wall': (50, 50, 50), 'path': (250, 250, 250)}

        for i in range(self.maze_x_size):
            for j in range(self.maze_y_size):
                x = (self.element_size + self.element_border * 2) * i + self.element_border + self.X_BORDER
                y = (self.element_size + self.element_border * 2) * j + self.element_border + self.Y_BORDER

                if (i, j) in self.maze.layout:
                    colour = colours['path']
                else:
                    colour = colours['wall']

                pygame.draw.rect(self.display, colour, [x, y, self.element_size, self.element_size])

    def draw_player(self):

        cur_x, cur_y = self.path_finder.cur_position

        cur_x = int((self.element_size + self.element_border * 2) * (cur_x + 0.5) + self.X_BORDER)
        cur_y = int((self.element_size + self.element_border * 2) * (cur_y + 0.5) + self.Y_BORDER)
        size = int(self.element_size * 0.4)

        pygame.draw.circle(self.display, (0, 255, 0), [cur_x, cur_y], size)

    def main_loop(self, tick_rate=60):

        while not self.crashed:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.crashed = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.path_finder.step_path_finder()
                    if event.key == pygame.K_r:
                        self.path_finder.reset()

                print(event)

                self.draw_maze()
                self.draw_player()

                pygame.display.update()
                self.clock.tick(tick_rate)


#%%
if __name__ == "__main__":
    from maze import Maze
    from greedy_path_algorithm import GreedyPathAlgorithm
    from path_finder import PathFinder

    maze = Maze('example_maze_1.csv')
    algorithm = GreedyPathAlgorithm()
    path_finder = PathFinder(maze, algorithm)

    vis = Visualiser(800, 600)
    vis.load_path_finder(path_finder)
    vis.main_loop()