import math
from board import Board
header = """
<html>
<head>
<style>
img {
	position: absolute;
}

</style>
</head>

<body>
<div>
"""

footer= """
</div>
</body>
</html>
"""

def hex_at_square_coords(x,y):
	return '<img src="http://www.fontsaddict.com/images/icons/png/22865.png" style="left:%dpx; top:%dpx" width="400">' % (x,y)

radius = 153
#this specific radius is special for the image source

def translate_hex_position_to_pixels(hex_position, radius):
        x_coord = hex_position[0]
        z_coord = hex_position[2]
        a_coord = (3.0/2.0)*radius*z_coord
        b_coord = math.sqrt(3)*radius*(z_coord/2.0 + x_coord)
        return (a_coord, b_coord)


e = Board(20,20,radius)

img_string = ''
for key in e.empty_grid:
	(a,b) = translate_hex_position_to_pixels(key, radius)
	img_string += hex_at_square_coords(a,b)

print header + img_string + footer
