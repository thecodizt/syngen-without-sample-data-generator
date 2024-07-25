import numpy as np
import pandas as pd

def generate_series_with_distribution(unique_values, distribution_name, num_records):
    if distribution_name == 'Uniform':
        index_values = np.random.uniform(low=0, high=len(unique_values) - 1, size=num_records)
        values = [unique_values[int(val)] for val in index_values] 
    elif distribution_name == 'Normal':
        # Calculate mean and standard deviation based on the number of unique strings
        mean = (len(unique_values) - 1) / 2  # mean is the middle index
        std_dev = len(unique_values) / 6  # adjust std deviation based on number of unique strings
        values = np.random.normal(mean, std_dev, size=num_records)
        values = np.clip(np.round(values), 0, len(unique_values) - 1)  # clip values to ensure they fall within range
        values = [unique_values[int(val)] for val in values]  # convert indices to corresponding strings
    elif distribution_name == 'Exponential':
        values = np.random.exponential(size=num_records)
        values = np.clip(np.round(values), 0, len(unique_values) - 1)  # clip values to ensure they fall within range
        values = [unique_values[int(val)] for val in values]  # convert indices to corresponding strings
    else:
        raise ValueError("Invalid distribution name. Choose from 'Uniform', 'Normal', or 'Exponential'.")

    return values