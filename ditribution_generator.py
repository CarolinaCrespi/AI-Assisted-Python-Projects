import numpy as np

np.random.seed() 

def adjust_distribution_to_total(distribution: np.ndarray, total: int) -> None:
    """Adjusts the distribution to ensure the sum equals the total."""
    difference = total - np.sum(distribution)
    
    while difference != 0:
        idx = np.random.randint(0, len(distribution))
        if difference > 0:
            distribution[idx] += 1
        elif distribution[idx] > 1:
            distribution[idx] -= 1
        difference = total - np.sum(distribution)

def generate_uniform_distribution(total_agents: int, num_groups: int) -> np.ndarray:
    """Generates a uniform distribution."""
    base_value = total_agents // num_groups
    distribution = np.full(num_groups, base_value)
    
    # Adjust if the division is not exact
    adjust_distribution_to_total(distribution, total_agents)
    return distribution

def generate_scaled_distribution(total_agents: int, num_groups: int, base_distribution: np.ndarray) -> np.ndarray:
    """Generates a distribution by scaling the base distribution."""
    scaling_factor = total_agents / np.sum(base_distribution)
    result = (base_distribution * scaling_factor).astype(int)
    
    # Adjust if the scaling causes rounding issues
    adjust_distribution_to_total(result, total_agents)
    return result

def generate_increasing_distribution(total_agents: int, num_groups: int) -> np.ndarray:
    """Generates an increasing distribution."""
    base_distribution = np.arange(1, num_groups + 1)
    return generate_scaled_distribution(total_agents, num_groups, base_distribution)

def generate_decreasing_distribution(total_agents: int, num_groups: int) -> np.ndarray:
    """Generates a decreasing distribution."""
    base_distribution = np.arange(num_groups, 0, -1)
    return generate_scaled_distribution(total_agents, num_groups, base_distribution)

def generate_random_distribution(total_agents: int, num_groups: int) -> np.ndarray:
    """Generates a random distribution."""
    distribution = np.random.randint(1, total_agents // num_groups + 1, size=num_groups)
    adjust_distribution_to_total(distribution, total_agents)
    return distribution

def generate_pyramidal_distribution(total_agents: int, num_groups: int) -> np.ndarray:
    """Generates a pyramidal distribution."""
    if num_groups % 2 == 0:
        base_distribution = np.concatenate((np.arange(1, num_groups // 2 + 1), np.arange(num_groups // 2, 0, -1)))
    else:
        base_distribution = np.concatenate((np.arange(1, num_groups // 2 + 2), np.arange(num_groups // 2, 0, -1)))
    
    return generate_scaled_distribution(total_agents, num_groups, base_distribution)

# Fixed parameters
total_agents = 200  # Total number of agents
num_groups = 20      # Number of groups

# Generate distributions
uniform = generate_uniform_distribution(total_agents, num_groups)
increasing = generate_increasing_distribution(total_agents, num_groups)
decreasing = generate_decreasing_distribution(total_agents, num_groups)
random = generate_random_distribution(total_agents, num_groups)
pyramidal = generate_pyramidal_distribution(total_agents, num_groups)


# Print distributions
print("Uniform Distribution:", uniform)
print("Increasing Distribution:", increasing)
print("Decreasing Distribution:", decreasing)
print("Pyramidal Distribution:", pyramidal)
print("Random Distribution:", random)

print("Sum of Uniform Distribution:", np.sum(uniform))
print("Sum of Increasing Distribution:", np.sum(increasing))
print("Sum of Decreasing Distribution:", np.sum(decreasing))
print("Sum of Pyramidal Distribution:", np.sum(pyramidal))
print("Sum of Random Distribution:", np.sum(random))