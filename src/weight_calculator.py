import numpy as np
from src.mutation_and_weight_assignor import assign_positional_weight
from src.normalizer import weighted_ave_normalization  # Updated import

def calculate_subsubregion_weights(subsubregion, subsubregion_mutations):
    """
    Calculate the weighted impact for a subsubregion based on mutations.

    Args:
    - subsubregion (list): A subsubregion represented as [subsubregion_number, length, start_index, end_index].
    - subsubregion_mutations (list of tuples): Mutations within the subsubregion, each represented as (position, impact).

    Returns:
    - float: The normalized weighted impact for the subsubregion.
    """
    total_positional_weighted_impact = 0

    # Return 0 if no mutations are found in the subsubregion
    if not subsubregion_mutations:
        return 0

    for pos, impact in subsubregion_mutations:
        # Calculate the distance from the mutation position to each position in the subsubregion
        distance = np.abs(np.arange(subsubregion[2], subsubregion[3] + 1) - pos)
        # Calculate positional weights based on the distance
        positional_weights = assign_positional_weight(distance)
        # Calculate the positional weighted impact
        positional_weighted_impact = positional_weights * impact
        # Accumulate the total positional weighted impact
        total_positional_weighted_impact += positional_weighted_impact

    # Normalize the total positional weighted impact
    subsubregion_normalized_weighted_impact = weighted_ave_normalization(total_positional_weighted_impact)
    return subsubregion_normalized_weighted_impact
