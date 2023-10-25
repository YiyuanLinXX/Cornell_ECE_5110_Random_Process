import random

# Estimate the value of pi using Monte Carlo simulation.
def estimate_pi(num_samples):
    # Initialize a counter for points that fall inside the unit circle.
    inside_circle = 0

    for _ in range(num_samples):
        # Randomly select x and y coordinates from a uniform distribution between -1 and 1.
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        # Calculate the distance of the point from the origin (0,0).
        distance_to_origin = x**2 + y**2
        if distance_to_origin <= 1:  # If the point is inside the unit circle
            inside_circle += 1

    pi_estimate = 4 * (inside_circle / num_samples)
    return pi_estimate

# Simulate the experiment with n samples
n = 10000000
pi_estimate = estimate_pi(n)
print(f"Estimation of pi using",n,"samples:", {pi_estimate})
