from src.mutation_file_reader import read_mutation_data
from src.mutation_quantifier import quantify_significant_mutations
from src.subsubregion_combiner import combine_and_map_weights_and_mutations

def process_mutation_data(mutation_file_path, seq_length):
    """
    Process mutation data and return positional weights and combined data.

    Args:
    - mutation_file_path (str): Path to the input mutation data file.
    - seq_length (int): Length of the DNA sequence.

    Returns:
    - tuple: (positional_weights_0_data, positional_weights_15_data, combined_data)
    """
    # Read mutation data
    mutations = read_mutation_data(mutation_file_path)

    if isinstance(mutations, list):
        # Quantify significant mutations
        positional_weights_0, positional_weights_15 = quantify_significant_mutations(seq_length, mutations)
        
        # Prepare data for returning
        positional_weights_0_data = [
            [subsubregion[0], subsubregion[1], subsubregion[2]] for subsubregion in positional_weights_0
        ]
        positional_weights_15_data = [
            [subsubregion[0], subsubregion[1], subsubregion[2]] for subsubregion in positional_weights_15
        ]
        combined_data = combine_and_map_weights_and_mutations(positional_weights_0, positional_weights_15)
        combined_data_csv = [
            [interval, mutations, weight] for interval, mutations, weight in combined_data
        ]

        return positional_weights_0_data, positional_weights_15_data, combined_data_csv
    else:
        raise ValueError(mutations)
