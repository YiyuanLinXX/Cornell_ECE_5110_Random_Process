import numpy as np

# Function to simulate the first n generations of the branching process
def simulate_branching_process(lam, generations):
    Z = [1]  # Start with a single node
    for _ in range(generations):
        # For each node in the current generation,
        # generate the number of children it has using a Poisson distribution
        children = np.random.poisson(lam, Z[-1])
        # Append the total number of children (next generation nodes) to the Z list
        Z.append(sum(children))
    # Return the number of nodes in the last generation
    return Z[-1]

# Function to simulate the branching process until it becomes extinct
def simulate_extinction_time(lam):
    Z = [1]  # Start with a single node
    generation = 0
    # Continue the simulation until the process becomes extinct
    # (i.e., the number of nodes in the current generation is 0)
    while Z[-1] > 0:
        generation += 1
        children = np.random.poisson(lam, Z[-1])
        Z.append(sum(children))
    # Return the generation at which the process became extinct
    return generation

def main():
    # Simulation for lambda = 2
    lam1 = 2
    generations = 5
    simulations = 1000000
    total_nodes = 0

    # Repeat the simulation for the specified number of times
    for _ in range(simulations):
        total_nodes += simulate_branching_process(lam1, generations)

    # Calculate the average number of nodes in the 5th generation
    average_nodes = total_nodes / simulations
    print(f"Lambda = {lam1}:")
    print(f"Average number of nodes at 5th generation: {average_nodes}")
    print("------")

    # Simulation for lambda = 0.5
    lam2 = 0.5
    extinction_times = []

    # Repeat the simulation for the specified number of times
    for _ in range(simulations):
        extinction_times.append(simulate_extinction_time(lam2))

    # Calculate the number of times the process became extinct in the first generation
    extinct_after_1_gen = extinction_times.count(1)
    # Calculate the average time to extinction
    average_extinction_time = sum(extinction_times) / simulations

    print(f"Lambda = {lam2}:")
    print(f"Number of times the process was extinct after 1 generation: {extinct_after_1_gen}")
    print(f"Average time to extinction: {average_extinction_time:.2f}")

# Execute the main function
main()
