import math
class LocationPiece(object):
	def __init__(self, piece_object, hex_coordinates, radius):
		self.piece_object = piece_object
		self.hex_coordinates = hex_coordinates
		self.x = self.hex_coordinates[0]
		self.y = self.hex_coordinates[1]
		self.z = self.hex_coordinates[2]
		self.sq_coordinates = self.translate_hex_position_to_pixels(radius)
		self.a = self.sq_coordinates[0]
		self.b = self.sq_coordinates[1]
		
	def translate_hex_position_to_pixels(self, radius):
		a_coord = (3.0/2.0)*radius*self.z
		b_coord = math.sqrt(3)*radius*(self.z/2.0 + self.x)
		return (a_coord, b_coord)
				
	@property
	def id_from_hex(self):
		return repr(self.hex_coordinates).replace(', ', '_')
