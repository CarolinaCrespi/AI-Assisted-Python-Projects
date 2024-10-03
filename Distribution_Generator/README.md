**Distribution_Generator.txt**

This folder contains a Python script designed to generate various types of statistical distributions across different groups.

### Python File Overview:
- **Purpose:** The script generates different types of distributions (e.g., uniform, increasing, decreasing, random, pyramidal) for a specified number of agents divided into multiple groups.
  
### Key Functions:
1. **generate_uniform_distribution(total_agents, num_groups):**  
   Generates a uniform distribution where each group has approximately the same number of agents. Any small differences are adjusted to ensure the total number of agents is correct.

2. **generate_increasing_distribution(total_agents, num_groups):**  
   Creates a distribution where the number of agents increases with each group. The groups are scaled to match the total number of agents.

3. **generate_decreasing_distribution(total_agents, num_groups):**  
   Generates a distribution where the number of agents decreases with each group, following a reverse scaling pattern.

4. **generate_random_distribution(total_agents, num_groups):**  
   Produces a random distribution where the number of agents per group varies randomly, while ensuring the total remains as specified.

5. **generate_pyramidal_distribution(total_agents, num_groups):**  
   Forms a pyramidal distribution where the number of agents increases towards the middle groups and then decreases symmetrically. 

### Fixed Parameters:
- **total_agents:** The total number of agents (default is 200).
- **num_groups:** The number of groups into which agents are divided (default is 20).

### How to Use:
1. Run the script in a Python environment.
2. The script automatically generates five different types of distributions (uniform, increasing, decreasing, random, and pyramidal).
3. The generated distributions are arrays representing the number of agents assigned to each group.


