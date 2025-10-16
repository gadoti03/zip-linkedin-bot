import copy

### CLASSES ##########

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

    def __str__(self):
        return "OrderedSet([" + ", ".join(repr(x) for x in self.order) + "])"

    def __repr__(self):
        return f"OrderedSet({self.order})"
    
### FUNCTIONS ##########

def get_neighbors(i, j, n_rows, n_cols, visited):
    directions = [(-1,0), (1,0), (0,-1), (0,1)] 
    neighbors = []

    for di, dj in directions:
        ni, nj = i + di, j + dj

        if 0 <= ni < n_rows and 0 <= nj < n_cols and (ni,nj) not in visited:
            neighbors.append((ni, nj))

    print(neighbors)
    
    return neighbors

# GLOBAL VARIABLES

# I have set:
# init_i, init_j
# n_numbers
# grid

init_i, init_j = 0, 1
res = []
n_numbers = 4
# n_numbers = 2
grid = [[None, 1, None, 2], [None, None, None, None], [4, None, None, 3], [None, None, None, None]]
# grid = [[1, 2], [None, None]]
n_rows = len(grid)
n_cols = len(grid[0])

read_numbers = [1]
visited_cells = OrderedSet(init_i, init_j)

# BACKTRACKING

def backtracking(i, j):
    if len(visited_cells) == n_rows*n_cols and len(read_numbers) == n_numbers:
        
        global res
        # deposit the solution in res
        res = copy.deepcopy(visited_cells.get()) # in this way I accept just a solution
        # insted of make a deepcopy i could think of:
        # stop at the first result
        # or
        # gather all the results (adding them in a list)
        return
    elif len(read_numbers)  == n_numbers:
        return
    
    # compute the list of movements
    for mov in get_neighbors(i, j, n_rows, n_cols, visited_cells):

        # changes
        visited_cells.add(mov)
        val = grid[mov[0]][mov[1]]
        if val is None:
            pass
        elif (not read_numbers) or (grid[mov[0]][mov[1]] == read_numbers[-1] + 1):
            read_numbers.append(grid[mov[0]][mov[1]])
        else:
            visited_cells.pop()
            continue

        # recursive backtracking
        backtracking(mov[0], mov[1])

        # corrections
        visited_cells.pop()
        if (val is not None and val == read_numbers[-1]):
            read_numbers.pop()

backtracking(init_i, init_j)
print(res)