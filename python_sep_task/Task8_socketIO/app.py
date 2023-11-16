from flask import render_template, Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)

@app.route("/")
def messages():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)