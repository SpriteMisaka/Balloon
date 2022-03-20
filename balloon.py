import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def parse_config(file_path):
    file = open(file_path, 'r')
    return {line.split('=')[0].strip() : line.split('=')[1].strip() for line in file}


def animate(i):
    global volume
    global count
    count += volume * (0.001 * inflate)
    if count > 1:
        count = 1
    elif count > 0:
        count -= (0.001 * deflate)
    line.set_ydata(count * np.sin(x))
    return line,


def print_sound(indata, outdata, frames, time, status):
    global volume
    volume = int(np.linalg.norm(indata) * 10)


if __name__ == "__main__":
    volume = 0
    count = 0
    config = parse_config('.\\config')
    inflate = float(config['inflate'])
    deflate = float(config['deflate'])
    
    fig, ax = plt.subplots()
    x = np.arange(0, 2 * np.pi, 0.01)
    line, = ax.plot(np.cos(x), np.sin(x))
    plt.axis('equal')
    
    ani = FuncAnimation(fig=fig, func=animate, interval=20, blit=False)
    
    with sd.Stream(callback=print_sound):
        plt.show()
