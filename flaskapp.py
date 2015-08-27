from flask import Flask, Response
import webhive
app = Flask(__name__)

@app.route("/")
def hello():
    return webhive.build_string()

@app.route("/click/<x>/<y>/<z>")
def asdf(x, y, z):
    return 'you clicked on' + str(x) + str(y) + str(z)
    #make the move in the python code 
    #return webhive.build_string() after it's done


@app.route("/piece_image.png")
def piece_image():
    return open("piece_image.png").read()

@app.route("/blank_image.png")
def blank_image():
    return open("blank_space.png").read()

if __name__ == "__main__":
    app.run(debug=True)
