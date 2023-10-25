import numpy as np
import matplotlib.pyplot as plt

# Define the target distribution pi(i)
def pi(i):
    # This function returns the probability of state 'i' based on the given distribution.
    if 1 <= i <= 5:
        return 1 / (2**(6-i))
    elif i == 0:
        return 1 / (2**5)
    else:
        return 0  # This handles any other input outside of {0, 1, 2, 3, 4, 5}

# Define the transition kernel Q(y|x)
def Q(y, x):
    return 1/6

# Metropolis-Hastings Algorithm
def metropolis_hastings(n):
    x = 0  # Initial state
    states = [0, 1, 2, 3, 4, 5]  # Possible states
    samples = [x]  # List to store the sequence of states visited

    for _ in range(n):
        # Propose a new state 'y' randomly from the set of possible states.
        y = np.random.choice(states)
        # Calculate the acceptance probability 'A'
        A = min(1, (pi(y) * Q(x, y)) / (pi(x) * Q(y, x)))
        # Decide whether to accept the proposed state 'y' or stay in the current state 'x'.
        if np.random.uniform(0, 1) < A:
            x = y
        samples.append(x)

    return samples  # Return the sequence of states visited

# Compute the total variation distance between two distributions
def total_variation(p, q):
    return 0.5 * sum(abs(p[i] - q[i]) for i in range(len(p)))

# Simulate, plot histograms, print frequencies, and evaluate closeness to pi
for n in [100, 1000, 10000]:
    samples = metropolis_hastings(n)
    frequencies = [samples.count(i)/n for i in range(6)]

    # Calculate the total variation distance
    tv_distance = total_variation(frequencies, [pi(i) for i in range(6)])

    print(f"For n={n}:")
    print("State\tFrequency\tTarget Distribution")
    for i in range(6):
        print(f"{i}\t{frequencies[i]:.4f}\t\t{pi(i):.4f}")
    print(f"Total Variation Distance: {tv_distance:.4f}\n")

    plt.figure(figsize=(8, 6))
    plt.hist(samples, bins=[0, 1, 2, 3, 4, 5, 6], align='left', density=True, alpha=0.7, color='skyblue', edgecolor='black')
    plt.title(f"Histogram of Visited States for n={n}")
    plt.xlabel("State")
    plt.ylabel("Frequency")
    plt.xticks([0, 1, 2, 3, 4, 5])
    plt.grid(axis='y')
    plt.show()
