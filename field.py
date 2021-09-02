
class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wall = True
        self.visited = False
        self.path = False

    def adjacentField(self, mymaze):
        result = []
        result.extend([mymaze.getField(i, self.y) for i in {self.x - 1, self.x + 1} if 0 <= i <= mymaze.N - 1])
        result.extend([mymaze.getField(self.x, i) for i in {self.y - 1, self.y + 1} if 0 <= i <= mymaze.M - 1])
        return result

    def unvisitedField(self, mymaze):
        return [i for i in self.adjacentField(mymaze) if i.visited == False]

    def adjacentOpen(self, mymaze):
        return [i for i in self.adjacentField(mymaze) if i.wall == False]

    def isPath(self, mymaze):
        return ((len(self.adjacentOpen(mymaze)) <= 1) or (
                (len(self.adjacentOpen(mymaze)) == 2) and (mymaze.escape in self.adjacentOpen(mymaze)) and len(
            mymaze.escape.adjacentOpen(mymaze)) == 0))

    def __repr__(self):
        if self.path:
            return "^"
        if self.visited:
            if self.wall:
                return "X"
            else:
                return "O"
        else:
            if self.wall:
                return "x"
            else:
                return "o"
