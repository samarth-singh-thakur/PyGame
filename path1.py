import pygame, sys, time ,math
from pygame.locals import *
from tkinter import *
from tkinter import messagebox


class gt_grid():

	def __init__(self):
		self.start_r = 0
		self.start_c = 0
		self.end_r = 49
		self.end_c = 49
		self.col = 30
		self.row = 30
		self.walls = {}
		self.t1 = [1, 0, -1, 0]
		self.t2 = [0, 1, 0, -1]
		self.vis = [[False for j in range(30)]for i in range(30)]
		self.The_list = []
		self.flag = False
		self.parent = {}
		self.ways = [[False for j in range(30)]for i in range(30)]
		self.dist = [[False for j in range(30)]for i in range(30)]
		pygame.init()
		self.screen = pygame.display.set_mode((300,300))

	def safe(self,r,c):
		if (r>=0 and r<self.row and c>=0 and c<self.col):
			return True
		else:
			return False


	def execute(self):
		bb = self.bfs_util(self.start_r, self.start_c)
		l = []
		print(self.walls)

		for x in self.The_list:
			o = x.split(',')
			c0 = int(o[0])
			r0 = int(o[1])

			pygame.draw.rect(self.screen,(98,30,86),(c0*10,r0*10,9,9))
			pygame.display.update()

		if bb is True:
			p = str(self.end_r)+","+str(self.end_c)
			# print(p)
			pygame.draw.rect(self.screen,(0, 255, 0),(self.end_c*10,self.end_r*10,9,9))
			pygame.display.update()
			while True:
				try:
					l.append(p)
					c = int(p.split(",")[1])
					r = int(p.split(",")[0])
					pygame.draw.rect(self.screen,(0, 255, 0),(c*10,r*10,9,9))
					pygame.display.update()
					p = self.parent[p]
					time.sleep(.12)
				except:
					# time.sleep(3)
					return self.ways[self.end_r][self.end_c], self.dist[self.end_r][self.end_c]




	def bfs_util(self, r, c):

		q = []
		coor = str(r)+","+str(c)
		q.append(coor)
		self.ways[r][c] = 1
		self.vis[r][c] = 1

		while(len(q)>0):
			node = q[0]
			q.pop(0)
			var = node.split(",")
			r = int(var[0])
			c = int(var[1])
			
			for i in range(4):
				r0 = r + self.t1[i]
				c0 = c + self.t2[i]
				child = str(r0)+","+str(c0)
				if self.safe(r0, c0) is True:
					if (self.vis[r0][c0] is False and (str(c0)+","+str(r0)) not in self.walls):
						#prints the coordinates it travels while doing bfs
						self.dist[r0][c0] = 1 + self.dist[r][c]
						self.ways[r0][c0] += self.ways[r][c]
						self.parent[child] = node
						q.append(child)
						self.vis[r0][c0] = True
						self.The_list.append(str(c0)+","+str(r0))
						# self.root.after(5, self.grid[r0][c0].configure(bg = "yellow"))
						if(r0 is self.end_r and c0 is self.end_c):
							return True
						
					else:
						if(self.dist[r][c]+1 == self.dist[r0][c0]):
							self.ways[r0][c0]+=self.ways[r][c]

	def init(self):
		done = False
	# 0 255 245 backtracking color
	# 255,30,86 starting node color
	# c = (0, 30, 86)

		start_clr = (255,30,86)
		end_clr = (255, 172, 65)
		c = (0,150,255)
		c2 = (0,173,225)
		while done == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True

				if pygame.mouse.get_pressed()[0]:
					x,y = pygame.mouse.get_pos()
					x = x//10
					y = y//10
		# print(pygame.key.get_pressed(), "*")
						# print(x,y)
					self.walls[str(x)+","+str(y)] = 1;
					pygame.draw.rect(self.screen,c,(x*10,y*10,9,9))


				if event.type == KEYDOWN:
					if event.key == K_s:
							# print("Fvx")
						x,y = pygame.mouse.get_pos()
						x = x//10
						y = y//10
						# print(pygame.key.get_pressed(), "*")
							# print(x,
						self.start_r = y
						self.start_c = x
						print(y, x)
						pygame.draw.rect(self.screen,start_clr,(x*10, y*10, 9, 9))
						self.parent[str(y)+","+str(x)] = "-1"
					elif event.key == K_e:
	
						x,y = pygame.mouse.get_pos()
						x = x//10
						y = y//10
							# print(pygame.key.get_pressed(), "*")
							# print(x,y)
						self.end_r = y
						self.end_c = x
						print(y, x)
						pygame.draw.rect(self.screen,end_clr,(x*10,y*10, 9, 9))

					elif event.key == K_d:
						return self.execute()
				else:
					break

			for x in range (0,500,10):
				pygame.draw.line(self.screen,c,(1,x),(300,x),2)
				pygame.draw.line(self.screen,c,(x,1),(x,300), 2)
				pygame.display.update()







obj = gt_grid()
dist, ways = obj.init() #distance and number of ways

