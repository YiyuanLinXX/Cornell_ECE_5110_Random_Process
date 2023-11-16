import numpy as np
import matplotlib.pyplot as plt

# Define the random walk step generator
def step(n):
    # Generate a step of +1 or -1 with equal probability (0.5 each)
    return np.where(np.random.rand(n) < 0.5, 1, -1)

# Function to generate random walk paths
def generate_random_walk_paths(N, num_paths):
    # Initialize a zero matrix to store the paths
    paths = np.zeros((num_paths, N + 1))
    for i in range(num_paths):
        # Generate steps and compute the cumulative sum to form the path
        steps = step(N)
        paths[i, 1:] = np.cumsum(steps)
    return paths

# Function to perform diffusive rescaling
def diffusive_rescaling(paths, N, t):
    # Calculate the index for time t using floor to simulate the Wiener process
    index_at_t = int(np.floor(N * t))
    # Select the path values at the calculated index and rescale
    rescaled_values_at_t = paths[:, index_at_t] / np.sqrt(N)
    return rescaled_values_at_t

# Function to calculate the empirical variance
def calculate_empirical_variance(values):
    # Calculate and return the variance of the given values
    return np.var(values)

# Define N values and number of sample paths
N_values = [10, 100, 1000]
num_sample_paths = 10000
t_values = [1, 0.2]

# Generate and rescale paths for each N and plot sample paths
empirical_variances = {}
for N in N_values:
    paths = generate_random_walk_paths(N, num_sample_paths)
    empirical_variances[N] = {}

    # Plotting the sample paths
    plt.figure(figsize=(12, 5))
    plt.title(f"Sample Paths for N={N}")
    for path in paths / np.sqrt(N):
        plt.plot(np.linspace(0, 1, N + 1), path)
    plt.xlabel("t")
    plt.ylabel("W_N(t)")
    plt.show()

    # Generating histograms and calculating variances
    plt.figure(figsize=(12, 5))
    for i, t in enumerate(t_values):
        rescaled_values = diffusive_rescaling(paths, N, t)
        variance = calculate_empirical_variance(rescaled_values)
        empirical_variances[N][t] = variance

        # Plotting histograms
        plt.subplot(1, 2, i+1)
        plt.hist(rescaled_values, bins=20, alpha=0.7)
        plt.title(f"Histogram of W_{N}({t}) - Variance: {variance:.4f}")
        plt.xlabel(f"W_{N}({t})")
        plt.ylabel("Frequency")

    plt.suptitle(f"Random Walk Simulation for N={N}")
    plt.tight_layout()
    plt.show()

# Display empirical variances
empirical_variances

