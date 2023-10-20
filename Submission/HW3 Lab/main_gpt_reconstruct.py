import numpy as np
from scipy import stats

def run(p, n):
    """
    Simulate the number of tosses needed to observe 'n' consecutive heads.

    Parameters:
    - p: Probability of observing a head in a single toss.
    - n: Number of consecutive heads to observe.

    Returns:
    - Number of tosses needed.
    """
    tosses = 0                   # Initialize the number of tosses
    in_a_row = 0                 # Initialize the number of consecutive heads observed

    # Continue tossing until 'n' consecutive heads are observed
    while in_a_row < n:
        tosses += 1
        if stats.bernoulli.rvs(p, size=1).item(0) == 1:
            in_a_row += 1
        else:
            in_a_row = 0  # Reset the count if a tail is observed

    return tosses

def simulate_run(p, n, repetitions):
    """
    Simulate 'repetitions' number of runs to observe 'n' consecutive heads.

    Parameters:
    - p: Probability of observing a head in a single toss.
    - n: Number of consecutive heads to observe.
    - repetitions: Number of simulations to run.

    Returns:
    - List of tosses needed for each simulation.
    """
    results = []
    for _ in range(repetitions):
        results.append(run(p, n))
    return results

def HT_run(p):
    """
    Simulate the number of tosses needed to observe a head followed by a tail.

    Parameters:
    - p: Probability of observing a head in a single toss.

    Returns:
    - Number of tosses needed.
    """
    Heads, Tails, tosses = 0, 0, 0

    # Continue tossing until a head followed by a tail is observed
    while Tails == 0:
        while Heads == 0:
            tosses += 1
            if stats.bernoulli.rvs(p, size=1).item(0) == 1:
                Heads += 1
        tosses += 1
        if stats.bernoulli.rvs(p, size=1).item(0) == 0:
            Tails += 1
    return tosses

def simulate_HT(p, N):
    """
    Simulate 'N' number of runs to observe a head followed by a tail.

    Parameters:
    - p: Probability of observing a head in a single toss.
    - N: Number of simulations to run.

    Returns:
    - List of tosses needed for each simulation.
    """
    return [HT_run(p) for _ in range(N)]

def HTHT_run(p):
    """
    Simulate the number of tosses needed to observe the sequence HTHT.

    Parameters:
    - p: Probability of observing a head in a single toss.

    Returns:
    - Number of tosses needed.
    """
    Heads, Tails, tosses = 0, 0, 0

    # Continue tossing until the sequence HTHT is observed
    while Tails < 2:
        while Heads < 2 and Tails < 2:
            tosses += 1
            result = stats.bernoulli.rvs(p, size=1).item(0)
            if result == 1:
                Heads += 1
            else:
                Tails += 1
                Heads = 0 if Tails == 1 else 1
    return tosses

def simulate_HTHT(p, N):
    """
    Simulate 'N' number of runs to observe the sequence HTHT.

    Parameters:
    - p: Probability of observing a head in a single toss.
    - N: Number of simulations to run.

    Returns:
    - List of tosses needed for each simulation.
    """
    return [HTHT_run(p) for _ in range(N)]

# Simulate different sequences
sim_W_HH = simulate_run(0.5, 2, 100)
sim_W_HT = simulate_HT(0.5, 100)
sim_W_HTHT = simulate_HTHT(0.5, 100)
sim_W_HHHH = simulate_run(0.5, 4, 100)

# Print the expected number of tosses for each sequence
print("E(time to see HT) =", np.mean(sim_W_HT))
print("E(time to see HH) =", np.mean(sim_W_HH))
print("E(time to see HTHT) =", np.mean(sim_W_HTHT))
print("E(time to see HHHH) =", np.mean(sim_W_HHHH))
