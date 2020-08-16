import pygame
import random
pygame.init()

cells=[]

class Cell:

	def __init__(self,x,y,alive,screen,bw,bh):
		self.x=x
		self.y=y
		self.alive=alive
		self.screen=screen
		self.bw=bw
		self.bh=bh
	def show(self):#coords will be mapped down to 1-cols and 1-rows
		if self.alive:
			pygame.draw.rect(self.screen,(30,30,30),pygame.Rect(self.x*self.bw,self.y*self.bh,self.bw,self.bh))
		else:
			pygame.draw.rect(self.screen,(220,220,220),pygame.Rect(self.x*self.bw,self.y*self.bh,self.bw,self.bh))
def drawGrid(screen,w,h,bw,bh,cols,rows,color):
	for i in range(cols):
		pygame.draw.line(screen,color,(bw*i+bw,0),(bw*i+bw,h))
	for i in range(cols):
		pygame.draw.line(screen,color,(0,bh*i+bh),(w,bh*i+bh))
def initCells(bw,bh,cols,rows,w,h,screen):
	for y in range(rows):
		cells.append([])
		for x in range(cols):
			cells[y].append(Cell(x,y,False,screen,bw,bh))#bool(random.getrandbits(1)) for random 50/50
def changeStateToRandom(bw,bh,cols,rows,w,h,screen):
	for y in range(rows):
		cells.append([])
		for x in range(cols):
			cells[y][x].alive=bool(random.getrandbits(1))#bool(random.getrandbits(1)) for random 50/50
def clearBoard(bw,bh,cols,rows,w,h,screen):
	for y in range(rows):
		cells.append([])
		for x in range(cols):
			cells[y][x].alive=False

	#cells.append(Cell(j,i,bool(random.getrandbits(1)),screen,bw,bh))
def countNeighbors(cell):#trx catch all of this
	counter=0
	try:
		if cells[cell.y-1][cell.x].alive:#left
			counter+=1
	except:
		pass
	try:
		if cells[cell.y+1][cell.x].alive:#right
			counter+=1
	except:
		pass
	try:	
		if cells[cell.y][cell.x-1].alive:#up
			counter+=1
	except:
		pass
	try:	
		if cells[cell.y][cell.x+1].alive:#down
			counter+=1
	except:
		pass
	try:	
		if cells[cell.y-1][cell.x-1].alive:#up left
			counter+=1
	except:
		pass
	try:	
		if cells[cell.y+1][cell.x-1].alive:#up right
			counter+=1
	except:
		pass
	try:	
		if cells[cell.y+1][cell.x+1].alive:#down right
			counter+=1
	except:
		pass
	try:	
		if cells[cell.y-1][cell.x+1].alive:#down left
			counter+=1
	except:
		pass
	#print(f"Cell ({cell.x},{cell.y}) has {counter} alive neighbors ")
	return counter
def gameOfLife(bw,bh,width,height,cols,rows):
	global cells
	newCells=[]
	for y in range(rows):
		newCells.append([])
		for x in range(cols):
			newCells[y].append(Cell(x,y,False,screen,bw,bh))


	for y in range(rows):
		for x in range(cols):

			if countNeighbors(cells[y][x])<2:
				newCells[y][x].alive=False
			elif countNeighbors(cells[y][x])>3:
				newCells[y][x].alive=False
			elif countNeighbors(cells[y][x])==3:
				newCells[y][x].alive=True
			else:
				newCells[y][x]=cells[y][x]
			
	cells=newCells
def displayCells(cells):
	for i in range(len(cells)):
		for j in range(len(cells[i])):
			cells[i][j].show()
def main():
	global Width,Height,gameRunning,screen,clock,FPS,bw,bh,cols,rows
	global cells 
	rows=40
	cols=60
	Width=1200
	Height=800

	startSimulation=False

	bw=Width/cols
	bh=Height/rows

	gameRunning=True
	clock=pygame.time.Clock()
	FPS=5
	screen=pygame.display.set_mode((Width,Height))
	pygame.display.set_caption("Game Of Life: Lars Edition")

	screen.fill((200,200,0))
	
	#TEST area - 
	#-------


	initCells(bw,bh,cols,rows,Width,Height,screen)
	#print(cells)
	
	tempX=0
	tempY=0
	while gameRunning:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameRunning=False
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_s:
					startSimulation=not startSimulation
				elif event.key==pygame.K_r:
					changeStateToRandom(bw,bh,cols,rows,Width,Height,screen)
				elif event.key==pygame.K_c:
					clearBoard(bw,bh,cols,rows,Width,Height,screen)
			if event.type==pygame.MOUSEBUTTONDOWN:
				
			

				cells[int(pygame.mouse.get_pos()[1]/bh)][int(pygame.mouse.get_pos()[0]/bw)].alive =not cells[int(pygame.mouse.get_pos()[1]/bh)][int(pygame.mouse.get_pos()[0]/bw)].alive
				tempY=int(pygame.mouse.get_pos()[1]/bh)
				tempX=int(pygame.mouse.get_pos()[0]/bw)
				
		
		displayCells(cells)
		drawGrid(screen,Width,Height,bw,bh,cols,rows,(0,200,200))
		if startSimulation:
			gameOfLife(bw,bh,Width,Height,cols,rows)
		
		pygame.display.flip()
		screen.fill((200,200,0))

if __name__=="__main__":
	main()
