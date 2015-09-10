class MoveValidator(object):
	def is_valid_move(self, start_hex_coord, end_hex_coord, piece_dict):
		return (self.are_adjacent(start_hex_coord,
				 end_hex_coord) 
		and
		self.flood(start_hex_coord, piece_dict)
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
		adj_spot_formulae = [
			(x_coord + 1, y_coord, z_coord - 1),
			(x_coord + 1, y_coord -1, z_coord),
			(x_coord, y_coord -1, z_coord + 1),
			(x_coord - 1, y_coord, z_coord + 1),
			(x_coord - 1, y_coord + 1, z_coord),
			(x_coord, y_coord + 1, z_coord - 1)]
		return [formula for formula in adj_spot_formulae]
	
	def neighbors(self, hex_position, pieces_dict):
		adj_spots = self.adjacent_spots(hex_position)
		return filter(lambda spot: pieces_dict.get(spot) != None, adj_spots)

			
	def find_all_new_neighs(self, spot, pieces_dict, visited):
		unvisited = filter(
			    lambda spot: spot not in visited,
			    self.neighbors(spot, pieces_dict))
		for each in unvisited:
			visited.append(each)
		for each in unvisited:
			self.find_all_new_neighs(each, pieces_dict, visited)
		return visited

	def flood(self, spot, pieces_dict):
		first_neigh = self.neighbors(spot,pieces_dict)[0]
		pieces_dict.pop(spot, None)
		visited = []
		flooded = self.find_all_new_neighs(first_neigh, pieces_dict, visited)
		return set(flooded) == set(pieces_dict.keys())
	def path_found_when_piece_is_moved(self, hex_position, pieces_dict):
		#find hex_position's neighbors
		neighbors_under_test = self.neighbors(hex_position, pieces_dict)
		pieces_dict.pop(hex_position, None)
		for neighbor in neighbors_under_test:
			self.path_from_piece_to_piece(xxxxx)
		#remove hex position from pieces_dict
		#is there a path from neghbor1>2, 2>3, n>n+1?
		#return if there is

		pass
	def path_from_piece_to_piece(self, spot1, spot2, visited_pieces, pieces_dict):
		visited_pieces.append(spot1)
		neighbors = filter(lambda spot: spot not in visited_pieces, self.neighbors(spot1, pieces_dict)) 
		for neighbor in neighbors:
			if neighbor == spot2:
				return (True, neighbor)
		return (False, visited_pieces)
		
