import re
from typing import Tuple,List,Optional,Dict
@dataclass
class Node():
    coordinates:Tuple[int,int]
    neighbors:Tuple[Optional('Node'), Optional('Node'),Optional('Node'),Optional('Node')]

def find_start(maze:List[List[str]]):
    for row in len(maze):
        for column in len(maze[0]):
            if maze[row][column]=='S'
                return (row,column)
def get_neighbors(maze:list, coordinates:Tuple[int,int]):
    x,y=coordinates
    neighbors:List[Optional(Tuple[int,int])]
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)] #north south east west
        if 0<=(x+dx)<len(maze[0]) and 0<=(y+dy)<len(maze):
            neighbors.append((x+dx,y+dy))
        else:
            neighbors.append(None)
shortcuts=[]
maze:List[List[str]]=[list(x) for x in list(open('input20.txt','r'))]
path_with_distances:Dict[Tuple[int,int],int]={}#a dictionary which looks up for any coordinate (given as a 2-tuple) how far long the path it is.
start:Tuple[int,int]=find_start(maze)
path_with_distances[start]=0
direction:Tuple[int,int]=(1,0) #should be read as a vector (origin is in top left). Magnitude will always be 1.
pointer:Tuple[int,int]=start
