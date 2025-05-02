from typing import Any, Tuple


class MaxHeap:
    def __init__(self, contents=None, value=None):
        self.value: float = value
        self.contents: Any = contents
        self.left: MaxHeap = None  # the smaller one
        self.right: MaxHeap = None  # the bigger one

    def push(self, contents: Any, value: float) -> None:
        if self.value is None:
            self.value = value
            self.contents = contents

        elif value <= self.value:
            if self.left is None:
                self.left = MaxHeap(contents, value)

            else:
                self.left.push(contents, value)

        elif value > self.value:
            if self.right is None:
                self.right = MaxHeap(contents, value)

            else:
                self.right.push(contents, value)

        else:
            raise ValueError("WTF DID YOU DO???????????")

    def pop(self) -> Any:
        if self.right is None:

            if self.left is None:
                self.value = None
                return self.contents

            return self.left.pop()
        return self.right.pop()

    def __repr__(self):
        out = ""
        if self.left is not None:
            out += str(self.left)+', '
        out += str(self.contents)
        if self.right is not None:
            out += ", "+str(self.right)
        return out

    def __iter__(self):
        out = []
        if self.left is not None:
            out += list(self.left)

        out.append(self.contents)

        if self.right is not None:
            out += list(self.right)

        return iter(out)

class MinHeap(MaxHeap):
    def push(self, contents, value):
        super().push(self, contents, -value)


def DepthFirstSearch(structure: any, start: any, end: any, queue=list) -> list:  # equivalent to DFS
    curr = start
    visited = []
    while curr != end:
        curr = queue.pop()
        for node in structure.GetNeighbors(curr):
            if node not in visited:
                queue.push(node)


def PrintProgress(structure: any, current, visited, queue, end):
    grid = [["."]*structure.width for _ in range(structure.height)]
    grid[current[0]][current[1]] = '$'
    grid[end[0]][end[1]] = '*'
    for node in queue:
        grid[node[0]][node[1]] = '@'
    for node in visited:
        grid[node[0]][node[1]] = '#'
    for line in grid:
        print("".join(line))


def PrintPath(structure: any, visited):
    grid = [["."]*structure.width for _ in range(structure.height)]
    for node in visited:
        grid[node[0]][node[1]] = '#'
    for line in grid:
        print("".join(line))

def GreedySearch(structure: any, start: any, end: any) -> list:  # I couldn't figure out a way to get this to run Search(). Skill issue ig
    curr = start
    visited = []
    queue = MaxHeap()
    push = lambda x: queue.push(x, -structure.GetDistance(x, end))
    push(curr)

    while curr != end:

        #PrintProgress(structure, curr, visited, queue, end)
        curr = queue.pop()
        visited.append(curr)
        for node in structure.GetNeighbors(curr):
            if node not in visited:
                push(node)
    PrintPath(structure, visited)
    return visited


class Grid:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height

    def GetNeighbors(self, node: Tuple[int, int]):
        """returns a list of coordinates for the x,y of up,down,left,right"""
        out = []
        if node[0] > 0:
            out.append((node[0]-1, node[1]))
        if node[0] < self.width:  # feels like this should be self.width-1 but I will trust my gut
            out.append((node[0]+1, node[1]))

        if node[1] > 0:
            out.append((node[0], node[1]-1))
        if node[1] < self.height:
            out.append((node[0], node[1]+1))
        return out

    def GetDistance(self, start: Tuple[int, int], end: Tuple[int, int]):
        return (((end[0]-start[0])**2) + ((end[1]-start[1])**2))**.5


if __name__ == "__main__":
    datGriddy = Grid(20, 20)
    print(len(GreedySearch(datGriddy, (0, 0), (10, 10))))
