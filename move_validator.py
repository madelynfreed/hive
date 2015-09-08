class MoveValidator(object):
	def is_valid_move(self, start_hex_coord, end_hex_coord, piece_dict):
		return (self.are_adjacent(start_hex_coord,
				 end_hex_coord) 
		and not 
		self.space_has_piece_in_it(end_hex_coord, piece_dict)
		and
		self.is_adjacent_to_the_hive(end_hex_coord, piece_dict))		

	def are_adjacent(self, hexposition1, hexposition2):
		return hexposition1 in self.adjacent_spots(hexposition2) 

	def space_has_piece_in_it(self, hex_coord, pieces_dict):
		return hex_coord in pieces_dict

	def is_adjacent_to_the_hive(self, hex_coord, pieces_dict):
		l = [self.adjacent_spots(hex_coo) for hex_coo in pieces_dict.keys()]
		flat_list = reduce(lambda x,y: x+y, l)
		return  hex_coord in flat_list 

	def adjacent_spots(self, hex_position):
		x_coord = hex_position[0]
		y_coord = hex_position[1]
		z_coord = hex_position[2]
		adj_spot_formulae = [(x_coord + 1, y_coord, z_coord - 1),
				     (x_coord + 1, y_coord -1, z_coord),
				     (x_coord, y_coord -1, z_coord + 1),
				     (x_coord - 1, y_coord, z_coord + 1),
				     (x_coord - 1, y_coord + 1, z_coord),
				     (x_coord, y_coord + 1, z_coord - 1)]
		return [formula for formula in adj_spot_formulae]
	


