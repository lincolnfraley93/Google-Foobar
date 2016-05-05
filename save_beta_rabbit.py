def answer(food,grid):
    length=len(grid)-1

    def decorator(remainder):
        prev_room={}
        def helper(*args):
            if args in prev_room:
                return prev_room[args]
            else:
                prev_room[args]=remainder(*args)
                return prev_room[args]
        return helper

    @decorator
    def remainder(current,i,j):
        if i>length or j>length:
            return food+1
        else:
            current-=grid[i][j]
            if current<0:
                return food+1
            elif i==length and j==length:
                return current
            else:
                return min(remainder(current,i+1,j),remainder(current,i,j+1))

    remainder=remainder(food,0,0)
    return remainder if remainder<=food else -1


