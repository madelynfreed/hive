import numpy as np
class MoveValidator(object):
	def is_valid_move(self, start_hex_coord, end_hex_coord, piece_dict):
		piece_type = piece_dict[start_hex_coord].piece_type
		if self.flood(start_hex_coord, piece_dict):
			if not self.space_has_piece_in_it(end_hex_coord, piece_dict):
				if self.is_adjacent_to_the_hive(end_hex_coord,piece_dict):
					if self.piece_validity(piece_type, start_hex_coord, end_hex_coord, piece_dict):
						return True
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False
		#piece_type = piece_dict[start_hex_coord].piece_type
		
		#return (self.flood(start_hex_coord, piece_dict)
		#and not 
		#self.space_has_piece_in_it(end_hex_coord, piece_dict)
		#and
		#self.is_adjacent_to_the_hive(end_hex_coord, piece_dict)
		#and self.queen_valid_move(start_hex_coord, end_hex_coord, piece_dict))		

	def piece_validity(self, piece_type, start_hex_coord, end_hex_coord, piece_dict):
		if piece_type == 'queen':
			return self.queen_valid_move(start_hex_coord, end_hex_coord, piece_dict)
		elif piece_type == 'grasshopper':
			return self.grasshopper_valid_move(start_hex_coord, end_hex_coord, piece_dict)
		else:
			return True
		

	def queen_valid_move(self, start_hex_coord, end_hex_coord, piece_dict):
		return (self.are_adjacent(start_hex_coord,
				 end_hex_coord)) 

	def grasshopper_valid_move(self, start_hex_coord, end_hex_coord, piece_dict):
		delta = map(lambda pair: pair[1]-pair[0], zip(start_hex_coord, end_hex_coord))
		
		if delta.count(0) == 1:
			all_pieces = [piece_dict.get(tuple(spot)) for spot in self.all_spots_between_two_inline_spots(start_hex_coord, end_hex_coord)]
			for piece in all_pieces:
				if piece == None:
					return False
				else:
					return True
		else:
			return False

			
	def all_spots_between_two_inline_spots(self, start_hex_coord, end_hex_coord):
		delta = tuple(map(lambda pair: pair[1]-pair[0], zip(start_hex_coord, end_hex_coord)))
		length_of_line = max(delta)
		digit = np.array(map(lambda coord: coord/length_of_line, delta))

		check_space = np.array(start_hex_coord)
		np_spots = list([check_space+(digit*i) for i in range(1, length_of_line)])
	
		return [list(spot) for spot in np_spots]
		
		#list(start-end) has exactly one 0 in it
		#there are pieces between start and end

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
		working_p_d = dict(pieces_dict)
		try:
			first_neigh = self.neighbors(spot,working_p_d)[0]
		except IndexError:
			return False
		working_p_d.pop(spot, None)
		visited = []
		flooded = self.find_all_new_neighs(first_neigh, working_p_d, visited)
		return set(flooded) == set(working_p_d.keys())
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
		
