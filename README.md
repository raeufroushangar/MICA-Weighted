# CEMPI (Contextual Encoding of Mutations Positional Impact)

CEMPI is a repository for implementing a set of algorithms related to the contextual encoding of mutations and their positional impact in a sequence.

## Project Description

CEMPI integrates partitioning and clustering algorithms to capture mutation positions (bases and regions) and their impact across DNA/RNA/protein sequences. The repository serves as a toolkit for bioinformaticians and researchers.

## Directory Structure

- `src`: Contains source code files.
- `mutations_data.csv`: Sample CSV file containing mutation data.

## mutations_data.csv

This file contains sample mutation data with the following columns:
- `mut_positions` (integer): Mutation positions in the sequence.
- `impact_score` (float or integer): Impact score of the mutations.

You should replace the data in this file with your own mutation data before running the analysis.

## CEMPI_result

This directory contains the output results from the algorithm. The following files are generated:
- `positional_weights_0.csv`: Contains mapped mutations and calculated positional weights data for sub-subregions generated from sequence partitioned starting at index 0.
- `positional_weights_15.csv`: Contains mapped mutations and calculated positional weights data for sub-subregions generated from sequence partitioned starting at index 15.
- `combined_data.csv`: Contains combined data from both sets of sub-subregions partitioned.

## System Requirements

- macOS 10.15 or higher / Windows 10 or higher / Linux
- Python 3.9 or higher
- pip3 24
- *May work with similar versions.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/raeufroushangar/CEMPI.git
   cd CEMPI

2. Install required packages:
   ```bash
   pip install -r requirements.txt

3. Run analysis script:
   ```bash
   python3 cempi_main.py -l <sequence_length>

   note: Replace <sequence_length> with the length of your DNA sequence. For example:
   python3 cempi_main.py -l 100
