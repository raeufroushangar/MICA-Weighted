import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Unable to import Axes3D")

import os
import argparse
from src.data_processor import process_mutation_data, process_region_details
from src.result_writer import write_processed_data, write_region_data_to_csv
from src.data_bucketer import bucket_subsubregions_to_subregions, bucket_subregions_to_regions
from src.plotter import generate_plots
from src.heatmapper import plot_region_heatmap, plot_subregion_heatmap, plot_subsubregion_heatmap

def run_ecmpia_analysis(seq_length, plot=False):
    """
    Run the ECMPIA analysis using the mutations_data.csv file in the current directory.

    Args:
    - seq_length (int): Length of the DNA sequence.
    - plot (bool): Whether to plot the data or not.

    Raises:
    - ValueError: If seq_length is greater than 100000.
    """
    if seq_length > 100000:
        print("Error: Sequence length must not exceed 100000.")
        return

    # Define the path to the mutations_data.csv file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mutation_file_path = os.path.join(current_dir, 'mutations_data.csv')
    result_dir = os.path.join(current_dir, "ECMPIA_result")
    region_details_file_path = os.path.join(result_dir, 'region_details.csv')
    region_weights_file_path = os.path.join(result_dir, 'region_weights.csv')

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

            # Generate and save plots if the plot argument is True
            if plot:
                generate_plots(positional_weights_0_data, positional_weights_15_data, combined_data_csv, region_details, result_dir)
                plot_region_heatmap(region_weights_file_path, result_dir)
                plot_subregion_heatmap(region_details_file_path, result_dir)
                plot_subsubregion_heatmap(region_details_file_path, result_dir)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ECMPIA analysis on mutation data.")
    parser.add_argument('-l', '--length', type=int, required=True, help="Length of the DNA sequence")
    parser.add_argument('--plot', action='store_true', help="Option to plot the data")
    args = parser.parse_args()

    run_ecmpia_analysis(args.length, args.plot)
