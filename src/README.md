# Source Directory

This directory contains the source code files for the CEMPI project. Each file is organized by the specific actions and functionalities they perform.

## File Descriptions

- **seq_partitioner.py**
  - Contains the `partition_seq_length` function, which partitions a given sequence length into sub-subregions of length between 30-45 for further analysis.

- **mutation_and_weight_assignor.py**
  - Contains the `assign_mutations` function, which assigns mutations to their respective sub-subregions.
  - Contains the `assign_positional_weight` function, which calculates the positional weight based on distance.

- **normalization.py**
  - Contains the `weighted_ave_normalization` function, which normalizes the weighted impact values by calculating their average.

- **weight_calculator.py**
  - Contains the `calculate_subsubregion_weights` function, which calculates the weighted impact for a sub-subregion based on mutations and uses the `assign_positional_weight` and `weighted_ave_normalization` functions for its calculations.
