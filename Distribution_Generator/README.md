# Distribution Generator

This folder contains a Python script designed to generate various types of distributions across different groups based on a specified total value.

## Python File Overview

- **Purpose:**  
  The script generates different types of distributions (e.g., uniform, increasing, decreasing, random, pyramidal) for a specified total value divided across multiple groups.

## Key Functions

1. **`generate_uniform_distribution(value, num_groups)`**  
   Generates a uniform distribution where each group receives approximately the same portion of the total value. Any small differences are adjusted to ensure the total is accurate.

2. **`generate_increasing_distribution(value, num_groups)`**  
   Creates an increasing distribution where each group receives a progressively larger portion of the total value. The distribution is scaled to match the total value.

3. **`generate_decreasing_distribution(value, num_groups)`**  
   Produces a decreasing distribution where each group receives a progressively smaller portion of the total value. The groups are scaled to maintain accuracy.

4. **`generate_random_distribution(value, num_groups)`**  
   Generates a random distribution where the portions vary randomly between groups, while ensuring that the total matches the specified value.

5. **`generate_pyramidal_distribution(value, num_groups)`**  
   Forms a pyramidal distribution where the values increase towards the middle groups and then symmetrically decrease, ensuring the total value remains correct.

## Fixed Parameters

- **`value`:** The total value to be distributed (default is 200).
- **`num_groups`:** The number of groups (default is 20).

## How to Use

1. Run the script in a Python environment.
2. The script automatically generates five different types of distributions: uniform, increasing, decreasing, random, and pyramidal.
3. The generated distributions are arrays representing the portion of the total value assigned to each group.
4. The script also prints the sum of the values in each distribution to verify accuracy.



