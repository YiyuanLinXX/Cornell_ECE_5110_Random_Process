# Define the transition probabilities and rewards for each state-action pair
P = {
    ("healthy", "healthy", "L"): 0.7,
    ("healthy", "minor", "L"): 0.3,
    ("minor", "healthy", "N"): 1,
    ("healthy", "major", "H"): 1,
    ("major", "major", "N"): 0.5,
    ("major", "minor", "N"): 0.5
}

R = {
    ("healthy", "L"): 100,
    ("healthy", "H"): 400,
    ("minor", "N"): 0,
    ("major", "N"): 0
}

# Initialize the value function for each state at time 0
V = {
    "healthy": [0],
    "minor": [0],
    "major": [0]
}

# Initialize the policy dictionary to store the optimal action for each day
policy = {}

# Number of days till retirement
n = 7

# Dynamic programming loop to find the optimal policy and value function
for i in range(1, n+1):
    # Calculate expected rewards for each action when in "healthy" state
    reward_low_risk = R[("healthy", "L")] + P[("healthy", "healthy", "L")] * V["healthy"][i-1] + P[("healthy", "minor", "L")] * V["minor"][i-1]
    reward_high_risk = R[("healthy", "H")] + P[("healthy", "major", "H")] * V["major"][i-1]

    # Store the maximum expected reward and corresponding action for "healthy" state
    if reward_low_risk > reward_high_risk:
        V["healthy"].append(reward_low_risk)
        policy[i] = "L"
    else:
        V["healthy"].append(reward_high_risk)
        policy[i] = "H"

    # Update value function for "minor" and "major" states
    V["minor"].append(V["healthy"][i-1])
    V["major"].append(P[("major", "minor", "N")] * V["minor"][i-1] + P[("major", "major", "N")] * V["major"][i-1])

# Print the optimal policy and value function for each day
for day in range(1, n+1):
    print(f"{day} days till retirement:")
    print(f"Optimal Action: {'Low-Risk Stunt' if policy[day] == 'L' else 'High-Risk Stunt'}")
    print(f"Expected Reward if Healthy: {V['healthy'][day]}")
    print(f"Expected Reward if Minor Injured: {V['minor'][day]}")
    print(f"Expected Reward if Major Injured: {V['major'][day]}")
    print("------")
