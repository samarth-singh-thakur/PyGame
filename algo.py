class Algo():

	def __init__(self):
		self.start_r = 0
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

	def safe(self,r,c):
		if (r>=0 and r<self.row and c>=0 and c<self.col):
			return True
		else:
			return False


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



