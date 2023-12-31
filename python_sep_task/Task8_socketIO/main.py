from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('Base.html')

@socketio.on('message')
def handle_message(data):
    message = data['message']
    print('Received message:', message)
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
