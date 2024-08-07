import os
import pandas as pd

def write_results_to_csv(file_path, data, headers):
    """
    Write data to a CSV file, creating a new directory each time.

    Args:
    - file_path (str): Path to the output file.
    - data (list): List of data to write.
    - headers (list): List of headers for the CSV file.
    """
    # Create directory, assuming it does not exist
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)

    # Write data to CSV
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(file_path, index=False)


def write_processed_data(result_dir, positional_weights_0_data, positional_weights_15_data, combined_data_csv):
    """
    Write processed data to CSV files in the specified result directory.

    Args:
    - result_dir (str): Path to the directory where the results will be stored.
    - positional_weights_0_data (list): Data for positional weights starting at index 0.
    - positional_weights_15_data (list): Data for positional weights starting at index 15.
    - combined_data_csv (list): Combined and mapped sub-subregions data.
    """
    # Define file paths
    positional_weights_0_file = os.path.join(result_dir, "positional_weights_0.csv")
    positional_weights_15_file = os.path.join(result_dir, "positional_weights_15.csv")
    combined_data_file = os.path.join(result_dir, "combined_data.csv")

    # Write results to CSV files
    write_results_to_csv(positional_weights_0_file, positional_weights_0_data, ['Sub-subregion', 'Mutations', 'Positional Weight'])
    write_results_to_csv(positional_weights_15_file, positional_weights_15_data, ['Sub-subregion', 'Mutations', 'Positional Weight'])
    write_results_to_csv(combined_data_file, combined_data_csv, ['Interval', 'Mutations', 'Average Weight'])

def write_region_data_to_csv(result_dir, region_details):
    """
    Write region details and region weights to CSV files in the specified result directory.

    Args:
    - result_dir (str): Path to the directory where the results will be stored.
    - region_details (list): List of region details to write.
    """
    # Define file paths for region details and region weights
    region_details_file = os.path.join(result_dir, "region_details.csv")
    region_weights_file = os.path.join(result_dir, "region_weights.csv")

    # Prepare the data for region details
    region_details_data = []
    for detail in region_details:
        region_number = detail['region_number']
        region_range = detail['region_range']
        region_weight = detail['region_weight']
        for subregion_detail in detail['subregions']:
            subregion_number = subregion_detail['subregion_number']
            subregion_range = subregion_detail['subregion_range']
            subregion_weight = subregion_detail['subregion_weight']

            for subsubregion_detail in subregion_detail['subsubregions']:
                subsubregion_number = subsubregion_detail['subsubregion_number']
                subsubregion_data = subsubregion_detail['subsubregion_data']
                subsubregion_range = tuple(subsubregion_data[0])
                subsubregion_weight = subsubregion_data[2]
                region_details_data.append([
                    region_number, region_range, region_weight,
                    subregion_number, subregion_range, subregion_weight,
                    subsubregion_number, subsubregion_range, subsubregion_weight
                ])
    
    # Write region details to CSV
    write_results_to_csv(region_details_file, region_details_data, [
        'Region Number', 
        'Region Range', 
        'Region Weight',
        'Subregion Number', 
        'Subregion Range', 
        'Subregion Weight',
        'Subsubregion Number',
        'Subsubregion Range', 
        'Subsubregion Weight'
    ])

    # Prepare the data for region weights
    region_weights_data = [
        [detail['region_number'], detail['region_range'], detail['region_weight']]
        for detail in region_details
    ]
    
    # Write region weights to CSV
    write_results_to_csv(region_weights_file, region_weights_data, [
        'Region Number', 'Region Range', 'Region Weight'
    ])
