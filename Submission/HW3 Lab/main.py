import numpy as np
from scipy import stats

def run(p, n):
    """Returns one simulated value of W_H,n
    in i.i.d. Bernoulli (p) trials"""

    tosses = 0                   # Number of tosses
    in_a_row = 0                 # Number of consecutive heads observed

    while in_a_row < n:          # While fewer than n consecutive heads
        tosses += 1             # update tosses
        if stats.bernoulli.rvs(p, size=1).item(0) == 1:
            in_a_row +=1                # update in_a_row
        else:
            in_a_row = 0                # reset in_a_row

    return tosses

def simulate_run(p, n, repetitions):
    """Returns an array of length equal to repetitions,
    whose entries are independent simulated values of W_H,n
    in i.i.d. Bernoulli (p) trials"""
    results = []
    i=0
    while i < repetitions:
        i+=1
        results.append(run(p,n))
    return results


def HT_run(p):
    """Returns one simulated value of W_HT
    in i.i.d. Bernoulli (p) trials"""

    Heads = 0
    Tails = 0
    tosses = 0
    while Tails == 0:  # While no Tails has been observed after a Heads
        while Heads == 0:
            tosses += 1
            if stats.bernoulli.rvs(p, size=1).item(0) == 1:
                Heads += 1       #Got a heads, break out of the heads loop
        tosses += 1

        if stats.bernoulli.rvs(p, size=1).item(0) == 0:
            Tails +=1
    return tosses

def simulate_HT(p, N):
    """Returns an array of length equal to repetitions,
    whose entries are independent simulated values of W_HT
    in i.i.d. Bernoulli (p) trials"""
    results = []
    i = 0
    while i< N:
        i += 1
        results.append(HT_run(p))
    return results

def HTHT_run(p):
    """Returns one simulated value of W_HTHT
    in i.i.d. Bernoulli (p) trials"""

    Heads = 0
    Tails = 0
    tosses = 0
    while Tails < 2 :  # While no Tails has been observed after a Heads
        while Heads == 0 and Tails == 0 :
            tosses += 1
            if stats.bernoulli.rvs(p, size=1).item(0) == 1:
                Heads += 1       #Got a heads (H), break out of the heads loop

        while Heads == 1 and Tails == 0 :
            tosses += 1
            if stats.bernoulli.rvs(p, size=1).item(0) == 0:
                Tails +=1 # Got T (HT), break out of the tails loop

        while Heads == 1 and Tails == 1:
            tosses += 1
            if stats.bernoulli.rvs(p, size=1).item(0) == 1:
                Heads += 1       #Got a heads (HTH), break out of the heads loop
            else:
                Heads = 0
                Tails = 0

        while Heads == 2 and Tails == 1:
            tosses += 1
            if stats.bernoulli.rvs(p, size=1).item(0) == 0:
                Tails += 1       #Got a T (HTHT), break out of the whole loop
            else:
                Heads = 1
                Tails = 0
    return tosses

def simulate_HTHT(p, N):
    """Returns an array of length equal to repetitions,
    whose entries are independent simulated values of W_HTHT
    in i.i.d. Bernoulli (p) trials"""
    results = []
    i = 0
    while i< N:
        i += 1
        results.append(HTHT_run(p))
    return results

sim_W_HH = simulate_run(0.5, 2, 10000)
sim_W_HT = simulate_HT(0.5, 10000)
sim_W_HTHT = simulate_HTHT(0.5, 10000)
sim_W_HHHH = simulate_run(0.5, 4, 10000)

print("E(time to see HT) = ", np.mean(sim_W_HT))
print("E(time to see HH) = ", np.mean(sim_W_HH))
print("E(time to see HTHT) = ", np.mean(sim_W_HTHT))
print("E(time to see HHHH) = ", np.mean(sim_W_HHHH))




