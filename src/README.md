# Source Directory

This directory contains the source code files for the CEMPI project. Each file is organized by the specific actions and functionalities they perform.

## Overview

In this project, the sequence is partitioned into two sets of sub-subregions: one starting from index 0 and the other starting from index 15. Various functions then assign mutations, weights, distances, and normalization values to each partitioning. Finally, the `subsubregion_combiner.py` file contains functions to combine both sets of sub-subregions.

## File Descriptions

- **seq_partitioner.py**
  - Contains the `partition_seq_length` function, which partitions a given sequence length into sub-subregions of length between 30-45 for further analysis. This function generates two lists of sub-subregions: one starting from index 0 and the other starting from index 15.

- **mutation_and_weight_assignor.py**
  - Contains the `assign_mutations` function, which assigns mutations to their respective sub-subregions.
  - Contains the `assign_positional_weight` function, which calculates the positional weight based on distance.

- **normalizer.py**
  - Contains the `weighted_ave_normalization` function, which normalizes the weighted impact values by calculating their average.

- **weight_calculator.py**
  - Contains the `calculate_subsubregion_weights` function, which calculates the weighted impact for a sub-subregion based on mutations and uses the `assign_positional_weight` and `weighted_ave_normalization` functions for its calculations.

- **mutation_quantifier.py**
  - Contains the `quantify_significant_mutations` function, which quantifies significant mutations by calculating positional weights for subsubregions using the `partition_seq_length`, `assign_mutations`, and `calculate_subsubregion_weights` functions.

- **subsubregion_combiner.py**
  - Contains functions to combine and map weights and mutations from both sets of sub-subregions:
    - `extract_boundaries`
    - `create_combined_intervals`
    - `map_subsubregions_to_intervals`
    - `calculate_overlap_and_combine`
    - `combine_and_map_weights_and_mutations`

- **mutation_file_reader.py**
  - Contains the `read_mutation_data` function, which reads mutation positions and impact scores from a CSV or Excel file and returns a list of tuples or an error message.

- **data_processor.py**
  - Contains the `process_mutation_data` function, which processes mutation data and returns positional weights and combined data.

- **result_writer.py**
  - Contains the `write_results_to_csv` function, which writes data to a CSV file.
  - Contains the `write_processed_data` function, which writes processed data to CSV files.
