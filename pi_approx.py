import numpy as np

k = np.arange(0,22)
t = 1 / ((2*k+1) * ((-3)**k))
p = np.sqrt(12) * sum(t)

print("Approximation of π:", p)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Colors as RGBA
WHITE = [1, 1, 1, 1]
BLACK = [0, 0, 0, 1]
GREY  = [0.5, 0.5, 0.5, 1]
RED   = [1, 0, 0, 1]
PINK  = [1, 0.6, 0.8, 1]   # tongue color

# Base panda face (eyes open but with red filled)
panda_base = np.array([
    [WHITE,WHITE,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,WHITE,WHITE,BLACK,BLACK,WHITE,WHITE,WHITE,WHITE],
    [WHITE,WHITE,WHITE,BLACK,BLACK,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,BLACK,BLACK,WHITE,WHITE,WHITE],
    [WHITE,WHITE,BLACK,BLACK,RED,RED,BLACK,BLACK,BLACK,BLACK,RED,RED,BLACK,BLACK,WHITE,WHITE],
    [WHITE,WHITE,BLACK,BLACK,RED,RED,BLACK,BLACK,BLACK,BLACK,RED,RED,BLACK,BLACK,WHITE,WHITE],
    [WHITE,WHITE,WHITE,BLACK,BLACK,BLACK,BLACK,WHITE,WHITE,BLACK,BLACK,BLACK,BLACK,WHITE,WHITE,WHITE],
    [WHITE,WHITE,WHITE,WHITE,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,BLACK,WHITE,WHITE,WHITE,WHITE],
    [WHITE,WHITE,WHITE,WHITE,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,BLACK,WHITE,WHITE,WHITE,WHITE],
    [WHITE,WHITE,WHITE,WHITE,WHITE,BLACK,WHITE,WHITE,WHITE,WHITE,BLACK,WHITE,WHITE,WHITE,WHITE,WHITE],
    [WHITE,WHITE,WHITE,WHITE,WHITE,GREY,BLACK,BLACK,BLACK,BLACK,GREY,WHITE,WHITE,WHITE,WHITE,WHITE],
    [WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,GREY,BLACK,BLACK,GREY,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE],
    [WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,GREY,GREY,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE],
    [WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE],
    [WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE,WHITE],
], dtype=float)

# Versions
panda_open   = panda_base.copy()
panda_closed = panda_base.copy()
panda_closed[2:4,4:6] = WHITE
panda_closed[2:4,10:12] = WHITE

# Tongue version (open + tongue)
panda_tongue = panda_open.copy()
panda_tongue[11,7:9] = PINK
panda_tongue[12,7:9] = PINK

# Set up figure
fig, ax = plt.subplots()
im = ax.imshow(panda_open, interpolation="nearest")
ax.axis("off")

# Animation function
def update(frame):
    if frame < 40:  # normal blinking
        if frame % 20 < 5:
            im.set_array(panda_closed)
        else:
            im.set_array(panda_open)
    else:  # last part: stick out tongue
        im.set_array(panda_tongue)
    return [im]

ani = animation.FuncAnimation(fig, update, frames=60, interval=200, blit=True)

plt.show()
