# Python Mathematical Visualizations

This repository contains Python scripts for visualizing mathematical concepts and creating interactive animations.

## Files

### `mandelbrot_set.py`
An interactive Julia set fractal generator that features:
- **Auto-cycling through different Julia set constants** - automatically switches between 8 different fractal patterns
- **Interactive zooming** - left-click to zoom into any point
- **Toggle controls** - right-click to pause/resume auto-cycling
- **Dynamic coloring** - uses random color maps for visual variety
- **Adaptive iterations** - increases detail when zooming in

**Usage:**
- Run the script to start the interactive visualization
- Left-click anywhere to zoom in on that point
- Right-click to toggle between auto-cycling and manual control
- Watch as different fractal patterns emerge every 1.5 seconds

### `pi_approx.py`
A dual-purpose script that:
1. **Calculates π approximation** using the series: π ≈ √12 × Σ(1/((2k+1)×(-3)^k))
2. **Animated panda visualization** - displays a cute blinking panda with tongue animation

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install numpy matplotlib
```

## Running the Scripts

```bash
python mandelbrot_set.py  # Interactive Julia set visualization
python pi_approx.py       # Pi approximation + panda animation
```

## Julia Set Constants

The Julia set visualizer includes these predefined constants:
- **Classic Spiral**: -0.7 + 0.27015j
- **Dendrite**: -0.8 + 0.156j  
- **Douady Rabbit**: 0.285 + 0.01j
- **Lightning**: -0.123 + 0.745j
- **Simple**: -0.75 + 0j
- **Swirl**: 0.3 - 0.5j
- **Branches**: -0.4 + 0.6j
- **Vertical**: 0 + 0.8j

## Features

- **Real-time interaction** with mathematical visualizations
- **Educational value** - demonstrates complex mathematical concepts
- **Visual appeal** - beautiful fractal patterns and animations
- **Performance optimized** - efficient NumPy operations

Enjoy exploring the beautiful world of mathematical visualizations!