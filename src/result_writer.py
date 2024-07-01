import os
import pandas as pd

def write_results_to_csv(file_path, data, headers):
    """
    Write data to a CSV file.

    Args:
    - file_path (str): Path to the output file.
    - data (list): List of data to write.
    - headers (list): List of headers for the CSV file.
    """
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(file_path, index=False)

def write_processed_data(output_dir, positional_weights_0_data, positional_weights_15_data, combined_data_csv):
    """
    Write processed data to CSV files.

    Args:
    - output_dir (str): Directory to save the output CSV files.
    - positional_weights_0_data (list): Data for positional weights starting at index 0.
    - positional_weights_15_data (list): Data for positional weights starting at index 15.
    - combined_data_csv (list): Combined and mapped sub-subregions data.
    """
    # Define file paths
    positional_weights_0_file = os.path.join(output_dir, "positional_weights_0.csv")
    positional_weights_15_file = os.path.join(output_dir, "positional_weights_15.csv")
    combined_data_file = os.path.join(output_dir, "combined_data.csv")

    # Write results to CSV files
    write_results_to_csv(positional_weights_0_file, positional_weights_0_data, ['Sub-subregion', 'Mutations', 'Positional Weight'])
    write_results_to_csv(positional_weights_15_file, positional_weights_15_data, ['Sub-subregion', 'Mutations', 'Positional Weight'])
    write_results_to_csv(combined_data_file, combined_data_csv, ['Interval', 'Mutations', 'Average Weight'])
