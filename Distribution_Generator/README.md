# Distribution Generator

This folder contains multiple Python scripts, each designed to generate a specific type of distribution across different groups based on a specified total number of objects.

## Python Scripts Overview

Each script focuses on a particular distribution type, allowing you to generate different distributions for a specified number of objects divided across multiple groups.

### Available Distribution Types

1. **Uniform Distribution:**  
   In the script `uniform_distribution.py`, this function generates a uniform distribution where each group receives approximately the same portion of the total number of objects. Small differences are adjusted to ensure the total is correct.

2. **Increasing Distribution:**  
   In the script `increasing_distribution.py`, this function creates a distribution where each group receives a progressively larger portion of the total number of objects. The distribution is scaled to match the total number of objects.

3. **Decreasing Distribution:**  
   In the script `decreasing_distribution.py`, this function generates a distribution where each group receives a progressively smaller portion of the total number of objects, ensuring accuracy in the total.

4. **Random Distribution:**  
   In the script `random_distribution.py`, this function generates a random distribution where the portions vary randomly between groups while ensuring the total matches the specified number of objects.

5. **Pyramidal Distribution:**  
   In the script `pyramidal_distribution.py`, this function forms a pyramidal distribution where the number of objects increases towards the middle groups and then symmetrically decreases, ensuring the total number of objects is correct.

## Parameters

- **`number_of_objects`:** The total number of objects to be distributed (default is 200).
- **`num_groups`:** The number of groups (default is 20).

## How to Use

1. Run the desired script in a Python environment.
2. Each script will generate a specific type of distribution (uniform, increasing, decreasing, random, or pyramidal).
3. The script will output an array representing the portion of the total number of objects assigned to each group and print the sum of the objects in the distribution to verify accuracy.
