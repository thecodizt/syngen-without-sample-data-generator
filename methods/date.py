import pandas as pd
import numpy as np

from .utils import generate_series_with_distribution

def generate_random_date(start, end, num_unique, distribution, num_records):
    unique_dates = np.array(pd.date_range(start=start, end=end, periods=num_unique))

    return generate_series_with_distribution(unique_values=unique_dates, distribution_name=distribution, num_records=num_records)