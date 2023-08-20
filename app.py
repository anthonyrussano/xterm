from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets(app)

@app.route('/')
def index():
    return render_template('index.html')

@sockets.route('/terminal')
def terminal_socket(ws):
    while True:
        message = ws.receive()
        output = run_your_cli_command(message)
        ws.send(output)
