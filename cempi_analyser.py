from src.data_processor import process_mutation_data
from src.result_writer import write_processed_data

mutation_file_path = '/home/raeuf/projects/CEMPI/mutations_data.csv'
seq_length = 100
output_dir = '/home/raeuf/projects/CEMPI'

try:
    # Process mutation data
    positional_weights_0_data, positional_weights_15_data, combined_data_csv = process_mutation_data(mutation_file_path, seq_length)

    # Write processed data to CSV files if processing was successful
    if positional_weights_0_data is not None and positional_weights_15_data is not None and combined_data_csv is not None:
        write_processed_data(output_dir, positional_weights_0_data, positional_weights_15_data, combined_data_csv)
except ValueError as e:
    print(e)
