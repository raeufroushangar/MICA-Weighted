from src.mutation_file_reader import read_mutation_data
from src.mutation_quantifier import quantify_significant_mutations
from src.subsubregion_combiner import combine_and_map_weights_and_mutations
from src.weight_calculator import calculate_region_weights, calculate_subregion_weights


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


def process_region_details(regions):
    """
    Extract details for each region, including weights and subregion information.

    Args:
    - regions (list): List of regions, where each region is a list of subregions.

    Returns:
    - list: List of dictionaries containing details for each region.
    """
    region_weights = []
    for region in regions:
        region_weight = calculate_region_weights(region)
        region_weights.append(region_weight)

    # Extract region details
    region_details = []
    
    for i, (region, region_weight) in enumerate(zip(regions, region_weights), start=1):
        if not region:
            continue
        start = region[0][0][0][0]
        end = region[-1][-1][0][1]
        subregions_details = []
        for j, subregion in enumerate(region, start=1):
            sub_start = subregion[0][0][0]
            sub_end = subregion[-1][0][1]
            subregion_weight = calculate_subregion_weights(subregion)
            subregions_details.append({
                'subregion_number': j,
                'subregion_range': (sub_start, sub_end),
                'subregion_weight': subregion_weight,
                'subsubregions': subregion
            })
        region_detail = {
            'region_number': i,
            'region_range': (start, end),
            'region_weight': region_weight,
            'subregions': subregions_details
        }
        region_details.append(region_detail)
    
    return region_details


