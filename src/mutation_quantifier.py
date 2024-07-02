from src.seq_partitioner import partition_seq_length
from src.mutation_and_weight_assignor import assign_mutations
from src.weight_calculator import calculate_subsubregion_weights


def quantify_significant_mutations(seq_length, mutations):
    """
    Quantify significant mutations by calculating positional weights for sub-subregions.

    Args:
    - seq_length (int): Length of the DNA sequence.
    - mutations (list of tuples): List of mutations, each represented as (position, mutation_data).

    Returns:
    - tuple: Two lists containing sub-subregions with their mutations and positional weights for sub-subregions starting at index 0 and index 15.
    """
    # Partition the sequence into sub-subregions starting at index 0 and index 15
    subsubregions_0, subsubregions_15 = partition_seq_length(seq_length)
    
    # Process sub-subregions starting at index 0
    subsubregion_mutations_positional_weights_0 = []
    assigned_mutations_0 = assign_mutations(subsubregions_0, mutations)
    for subsubregion, subsubregion_mutations in assigned_mutations_0:
        positional_weight = calculate_subsubregion_weights(subsubregion, subsubregion_mutations)
        subsubregion_mutations_positional_weights_0.append((subsubregion, subsubregion_mutations, positional_weight))

    # Process sub-subregions starting at index 15
    subsubregion_mutations_positional_weights_15 = []
    assigned_mutations_15 = assign_mutations(subsubregions_15, mutations)
    for subsubregion, subsubregion_mutations in assigned_mutations_15:
        positional_weight = calculate_subsubregion_weights(subsubregion, subsubregion_mutations)
        subsubregion_mutations_positional_weights_15.append((subsubregion, subsubregion_mutations, positional_weight))

    return subsubregion_mutations_positional_weights_0, subsubregion_mutations_positional_weights_15