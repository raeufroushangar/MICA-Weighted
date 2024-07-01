import os
import pandas as pd

def write_results_to_csv(file_path, data, headers):
    """
    Write data to a CSV file, creating the directory if it doesn't exist.

    Args:
    - file_path (str): Path to the output file.
    - data (list): List of data to write.
    - headers (list): List of headers for the CSV file.
    """
    # Create directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write data to CSV
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(file_path, index=False)

def write_processed_data(mutation_file_path, positional_weights_0_data, positional_weights_15_data, combined_data_csv):
    """
    Write processed data to CSV files in the CEMPI_result directory.

    Args:
    - mutation_file_path (str): Path to the input mutation data file.
    - positional_weights_0_data (list): Data for positional weights starting at index 0.
    - positional_weights_15_data (list): Data for positional weights starting at index 15.
    - combined_data_csv (list): Combined and mapped sub-subregions data.
    """
    # Derive the output directory from the mutation file path
    base_dir = os.path.dirname(mutation_file_path)
    result_dir = os.path.join(base_dir, "CEMPI_result")
    
    # Define file paths
    positional_weights_0_file = os.path.join(result_dir, "positional_weights_0.csv")
    positional_weights_15_file = os.path.join(result_dir, "positional_weights_15.csv")
    combined_data_file = os.path.join(result_dir, "combined_data.csv")

    # Write results to CSV files
    write_results_to_csv(positional_weights_0_file, positional_weights_0_data, ['Sub-subregion', 'Mutations', 'Positional Weight'])
    write_results_to_csv(positional_weights_15_file, positional_weights_15_data, ['Sub-subregion', 'Mutations', 'Positional Weight'])
    write_results_to_csv(combined_data_file, combined_data_csv, ['Interval', 'Mutations', 'Average Weight'])