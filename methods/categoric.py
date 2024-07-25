import numpy as np
import random
import string

from .utils import generate_series_with_distribution

def generate_random_strings(n, length=5):
    unique_strings = set()  # Use a set to store unique strings
    
    while len(unique_strings) < n:
        # Generate a random string of specified length
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        unique_strings.add(random_string)
    
    return list(unique_strings)

def generate_random_strings_with_distribution(num_unique = 1, distribution = "Uniform", num_records=100):
    unique_strings = generate_random_strings(num_unique)
    
    return generate_series_with_distribution(
        unique_values=unique_strings, 
        distribution_name=distribution, 
        num_records=num_records
    )