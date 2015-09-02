from flask import Flask
import webhive
from board import Board as bo
app = Flask(__name__)

wh = webhive.WebHive()

@app.route("/")
def start():
    #d = filter(lambda coord: type(coord) == 'unicode', [x,y,z])
    #print "THIS IS IT"
    #print d
    return wh.build_string()

@app.route("/click/<x>/<y>/<z>")
def place_piece(x, y, z):
    wh.place_piece(x,y,z)
    return wh.build_string()


@app.route("/piece_image.png")
def piece_image():
    return open("piece_image.png").read()

@app.route("/blank_image.png")
def blank_image():
    return open("blank_space.png").read()

if __name__ == "__main__":
    app.run(debug=True)
