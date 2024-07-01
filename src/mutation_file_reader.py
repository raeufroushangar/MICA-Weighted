import os
import pandas as pd

def read_mutation_data(file_path):
    """
    Read mutation positions and impact scores from a CSV file.

    Args:
    - file_path (str): Path to the input CSV file.

    Returns:
    - list of tuples: List of (mutation_position, impact_score) tuples if successful.
    - str: Error message if any issue occurs.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            return f"File not found: {file_path}"
        
        # Check if the file path is a file
        if not os.path.isfile(file_path):
            return "File not found."
        
        # Check the file extension to ensure it is a CSV file
        if not file_path.endswith('.csv'):
            return "Invalid file format. Only CSV files are supported."

        # Read the CSV file
        df = pd.read_csv(file_path, keep_default_na=False)
        
        # Check if the DataFrame has the required columns
        if 'mut_positions' not in df.columns or 'impact_score' not in df.columns:
            return "Parsing error. The file must contain 'mut_positions' and 'impact_score' columns."
        
        # Replace empty cells with None
        df.replace('', None, inplace=True)
        
        # Check if the DataFrame is empty
        if df.empty:
            return "File is empty."
        
        # Extract mutation positions and impact scores as a list of tuples
        mutations = list(df[['mut_positions', 'impact_score']].itertuples(index=False, name=None))
        
        return mutations
    
    except pd.errors.ParserError:
        return "Parsing error. Please check the file format and content."
    except Exception as e:
        return f"{str(e)}"
