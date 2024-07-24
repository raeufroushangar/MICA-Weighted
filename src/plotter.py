import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
    scatter_0 = ax.scatter(mutation_positions_0, weights_0, color='blue', label='Start Index 0', alpha=0.4, s=20)
    scatter_15 = ax.scatter(mutation_positions_15, weights_15, color='green', label='Start Index 15', alpha=0.4, s=20)
    scatter_combined = ax.scatter(combined_positions, combined_weights, color='red', label='Combined', alpha=0.4, s=20)

    # Plot lines connecting the dots for each category
    # Start Index 0
    if mutation_positions_0:
        ax.plot(mutation_positions_0, weights_0, color='blue', linestyle='-', alpha=0.4)

    # Start Index 15
    if mutation_positions_15:
        ax.plot(mutation_positions_15, weights_15, color='green', linestyle='-', alpha=0.4)

    # Combined
    if combined_positions:
        ax.plot(combined_positions, combined_weights, color='red', linestyle='-', alpha=0.4)

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


def plot_density_for_positional_weights(positional_weights_0, positional_weights_15, combined_data, output_dir):
    def extract_plot_data(positional_weights):
        indices = []
        weights = []
        for subsubregion in positional_weights:
            if len(subsubregion) < 3 or not subsubregion[0] or len(subsubregion[0]) < 4:
                continue  # Skip if the sub-subregion does not have the expected format
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
                continue  # Skip if the sub-subregion does not have the expected format
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
    plt.title('Positional Weights Density Plot')
    plt.legend(title='Type')

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_weight_density_plot.png')
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
        region_data.append((start, end, weight, region_detail['region_number']))

        for subregion_detail in region_detail['subregions']:
            # Extract subregion data
            sub_start, sub_end = subregion_detail['subregion_range']
            subregion_weight = subregion_detail['subregion_weight']
            if subregion_weight != 0:
                subregion_data.append((sub_start, sub_end, subregion_weight, region_detail['region_number'], subregion_detail['subregion_number']))

            for subsubregion_detail in subregion_detail['subsubregions']:
                # Extract sub-subregion data
                subsub_start, subsub_end = subsubregion_detail['subsubregion_data'][0]
                subsubregion_weight = subsubregion_detail['subsubregion_data'][2]
                if subsubregion_weight != 0:
                    subsubregion_data.append((subsub_start, subsub_end, subsubregion_weight, region_detail['region_number'], subregion_detail['subregion_number'], subsubregion_detail['subsubregion_number']))
                for mutation in subsubregion_detail['subsubregion_data'][1]:
                    mutation_positions.append(mutation[0])
                    mutation_weights.append(subsubregion_weight)
    
    return subsubregion_data, subregion_data, region_data, mutation_positions, mutation_weights
def add_interval_bars(ax, data, color, label, hierarchy=False):
    for start, end, weight, *numbers in data:
        ax.hlines(weight, start, end, colors=color, alpha=0.4, linewidth=5)
        if hierarchy:
            ax.text((start + end) / 2, weight, f"{numbers[0]},{numbers[1]}", fontsize=7, color=color, ha='center', va='bottom')
        else:
            ax.text((start + end) / 2, weight, f"{numbers[0]}", fontsize=7, color=color, ha='center', va='bottom')

def plot_data(data, label, color, title, output_dir, file_name, hierarchy=False, points=False):
    fig, ax = plt.subplots(figsize=(15, 8))

    if points:
        # Plot points for subsubregions
        for start, end, weight, *numbers in data:
            mid_point = (start + end) / 2
            ax.scatter(mid_point, weight, color=color, alpha=0.4, s=5)
            if hierarchy:
                ax.text(mid_point, weight, f"{numbers[0]},{numbers[1]},{numbers[2]}", fontsize=7, color=color, ha='center', va='bottom')
            else:
                ax.text(mid_point, weight, f"{numbers[-1]}", fontsize=7, color=color, ha='center', va='bottom')
    else:
        # Add interval bars
        add_interval_bars(ax, data, color, label, hierarchy=hierarchy)

    # Custom legend
    handles = [
        plt.Line2D([0], [0], color=color, linewidth=5 if not points else 0, marker='o' if points else '', markersize=3 if points else 0, label=label, alpha=0.4)
    ]

    # Labels and legend
    ax.set_xlabel('Sequence Length')
    ax.set_ylabel('Positional Weight')
    ax.set_title(title)
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, file_name)
    plt.savefig(plot_file)
    plt.close(fig)

def plot_regions_subregions_positional_weights(region_details, output_dir):
    # Extract plot data
    subsubregion_data, subregion_data, region_data, mutation_positions, mutation_weights = extract_plot_data_from_details(region_details)

    # Plotting the data
    fig, ax = plt.subplots(figsize=(15, 8))

    # Add interval bars for regions and subregions
    add_interval_bars(ax, region_data, 'red', 'Region')
    add_interval_bars(ax, subregion_data, 'green', 'Subregion', hierarchy=True)

    # Custom legend
    handles = [
        plt.Line2D([0], [0], color='red', linewidth=5, label='Region', alpha=0.4),
        plt.Line2D([0], [0], color='green', linewidth=5, label='Subregion', alpha=0.4),
    ]

    # Labels and legend
    ax.set_xlabel('Sequence Length')
    ax.set_ylabel('Positional Weight')
    ax.set_title('Positional Weights of Regions, Subregions')
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_weights_of_regions_subregions.png')
    plt.savefig(plot_file)
    plt.close(fig)

def plot_positional_weights(region_details, output_dir):
    # Extract plot data
    subsubregion_data, subregion_data, region_data, mutation_positions, mutation_weights = extract_plot_data_from_details(region_details)

    # Plotting the data
    fig, ax = plt.subplots(figsize=(15, 8))

    # Add interval bars for regions and subregions
    add_interval_bars(ax, region_data, 'red', 'Region')
    add_interval_bars(ax, subregion_data, 'green', 'Region, Subregion', hierarchy=True)

    # Plot points for sub-subregions
    for start, end, weight, *numbers in subsubregion_data:
        mid_point = (start + end) / 2
        ax.scatter(mid_point, weight, color='blue', alpha=0.4, s=5)
        ax.text(mid_point, weight, f"{numbers[0]},{numbers[1]},{numbers[2]}", fontsize=7, color='blue', ha='center', va='bottom')

    # Custom legend
    handles = [
        plt.Line2D([0], [0], color='red', linewidth=5, label='Region', alpha=0.4),
        plt.Line2D([0], [0], color='green', linewidth=5, label='Subregion', alpha=0.4),
        plt.Line2D([0], [0], marker='o', color='blue', markersize=3, label='Sub-subregion', linestyle='', alpha=0.4)
    ]

    # Labels and legend
    ax.set_xlabel('Sequence Length')
    ax.set_ylabel('Positional Weight')
    ax.set_title('Positional Weights of Regions, Subregions, Sub-subregions')
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_weights_of_regions_subregions_subsubregions.png')
    plt.savefig(plot_file)
    plt.close(fig)

    # Generate individual plots
    plot_data(region_data, 'Region', 'red', 'Positional Weights of Regions', output_dir, 'positional_weights_regions.png')
    plot_data(subregion_data, 'Subregion', 'green', 'Positional Weights of Subregions', output_dir, 'positional_weights_subregions.png', hierarchy=True)
    plot_data(subsubregion_data, 'Sub-subregion', 'blue', 'Positional Weights of Sub-subregions', output_dir, 'positional_weights_subsubregions.png', hierarchy=True, points=True)



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
    plot_regions_subregions_positional_weights(region_details, output_dir)

    plot_density_for_positional_weights(positional_weights_0, positional_weights_15, combined_data, output_dir)
    plot_positional_weights(region_details, output_dir)
