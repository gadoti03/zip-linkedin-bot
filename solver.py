import copy

class OrderedSet:
    def __init__(self, i=None, j=None):
        self.data = {}
        self.order = []
        if i is not None and j is not None:
            self.add((i, j))

    def add(self, x):
        if x not in self.data:
            self.data[x] = True
            self.order.append(x)

    def pop(self):
        if not self.order:
            raise KeyError("set is empty")
        x = self.order.pop()
        del self.data[x]
        return x
    
    def get(self):
        return self.order

    def __contains__(self, x):
        return x in self.data

    def __iter__(self):
        return iter(self.order)
    
    def __len__(self):
        return len(self.order)
    
def get_starting_coords(grid):
    if grid is None:
        return None
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return i, j

def get_neighbors(i, j, n_rows, n_cols, visited):
    directions = [(-1,0), (1,0), (0,-1), (0,1)] 
    neighbors = []

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n_rows and 0 <= nj < n_cols and (ni,nj) not in visited:
            neighbors.append((ni, nj))
    
    return neighbors

def get_moves(path):
    def diff(a, b):
        return (b[0] - a[0], b[1] - a[1])

    moves = []
    for i in range(1, len(path)):
        if diff(path[i], path[i-1]) == (0, -1):
            moves.append("right")
        if diff(path[i], path[i-1]) == (-1, 0):
            moves.append("down")
        if diff(path[i], path[i-1]) == (0, 1):
            moves.append("left")
        if diff(path[i], path[i-1]) == (1, 0):
            moves.append("up")
    return moves

def solve(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])

    n_numbers = sum(1 for row in grid for v in row if v is not None)
    
    # get for start_i, start_j
    start_i, start_j = get_starting_coords(grid)

    visited_cells = OrderedSet(start_i, start_j)
    read_numbers = []
    if grid[start_i][start_j] is not None:
        read_numbers.append(grid[start_i][start_j])

    res = []

    def backtracking(i, j):
        nonlocal res

        if len(visited_cells) == n_rows*n_cols and len(read_numbers) == n_numbers:
            res = copy.deepcopy(visited_cells.get())
            return True  # stop at first solution
        elif len(read_numbers) == n_numbers:
            return False

        for mov in get_neighbors(i, j, n_rows, n_cols, visited_cells):
            visited_cells.add(mov)
            val = grid[mov[0]][mov[1]]
            added_number = False
            if val is not None:
                if not read_numbers or val == read_numbers[-1] + 1:
                    read_numbers.append(val)
                    added_number = True
                else:
                    visited_cells.pop()
                    continue

            if backtracking(mov[0], mov[1]):
                return True

            visited_cells.pop()
            if added_number:
                read_numbers.pop()
        return False

    backtracking(start_i, start_j)
    return get_moves(res)
