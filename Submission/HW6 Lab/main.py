import numpy as np
import matplotlib.pyplot as plt

# Define the range for x values
x = np.linspace(-5, 5, 400)  # limited range to avoid singularities

# Define the functions
y1 = 60 / (17 - 8 * np.cos(2 * np.pi * x))
y2 = 28 / (25 - 24 * np.cos(2 * np.pi * x))

# Handling potential division by zero or very small denominators
y1[np.isinf(y1)] = np.nan
y2[np.isinf(y2)] = np.nan

# Create the plots
plt.figure(figsize=(12, 6))

# Plotting the first function
plt.subplot(1, 2, 1)
plt.plot(x, y1, label=r'$\frac{60}{17-8\cos(2\pi x)}$')
plt.title(r'Graph of $\frac{60}{17-8\cos(2\pi x)}$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.ylim(0, 30)  # Limiting y-axis to observe the pattern
plt.legend()

# Plotting the second function
plt.subplot(1, 2, 2)
plt.plot(x, y2, label=r'$\frac{28}{25-24\cos(2\pi x)}$')
plt.title(r'Graph of $\frac{28}{25-24\cos(2\pi x)}$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.ylim(0, 30)  # Limiting y-axis to observe the pattern
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
