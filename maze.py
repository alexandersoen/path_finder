import csv

# 's' for start of maze
# 'e' for end of maze
# 'w' for wall

class Maze:
    
    def __init__(self, layout):

        if type(layout) == str:
            layout = load_from_file(layout)

        self.start = [pos for (pos, v) in layout.items() if v == 's'][0]  # Maybe I should fix something here
        self.end = [pos for (pos, v) in layout.items() if v == 'e'][0]

        all_pos = layout.keys()
        self.dimensions = tuple(map(lambda x: max(x) + 1, zip(*all_pos)))

        # Format maze layout
        self.layout = dict()
        for pos, cost in layout.items():
            if cost in ['s', 'e']:
                self.layout[pos] = 0
            elif cost == 'w':
                continue
            else:
                self.layout[pos] = float(cost)

    def __getitem__(self, pos):
        if pos not in self.layout:
            return None
        else:
            return self.layout[pos]

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def get_avail_moves(self, cur_pos):
        avail_moves = dict()
        for pos in get_adjacent(*cur_pos):
            # Check for walls
            if self[pos] is None:
                continue

            avail_moves[pos] = self[pos]

        return avail_moves


def load_from_file(f_loc):

    layout = dict()
    with open(f_loc, 'r') as f:
        reader = csv.reader(f)
        for j, row in enumerate(reader):
            for i, v in enumerate(row):
                layout[(i, j)] = v.strip()

    return layout

def get_adjacent(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    #return [(i, j) for (i, j) in product(range(x-1, x+2), range(y-1, y+2)) if (x, y) != (i, j)]