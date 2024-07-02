import os
import argparse
import numpy as np
import pandas as pd
from src.data_processor import process_mutation_data, process_region_details
from src.result_writer import write_processed_data, write_region_data_to_csv
from src.data_bucketer import bucket_subsubregions_to_subregions, bucket_subregions_to_regions

def run_cempi_analysis(seq_length):
    """
    Run the CEMPI analysis using the mutations_data.csv file in the current directory.

    Args:
    - seq_length (int): Length of the DNA sequence.
    """
    # Define the path to the mutations_data.csv file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mutation_file_path = os.path.join(current_dir, 'mutations_data.csv')

    try:
        # Process mutation data
        positional_weights_0_data, positional_weights_15_data, combined_data_csv = process_mutation_data(mutation_file_path, seq_length)

        # Write processed data to CSV files if processing was successful
        if positional_weights_0_data is not None and positional_weights_15_data is not None and combined_data_csv is not None:
            write_processed_data(mutation_file_path, positional_weights_0_data, positional_weights_15_data, combined_data_csv)
            
            # Call the bucket_subsubregions_to_subregions function
            subregions = bucket_subsubregions_to_subregions(combined_data_csv)

            # Call the bucket_subregions_to_regions function
            regions = bucket_subregions_to_regions(subregions)
            
            # Process region details
            region_details = process_region_details(regions)

            # Write region details and region weights to CSV
            write_region_data_to_csv(region_details, mutation_file_path)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run CEMPI analysis on mutation data.")
    parser.add_argument('-l', '--length', type=int, required=True, help="Length of the DNA sequence")
    args = parser.parse_args()

    run_cempi_analysis(args.length)
