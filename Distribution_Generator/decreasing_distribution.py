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


def generate_scaled_distribution(num_objects: int, num_groups: int, base_distribution: np.ndarray) -> np.ndarray:
    """Generates a distribution by scaling the base distribution."""
    scaling_factor = num_objects / np.sum(base_distribution)
    result = (base_distribution * scaling_factor).astype(int)
    
    # Adjust if the scaling causes rounding issues
    adjust_distribution_to_total(result, num_objects)
    return result


def generate_decreasing_distribution(num_objects: int, num_groups: int) -> np.ndarray:
    """Generates a decreasing distribution."""
    base_distribution = np.arange(num_groups, 0, -1)
    return generate_scaled_distribution(num_objects, num_groups, base_distribution)


# Fixed parameters
num_objects = 200          # Number of objects
num_groups = 20      # Number of groups

# Generate distributions
decreasing = generate_decreasing_distribution(num_objects, num_groups)



# Print distributions
print("Decreasing Distribution:", decreasing)
print("Sum of Decreasing Distribution:", np.sum(decreasing))
