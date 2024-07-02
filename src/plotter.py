import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def extract_plot_data(positional_weights):
    mutation_positions = []
    weights = []
    for subsubregion in positional_weights:
        start = subsubregion[0][2]
        end = subsubregion[0][3]
        weight = subsubregion[2]
        for mutation in subsubregion[1]:
            mutation_positions.append(mutation[0])
            weights.append(weight)
    return mutation_positions, weights

def plot_positional_weights_by_mutation_positions(positional_weights_0, positional_weights_15, combined_data, output_dir):
    mutation_positions_0, weights_0 = extract_plot_data(positional_weights_0)
    mutation_positions_15, weights_15 = extract_plot_data(positional_weights_15)

    combined_positions = []
    combined_weights = []
    for interval, mutations, weight in combined_data:
        for mutation in mutations:
            combined_positions.append(mutation[0])
            combined_weights.append(weight)

    # Plotting the data
    fig, ax = plt.subplots(figsize=(15, 8))

    # Scatter plot for mutation positions and positional weights
    scatter_0 = ax.scatter(mutation_positions_0, weights_0, color='blue', label='Start Index 0', alpha=0.7, s=20)
    scatter_15 = ax.scatter(mutation_positions_15, weights_15, color='green', label='Start Index 15', alpha=0.7, s=20)
    scatter_combined = ax.scatter(combined_positions, combined_weights, color='red', label='Combined', alpha=0.7, s=20)

    # Plot lines connecting the dots for each category
    # Start Index 0
    if mutation_positions_0:
        ax.plot(mutation_positions_0, weights_0, color='blue', linestyle='-', alpha=0.7)

    # Start Index 15
    if mutation_positions_15:
        ax.plot(mutation_positions_15, weights_15, color='green', linestyle='-', alpha=0.7)

    # Combined
    if combined_positions:
        ax.plot(combined_positions, combined_weights, color='red', linestyle='-', alpha=0.7)

    # Function to add labels and prevent overlap
    def add_labels_with_prevention(ax, positions, weights, color):
        y_positions = []
        for i, (pos, weight) in enumerate(zip(positions, weights)):
            y = weight + 0.01
            while any(abs(y - prev_y) < 0.01 for prev_y in y_positions):
                y += 0.01
            y_positions.append(y)
            ax.text(pos, y, str(pos), fontsize=9, color=color, ha='center', va='bottom')

    # Add labels for each dot with overlap prevention
    add_labels_with_prevention(ax, mutation_positions_0, weights_0, 'blue')
    add_labels_with_prevention(ax, mutation_positions_15, weights_15, 'green')
    add_labels_with_prevention(ax, combined_positions, combined_weights, 'red')

    # Custom legend
    handles = [
        plt.Line2D([0], [0], marker='o', color='blue', markersize=10, label='Start Index 0', linestyle='-'),
        plt.Line2D([0], [0], marker='o', color='green', markersize=10, label='Start Index 15', linestyle='-'),
        plt.Line2D([0], [0], marker='o', color='red', markersize=10, label='Combined', linestyle='-')
    ]

    # Labels and legend
    ax.set_xlabel('Mutation Position')
    ax.set_ylabel('Positional Weight')
    ax.set_title('Positional Weights by Mutation Positions')
    ax.legend(handles=handles)

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_weights_by_mutation_positions.png')
    plt.savefig(plot_file)
    plt.close(fig)

def plot_positional_weights_by_subsubregion_ranges(positional_weights_0, positional_weights_15, combined_data, output_dir):
    def extract_plot_data(positional_weights):
        subregion_intervals = []
        mutation_positions = []
        weights = []
        for subsubregion in positional_weights:
            start = subsubregion[0][2]
            end = subsubregion[0][3]
            weight = subsubregion[2]
            if weight != 0:  # Filter out zero weights
                interval_label = f"{start}-{end}"
                subregion_intervals.append((start, end, weight, interval_label))
                for mutation in subsubregion[1]:
                    mutation_positions.append(mutation[0])
                    weights.append(weight)
        return subregion_intervals, mutation_positions, weights

    subregion_intervals_0, mutation_positions_0, weights_0 = extract_plot_data(positional_weights_0)
    subregion_intervals_15, mutation_positions_15, weights_15 = extract_plot_data(positional_weights_15)

    combined_intervals = []
    combined_positions = []
    combined_weights = []
    for interval, mutations, weight in combined_data:
        if weight != 0:  # Filter out zero weights
            start, end = interval
            interval_label = f"{start}-{end}"
            combined_intervals.append((start, end, weight, interval_label))
            for mutation in mutations:
                combined_positions.append(mutation[0])
                combined_weights.append(weight)

    # Plotting the data
    fig, ax = plt.subplots(figsize=(15, 8))

    # Function to add labels and prevent overlap
    def add_labels_with_prevention(ax, intervals, color):
        last_position = None
        for start, end, weight, label in intervals:
            position = (start + end) / 2
            y = weight
            if last_position is not None and abs(position - last_position) < 5:
                position += 10 - abs(position - last_position)
            ax.hlines(weight, start, end, colors=color, alpha=0.4)
            ax.text(position, y, label, fontsize=9, color=color, ha='center', va='bottom')
            last_position = position

    # Plot lines for subregion intervals and add labels with overlap prevention
    add_labels_with_prevention(ax, subregion_intervals_0, 'blue')
    add_labels_with_prevention(ax, subregion_intervals_15, 'green')
    add_labels_with_prevention(ax, combined_intervals, 'red')

    # Scatter plot for mutation positions and positional weights
    ax.scatter(mutation_positions_0, weights_0, color='blue', label='Start Index 0', alpha=0.7)
    ax.scatter(mutation_positions_15, weights_15, color='green', label='Start Index 15', alpha=0.7)
    ax.scatter(combined_positions, combined_weights, color='red', label='Combined', alpha=0.7)

    # Plot lines connecting the dots for each category
    # Start Index 0
    if mutation_positions_0:
        ax.plot(mutation_positions_0, weights_0, color='blue', linestyle='-', alpha=0.7)

    # Start Index 15
    if mutation_positions_15:
        ax.plot(mutation_positions_15, weights_15, color='green', linestyle='-', alpha=0.7)

    # Combined
    if combined_positions:
        ax.plot(combined_positions, combined_weights, color='red', linestyle='-', alpha=0.7)

    # Custom legend
    handles = [
        plt.Line2D([0], [0], marker='o', color='blue', markersize=10, label='Start Index 0', linestyle='-'),
        plt.Line2D([0], [0], marker='o', color='green', markersize=10, label='Start Index 15', linestyle='-'),
        plt.Line2D([0], [0], marker='o', color='red', markersize=10, label='Combined', linestyle='-')
    ]

    # Labels and legend
    ax.set_xlabel('Sub-subregions')
    ax.set_ylabel('Positional Weight')
    ax.set_title('Positional Weights by Sub-subregion Ranges')
    ax.legend(handles=handles)

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_weights_by_subsubregion_ranges.png')
    plt.savefig(plot_file)
    plt.close(fig)

def plot_density_for_positional_weights(positional_weights_0, positional_weights_15, combined_data, output_dir):
    def extract_plot_data(positional_weights):
        indices = []
        weights = []
        for subsubregion in positional_weights:
            if len(subsubregion) < 3 or not subsubregion[0] or len(subsubregion[0]) < 4:
                continue  # Skip if the subsubregion does not have the expected format
            start, end = subsubregion[0][2], subsubregion[0][3]
            weight = subsubregion[2]
            indices.extend(range(start, end + 1))
            weights.extend([weight] * (end - start + 1))
        return indices, weights

    def extract_combined_plot_data(combined_data):
        indices = []
        weights = []
        for subsubregion in combined_data:
            if len(subsubregion) < 3:
                continue  # Skip if the subsubregion does not have the expected format
            start, end = subsubregion[0][0], subsubregion[0][1]
            weight = subsubregion[2]
            indices.extend(range(start, end + 1))
            weights.extend([weight] * (end - start + 1))
        return indices, weights

    # Extract data for plotting
    indices_0, weights_0 = extract_plot_data(positional_weights_0)
    indices_15, weights_15 = extract_plot_data(positional_weights_15)
    indices_combined, weights_combined = extract_combined_plot_data(combined_data)

    # Combine data into DataFrames for plotting with Seaborn
    data_0 = pd.DataFrame({'Index': indices_0, 'Weight': weights_0, 'Type': 'Start Index 0'})
    data_15 = pd.DataFrame({'Index': indices_15, 'Weight': weights_15, 'Type': 'Start Index 15'})
    data_combined = pd.DataFrame({'Index': indices_combined, 'Weight': weights_combined, 'Type': 'Combined'})

    # Plot the data
    plt.figure(figsize=(15, 8))

    # KDE plot with less dense colors (more transparent)
    sns.kdeplot(data=data_0, x='Index', weights='Weight', fill=True, color='blue', label='Start Index 0', alpha=0.2)
    sns.kdeplot(data=data_15, x='Index', weights='Weight', fill=True, color='green', label='Start Index 15', alpha=0.2)
    sns.kdeplot(data=data_combined, x='Index', weights='Weight', fill=True, color='red', label='Combined', alpha=0.2)

    # Labels and legend
    plt.xlabel('Sub-subregions')
    plt.ylabel('Density')
    plt.title('Density Plot for Positional Weights')
    plt.legend(title='Type')

    # Save the plot
    plot_file = os.path.join(output_dir, 'density_plot_for_positional_weights.png')
    plt.savefig(plot_file)
    plt.close()

def extract_plot_data_from_details(region_details):
    subsubregion_data = []
    subregion_data = []
    region_data = []
    mutation_positions = []
    mutation_weights = []

    for region_detail in region_details:
        # Extract region data
        start, end = region_detail['region_range']
        weight = region_detail['region_weight']
        region_data.append((start, end, weight))

        for subregion_detail in region_detail['subregions']:
            # Extract subregion data
            sub_start, sub_end = subregion_detail['subregion_range']
            subregion_weight = subregion_detail['subregion_weight']
            if subregion_weight != 0:
                subregion_data.append((sub_start, sub_end, subregion_weight))

            for subsubregion in subregion_detail['subsubregions']:
                if len(subsubregion) < 3:
                    continue
                # Extract sub-subregion data
                subsub_start, subsub_end = subsubregion[0][0], subsubregion[0][1]
                subsub_weight = subsubregion[2]
                if subsub_weight != 0:
                    subsubregion_data.append((subsub_start, subsub_end, subsub_weight))
                for mutation in subsubregion[1]:
                    mutation_positions.append(mutation[0])
                    mutation_weights.append(subsub_weight)
    
    return subsubregion_data, subregion_data, region_data, mutation_positions, mutation_weights


# Function to add interval bars and labels
def add_interval_bars(ax, data, color, label):
    for start, end, weight in data:
        ax.hlines(weight, start, end, colors=color, alpha=0.4, linewidth=5)
        ax.text((start + end) / 2, weight, f"{start}-{end}", fontsize=9, color=color, ha='center', va='bottom')

# Function to add labels and prevent overlap
def add_labels_with_prevention(ax, positions, weights, color):
    y_positions = []
    for i, (pos, weight) in enumerate(zip(positions, weights)):
        y = weight + 0.02
        while any(abs(y - prev_y) < 0.00 for prev_y in y_positions):
            y += 0.05
        y_positions.append(y)
        ax.text(pos, y, str(pos), fontsize=9, color=color, ha='center', va='bottom')

def plot_positional_weights(region_details, output_dir):
    # Extract plot data
    subsubregion_data, subregion_data, region_data, mutation_positions, mutation_weights = extract_plot_data_from_details(region_details)

    # Plotting the data
    fig, ax = plt.subplots(figsize=(15, 8))

    # Add interval bars for regions, subregions, and sub-subregions
    add_interval_bars(ax, region_data, 'red', 'Regions')
    add_interval_bars(ax, subregion_data, 'green', 'Subregions')
    add_interval_bars(ax, subsubregion_data, 'blue', 'Sub-subregions')

    # Scatter plot for mutation positions and positional weights
    scatter_mutations = ax.scatter(mutation_positions, mutation_weights, color='purple', label='Mutations', alpha=0.7, s=1)

    # Add labels for mutation points with overlap prevention
    add_labels_with_prevention(ax, mutation_positions, mutation_weights, 'purple')

    # Custom legend
    handles = [
        plt.Line2D([0], [0], color='red', linewidth=5, label='Regions', alpha=0.4),
        plt.Line2D([0], [0], color='green', linewidth=5, label='Subregions', alpha=0.4),
        plt.Line2D([0], [0], color='blue', linewidth=5, label='Sub-subregions', alpha=0.4),
        plt.Line2D([0], [0], marker='o', color='purple', markersize=5, label='Mutations', linestyle='')
    ]

    # Labels and legend
    ax.set_xlabel('Regions, Subregions, Sub-subregions')
    ax.set_ylabel('Positional Weight')
    ax.set_title('Positional Weights of Regions, Subregions, Sub-subregions')
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_weights_of_regions_subregions_subsubregions.png')
    plt.savefig(plot_file)
    plt.close(fig)

def generate_plots(positional_weights_0, positional_weights_15, combined_data, region_details, output_dir):
    """
    Generate and save all plots to the specified output directory.

    Args:
    - positional_weights_0: Positional weights starting from index 0
    - positional_weights_15: Positional weights starting from index 15
    - combined_data: Combined positional weights data
    - region_details: Detailed information about regions, subregions, and sub-subregions
    - output_dir: Directory to save the plots
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plot_positional_weights_by_mutation_positions(positional_weights_0, positional_weights_15, combined_data, output_dir)
    plot_positional_weights_by_subsubregion_ranges(positional_weights_0, positional_weights_15, combined_data, output_dir)
    plot_density_for_positional_weights(positional_weights_0, positional_weights_15, combined_data, output_dir)
    plot_positional_weights(region_details, output_dir)
