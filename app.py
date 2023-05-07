from flask import Flask, render_template, request, Response
import base64
from qprob import quantum_state_gif

app = Flask(__name__)


@app.route('/')
def display_page():
    return render_template('index.html')


@app.route('/display_animation', methods=['GET'])
def display_animation():
    quantum_state_string = request.args.get('quantum_state')
    print(quantum_state_string)

    base64_gif_data = quantum_state_gif(quantum_state_string)
    gif_data = base64.b64decode(base64_gif_data)

    return Response(gif_data, mimetype='image/gif')


if __name__ == '__main__':
    app.run()
