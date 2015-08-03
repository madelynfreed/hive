class Position(object):
	def __init__(self, x_coord, y_coord, z_coord):	
		self.x_coord = x_coord
		self.y_coord = y_coord		
		self.z_coord = z_coord		
	
	def adjacent_spots(self):
		adj_spot_formulae = [(self.x_coord + 1, self.y_coord, self.z_coord - 1),
				     (self.x_coord + 1, self.y_coord -1, self.z_coord),
				     (self.x_coord, self.y_coord -1, self.z_coord + 1),
				     (self.x_coord - 1, self.y_coord, self.z_coord + 1),
				     (self.x_coord - 1, self.y_coord + 1, self.z_coord),
				     (self.x_coord, self.y_coord + 1, self.z_coord - 1)]
		return [formula for formula in adj_spot_formulae]
