import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation

def julia_set(z, c, max_iter=50):
    """Julia set: z = z² + c, but c is constant and z varies"""
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_julia(x_min=-2, x_max=2, y_min=-2, y_max=2, width=400, height=400, max_iter=50, c=-0.7+0.27015j):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    
    image = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            z = complex(x[j], y[i])  # z varies, c is constant
            image[i, j] = julia_set(z, c, max_iter)
    return image

# Current view bounds and settings
x_min, x_max = -2, 2
y_min, y_max = -2, 2
zoom_level = 0

# Cool Julia set constants to try
julia_constants = [
    (-0.7 + 0.27015j, "Classic Spiral"),
    (-0.8 + 0.156j, "Dendrite"),
    (0.285 + 0.01j, "Douady Rabbit"),
    (-0.123 + 0.745j, "Lightning"),
    (-0.75 + 0j, "Simple"),
    (0.3 - 0.5j, "Swirl"),
    (-0.4 + 0.6j, "Branches"),
    (0 + 0.8j, "Vertical")
]

current_index = 0
auto_cycle = True

def on_click(event):
    global x_min, x_max, y_min, y_max, zoom_level, current_index, auto_cycle
    
    if event.button == 1:  # Left click to zoom in
        if event.xdata is not None and event.ydata is not None:
            click_x = x_min + (event.xdata / 400) * (x_max - x_min)
            click_y = y_min + (event.ydata / 400) * (y_max - y_min)
            
            width = (x_max - x_min) * 0.5
            height = (y_max - y_min) * 0.5
            
            x_min = click_x - width/2
            x_max = click_x + width/2
            y_min = click_y - height/2
            y_max = click_y + height/2
            
            zoom_level += 1
            update_plot()
    
    elif event.button == 3:  # Right click to toggle auto-cycle
        auto_cycle = not auto_cycle
        print(f"Auto-cycle: {'ON' if auto_cycle else 'OFF'}")
        if not auto_cycle:
            x_min, x_max = -2, 2
            y_min, y_max = -2, 2
            zoom_level = 0

def update_plot(frame=None):
    global current_index
    
    plt.clf()
    
    if auto_cycle:
        current_c, name = julia_constants[current_index]
    else:
        current_c, name = julia_constants[current_index]
    
    max_iter = 50 + zoom_level * 20
    
    image = generate_julia(x_min, x_max, y_min, y_max, max_iter=max_iter, c=current_c)
    
    colors = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'rainbow', 
              'hot', 'cool', 'spring', 'summer', 'autumn', 'winter', 'copper']
    random_cmap = random.choice(colors)
    
    plt.imshow(image, cmap=random_cmap)
    plt.axis('off')
    
    status = "AUTO-CYCLING" if auto_cycle else "PAUSED"
    plt.title(f'JULIA SET: {name} | {status} | Left click = Zoom | Right click = Toggle cycle', 
              fontsize=9, pad=10)
    
    print(f"{name}: {current_c}")

def animate(frame):
    global current_index
    if auto_cycle:
        current_index = (current_index + 1) % len(julia_constants)
        update_plot()

# Create interactive plot with animation
fig, ax = plt.subplots(figsize=(8, 8))
fig.canvas.mpl_connect('button_press_event', on_click)

# Start animation - changes every 1.5 seconds (1500ms)
ani = animation.FuncAnimation(fig, animate, interval=1500, repeat=True)

# Initial plot
update_plot()
plt.show()

print("Auto-cycling through Julia sets every 1.5 seconds!")
print("Left click to zoom in")
print("Right click to toggle auto-cycle on/off")
print("Watch the different fractal patterns emerge!")