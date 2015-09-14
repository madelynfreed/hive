from flask import Flask
import webhive
app = Flask(__name__)

wh = webhive.WebHive()
def map_to_int(hex_coords):
    return map(lambda hex_coord: int(hex_coord), hex_coords)
@app.route("/")
def start():
    return wh.build_string()

@app.route("/click/<x>/<y>/<z>")
def place_piece(x, y, z):
    int_hexes = map_to_int([x,y,z])
    wh.place_piece('exists',*int_hexes)
    return wh.build_string()

@app.route("/place/<piece_type>/at/<x>/<y>/<z>")
def place_piece_and_type(piece_type, x, y, z):
    int_hexes = map_to_int([x,y,z])
    piece_type = str(piece_type)
    wh.place_piece(piece_type, *int_hexes)
    return wh.build_string()

@app.route("/move/<x1>/<y1>/<z1>/to/<x2>/<y2>/<z2>")
def move_piece(x1, y1, z1, x2, y2, z2):
    int_hexes = map_to_int([x1, y1, z1, x2, y2, z2])
    wh.move_piece(*int_hexes)
    return wh.build_string()

@app.route("/hexagons.css")
def open_css():
	return open("hexagons.css").read()

@app.route("/piece_image.png")
def piece_image():
    return open("piece_image.png").read()

@app.route("/blank_image.png")
def blank_image():
    return open("blank_space.png").read()

if __name__ == "__main__":
    app.run(debug=True)
