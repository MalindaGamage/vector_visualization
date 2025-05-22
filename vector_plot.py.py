"""
Vector Visualization Script

This script visualizes 2D vectors using Matplotlib and NumPy.
It creates a plot showing vectors as arrows from the origin.
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_vectors(vectors, colors, labels, output_file='output/vector_plot.png'):
    """
    Plot 2D vectors as arrows from the origin.

    Parameters:
        vectors (list of np.array): List of vectors to plot
        colors (list of str): Colors for each vector
        labels (list of str): Labels for each vector
        output_file (str): Path to save the output image
    """
    # Create figure
    plt.figure(figsize=(8, 6))

    # Plot each vector
    for v, color, label in zip(vectors, colors, labels):
        plt.quiver(0, 0, v[0], v[1],
                   angles='xy', scale_units='xy', scale=1,
                   color=color, label=label, width=0.005)

    # Determine plot limits based on vectors
    max_val = max(np.max(np.abs(v)) for v in vectors) + 1
    plt.xlim(-1, max_val)
    plt.ylim(-1, max_val)

    # Add grid and axes
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Add title and legend
    plt.title('2D Vector Visualization', pad=20)
    plt.legend(loc='upper right')

    # Axis labels
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Save and close
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Plot saved as {output_file}")


if __name__ == "__main__":
    # Example vectors to visualize
    vectors = [
        np.array([2, 1]),  # v1
        np.array([1, 3]),  # v2
        np.array([-1, 2])  # v3 (added for demonstration)
    ]

    colors = ['r', 'b', 'g']
    labels = [
        'v1 = [2, 1]',
        'v2 = [1, 3]',
        'v3 = [-1, 2]'
    ]

    # Create output directory if it doesn't exist
    import os

    os.makedirs('output', exist_ok=True)

    # Generate and save the plot
    plot_vectors(vectors, colors, labels)