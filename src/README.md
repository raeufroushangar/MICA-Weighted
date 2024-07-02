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
  - Contains the following functions:
    - `calculate_subsubregion_weights`: Calculates the weighted impact for a sub-subregion based on mutations.
    - `calculate_subregion_weights`: Calculates the weights for a subregion.
    - `calculate_region_weights`: Calculates the weights for a region.

- **mutation_quantifier.py**
  - Contains the `quantify_significant_mutations` function, which quantifies significant mutations by calculating positional weights for sub-subregions using the `partition_seq_length`, `assign_mutations`, and `calculate_subsubregion_weights` functions.

- **subsubregion_combiner.py**
  - Contains functions to combine and map weights and mutations from both sets of sub-subregions:
    - `extract_boundaries`
    - `create_combined_intervals`
    - `map_subsubregions_to_intervals`
    - `calculate_overlap_and_combine`
    - `combine_and_map_weights_and_mutations`

- **mutation_file_reader.py**
  - Contains the `read_mutation_data` function, which reads mutation positions and impact scores from a CSV file and returns a list of tuples or an error message.

- **data_processor.py**
  - Contains the following functions:
    - `process_mutation_data`: Processes mutation data and returns positional weights and combined data.
    - `process_region_details`: Extracts details for each region, including weights and subregion information.

- **result_writer.py**
  - Contains the following functions:
    - `write_results_to_csv`: Writes data to a CSV file.
    - `write_processed_data`: Writes processed data to CSV files.
    - `write_region_data_to_csv`: Writes region details and region weights to separate CSV files.

- **data_bucketer.py**
  - Contains the following functions:
    - `bucket_subsubregions_to_subregions`: Groups sub-subregions into subregions.
    - `bucket_subregions_to_regions`: Groups subregions into regions.
