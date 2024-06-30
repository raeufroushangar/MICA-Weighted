import numpy as np

def weighted_ave_normalization(weighted_impact):
    """
    Normalize the weighted impact values by calculating their average.

    Args:
    - weighted_impact (list or array): A list or array of weighted impact values.

    Returns:
    - float: The normalized value, with NaNs replaced by 0.
    """
    # Calculate the average of the weighted impact values
    normalized_value = np.sum(weighted_impact) / len(weighted_impact)
    
    # Replace NaN values with 0
    return np.nan_to_num(normalized_value)