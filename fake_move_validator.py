class FakeMoveValidator(object):
	def __init__(self):
		self.valid_moves = []
	
	def allow_move(self, start_place, end_place, pieces):
		self.valid_moves.append((start_place, end_place, pieces))

	def is_valid_move(self, start_place, end_place, pieces):
		return (start_place, end_place, pieces) in self.valid_moves
