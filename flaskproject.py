from flask import Flask , render_template , session, redirect, url_for
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None,None,None],[None,None,None],[None,None,None]]
        session["turn"] = "X"
    return render_template("game.html", board=session["board"],turn=session["turn"])

@app.route("/play/<int:row>/<int:col>")
def play(row,col):
    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "Y"
    else:
        session["turn"] = "X"

    return redirect(url_for("index"))
    #return f"played {row} & {col}"

if __name__ == "__main__":
    app.run(host='127.0.0.1')

