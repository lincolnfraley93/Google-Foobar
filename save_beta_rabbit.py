from functools import wraps

def answer(food, grid):
    
    @memoized
    def r(t, i, j):
        
        t -= grid[i][j]
        if i < 0 or j < 0 or t < 0:
            return food + 1
        elif i == j == 0:
            return t
        else:
            return min(r(t, i - 1, j), r(t, i, j - 1))

    remainder = r(food, len(grid) - 1, len(grid) - 1)
    return remainder if remainder <= food else -1

def memoized(f):
    cache = {}
    #@wraps(f)
    def wrapped(*args):
        try:
            result = cache[args]
        except KeyError:
            result = cache[args] = f(*args)
        return result
    return wrapped


