import pygame, sys, time ,math
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
from algo import Algo

class gt_grid(Algo):

	def __init__(self):
<<<<<<< HEAD
		Algo.__init__(self)
=======
		self.start_r = 0
		self.start_c = 0
		self.end_r = 59
		self.end_c = 59
		self.col = 60
		self.row = 60
		self.walls = {}
		self.t1 = [1, 0, -1, 0]
		self.t2 = [0, 1, 0, -1]
		self.vis = [[False for j in range(60)]for i in range(60)]
		self.The_list = []
		self.flag = False
		self.parent = {}
		self.ways = [[False for j in range(60)]for i in range(60)]
		self.dist = [[False for j in range(60)]for i in range(60)]
>>>>>>> 76a13fc2e13190847a19e6bdf8968f5d27e8a0ee
		pygame.init()
		self.screen = pygame.display.set_mode((900,900))



	def execute(self):
		bb = self.bfs_util(self.start_r, self.start_c)
		l = []
		# print(self.walls)
		r = 225
		g = 30
		for x in self.The_list:
			o = x.split(',')
			c0 = int(o[0])
			r0 = int(o[1])

			pygame.draw.rect(self.screen,(225,30,86),(c0*30,r0*30,30,30))
			pygame.display.update()
			time.sleep(.02)




		if bb is True:
			p = str(self.end_r)+","+str(self.end_c)
			# print(p)
			pygame.draw.rect(self.screen,(0, 255, 0),(self.end_c*30,self.end_r*30,30,30))
			pygame.display.update()
			# time.sleep()
			while True:
				try:
					l.append(p)
					c = int(p.split(",")[1])
					r = int(p.split(",")[0])
					pygame.draw.rect(self.screen,(0, 255, 0),(c*30,r*30,30,30))
					pygame.display.update()
					p = self.parent[p]
					time.sleep(.12)
				except:
					# time.sleep(3)
					return self.ways[self.end_r][self.end_c], self.dist[self.end_r][self.end_c]


	def init(self):
		done = False
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
					x = x//30
					y = y//30
		# print(pygame.key.get_pressed(), "*")
						# print(x,y)
					self.walls[str(x)+","+str(y)] = 1;
					pygame.draw.rect(self.screen,c,(x*30,y*30,30,30))


				if event.type == KEYDOWN:
					if event.key == K_s:
							# print("Fvx")
						x,y = pygame.mouse.get_pos()
						x = x//30
						y = y//30
						# print(pygame.key.get_pressed(), "*")
							# print(x,
						self.start_r = y
						self.start_c = x
						print(f"starting node -- {y}, {x}")
						pygame.draw.rect(self.screen,start_clr,(x*30, y*30, 30, 30))
						self.parent[str(y)+","+str(x)] = "-1"
					elif event.key == K_e:
	
						x,y = pygame.mouse.get_pos()
						x = x//30
						y = y//30
							# print(pygame.key.get_pressed(), "*")
							# print(x,y)
						self.end_r = y
						self.end_c = x
						print(f"starting node -- {y}, {x}")
						pygame.draw.rect(self.screen,end_clr,(x*30,y*30, 30, 30))

					elif event.key == K_d:
						return self.execute()
				else:
					break

			for x in range (0,900,30):
				pygame.draw.line(self.screen,c,(1,x),(900,x),2)
				pygame.draw.line(self.screen,c,(x,1),(x,900), 2)
				pygame.display.update()


obj = gt_grid()
ways, dist = obj.init() #distance and number of ways
<<<<<<< HEAD
print(f"the shortest path to dest is {dist} blocks away and there are {ways} to reach the destination")
=======
print(f"the shortest path to dest is {dist} blocks away and there are {ways} to reach the destination")

>>>>>>> 76a13fc2e13190847a19e6bdf8968f5d27e8a0ee
