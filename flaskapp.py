from flask import Flask, g, jsonify, render_template, request, url_for
import sqlite3
import webhive
from contextlib import closing

#configuration
DATABASE = '/tmp/hive.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

wh = webhive.WebHive()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

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
	return open("templates/hexagons.css").read()
@app.route("/main.js")
def open_js():
    return open("main.js").read()

@app.route("/piece_image.png")
def piece_image():
    return open("piece_image.png").read()

@app.route("/blank_image.png")
def blank_image():
    return open("blank_space.png").read()

@app.route('/_add_numbers')
def add_numbers():
	a = request.args.get('a',0,type=int)
	b = request.args.get('b',0,type=int)
	return jsonify(result=a+b)

@app.route('/index')
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
