extends Node2D
GRID_WIDTH:int=200
GRID_HEIGHT:int=200
CANVAS_WIDTH:int= 1000
CANVAS_HEIGHT:int= 1000
CELL_WIDTH=CANVAS_WIDTH/GRID_WIDTH 
CELL_HEIGHT=CANVAS_HEIGHT/GRID_HEIGHT 
OFFSET=Vector2(CELL_WIDTH*.5,CELL_HEIGHT*.5)


def numNeighbors(x,y,fast=false):
	neighbors= 0
	if fast:
		for i in [[x+1,y+1],[x+1,y],[x+1,y-1],[x,y+1],[x,y-1],[x-1,y+1],[x-1,y],[x-1,y-1]]:
			if grid[i[0]][i[1]]:
				neighbors+=1
		return neighbors
	else:
		if x>0:
			neighbors+=int(grid[x-1][y])
			if y>0:
				neighbors+=int(grid[x-1][y-1])
				neighbors+=int(grid[x][y-1])
			elif y<GRID_WIDTH:
				neighbors+=int(grid[x-1][y+1])
				neighbors+=int(grid[x-1][y])
		if x<GRID_WIDTH-1:
			if y>0:
				neighbors+=int(grid[x+1][y-1])
			elif y<GRID_WIDTH-1:
				neighbors+=int(grid[x+1][y+1])
		return neighbors
def makeGrid(width=GRID_WIDTH, height=GRID_HEIGHT):
	var out=Array()
	for i in range(height):
		row_array = Array(range(width))
		row_array.fill(false)
		out.append(row_array)
	return out
def scramble():
	for i in grid:
		for j in range(len(i)):
			i[j]=bool(randi()%2)
def iterate():
	var newGrid=makeGrid()
	for i in range(1,GRID_WIDTH-1):
		for j in range(1,GRID_HEIGHT-1):
			crowdedness=numNeighbors(i,j,true)
			if crowdedness==3:
				newGrid[i][j]=true
			elif crowdedness==2 and grid[i][j]:
				newGrid[i][j]=true
	return newGrid
def _on_timer_timeout():
	grid=iterate()
	update()
def makeCells():
	out=[]
	for x in range(GRID_WIDTH):
		var cell_row=[]
		for y in range(GRID_HEIGHT):
			var cell=$Cell.duplicate()
			cell.position=Vector2(x*CELL_WIDTH,y*CELL_HEIGHT)+OFFSET
			add_child(cell)
			cell_row.append(cell)
		out.append(cell_row)
	return out
def update():
	for x in range(GRID_WIDTH):
		for y in range(GRID_HEIGHT):
			if grid[x][y]:
				cells[x][y].show()
			else:
				cells[x][y].hide()
def _ready():
	cells=makeCells()
	grid=makeGrid()
	scramble()
	$Cell.hide()
	$Timer.timeout.connect(_on_timer_timeout)
