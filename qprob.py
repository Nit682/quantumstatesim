import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import qr
import base64
from PIL import Image
from io import BytesIO
import re


def generate_gif(fig, update_quantum_state_plot, frames, interval):
    images = []

    for frame in range(frames):
        update_quantum_state_plot(frame)
        fig.canvas.draw()
        img = Image.frombytes(
            'RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())
        images.append(img)

    output_buffer = BytesIO()
    images[0].save(output_buffer, format='GIF', save_all=True,
                   append_images=images[1:], duration=interval, loop=0)

    return base64.b64encode(output_buffer.getvalue()).decode('utf-8')


def random_unitary(n):
    rand_matrix = np.random.rand(n, n) + 1j * np.random.rand(n, n)
    Q, _ = qr(rand_matrix)
    return Q


def parse_complex_string(complex_str):
    match = re.match(
        r'([+-]?\d+(\.\d+)?)([+-]\d+(\.\d+)?)j', complex_str.strip())
    if match:
        real = float(match.group(1))
        imaginary = float(match.group(3))
        return complex(real, imaginary)
    else:
        raise ValueError(f'Invalid complex number string: {complex_str}')


def quantum_state_gif(quantum_state_string):
    def update_quantum_state_plot(frame):
        nonlocal quantum_state

        probabilities = np.abs(quantum_state)**2

        ax.clear()
        ax.bar(outcome_indices, probabilities, color=outcome_colors)
        ax.set_ylim([0, 1])
        ax.set_xticks(outcome_indices)
        ax.set_xticklabels(outcome_labels)
        ax.set_ylabel('Probability')
        ax.set_xlabel('Outcome #')

        if np.all(probabilities < prob_threshold):
            print('Probabilities below threshold. Exiting...')
            plt.close()

        quantum_state = random_unitary(len(quantum_state)).dot(quantum_state)

    # Convert the input string to a NumPy array with complex numbers
    quantum_state = np.array(
        [parse_complex_string(x) for x in quantum_state_string.split(',')],
        dtype=complex
    )

    colormap = plt.cm.get_cmap('viridis')
    color_norm = plt.Normalize(vmin=0, vmax=len(quantum_state) - 1)
    outcome_colors = colormap(color_norm(np.arange(len(quantum_state))))

    prob_threshold = 0.01

    fig, ax = plt.subplots()

    outcome_indices = np.arange(len(quantum_state))
    outcome_labels = [f'{i+1}' for i in range(len(quantum_state))]

    animation_speed = 200
    total_frames = 25

    base64_gif_data = generate_gif(
        fig, update_quantum_state_plot, total_frames, animation_speed)

    return base64_gif_data
