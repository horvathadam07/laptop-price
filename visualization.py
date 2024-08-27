#import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_categories(df, features):

    # Calculate number of rows and columns for subplots
    num_cols = min(2, len(features))
    num_rows = (len(features) - 1) // 2 + 1

# Create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(9, 3*num_rows))

# Flatten axes if only one row
    if num_rows == 1:
        axes = axes.reshape(1, -1)

# Plot categorical features
    for i, column in enumerate(features):
        row_idx = i // num_cols
        col_idx = i % num_cols
        sns.countplot(x=df[column], ax=axes[row_idx, col_idx], saturation=0.5, width=0.75)
        axes[row_idx, col_idx].set_xlabel(column, fontsize=8)
        axes[row_idx, col_idx].set_ylabel('Count', fontsize=8)
        axes[row_idx, col_idx].tick_params(axis='both', which='both', labelsize=6)
        axes[row_idx, col_idx].tick_params(axis='x', rotation=45)  # Rotate x-axis labels

# Remove any empty subplots
    for i in range(len(features), num_rows * num_cols):
        row_idx = i // num_cols
        col_idx = i % num_cols
        fig.delaxes(axes[row_idx, col_idx])

# Adjust layout
    plt.tight_layout()
    plt.show()


def plot_histograms(df, features):

    # Calculate number of rows and columns for subplots
    num_cols = min(2, len(features))
    num_rows = (len(features) - 1) // 2 + 1

# Create subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(9, 3*num_rows))

# Flatten axes if only one row
    if num_rows == 1:
        axes = axes.reshape(1, -1)

# Plot numerical features
    for i, column in enumerate(features):
        row_idx = i // num_cols
        col_idx = i % num_cols

        sns.histplot(x=df[column], ax=axes[row_idx, col_idx])
        axes[row_idx, col_idx].set_xlabel(column) 

# Remove any empty subplots
    for i in range(len(features), num_rows * num_cols):
        row_idx = i // num_cols
        col_idx = i % num_cols
        fig.delaxes(axes[row_idx, col_idx])

# Adjust layout
    plt.tight_layout()
    plt.show()
