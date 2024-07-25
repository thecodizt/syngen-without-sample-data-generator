import numpy as np
import math
import random

from .utils import generate_series_with_distribution

def generate_random_lat_lon_pairs(root_lat = 0, root_lon = 0, radius_lat = 1, radius_lon = 1, n=1):
    pairs = set()
    
    while len(pairs) < n:
         # Generate random angles within the specified radius
        lat = root_lat + random.uniform(-1 * radius_lat, radius_lat)
        lon = root_lon + random.uniform(-1 * radius_lon, radius_lon)
        
        # Ensure latitude and longitude values are within valid ranges
        lat = max(-90, min(90, lat))
        lon = max(-180, min(180, lon))
        
        # Add the pair to the set
        pairs.add((lat, lon))
        
    return [' '.join([str(v) for v in p]) for p in list(pairs)]

def generate_lat_lon_data(root_lat, root_lon, lat_radius, lon_radius, n_unique, distribution, num_records):
    unique_pairs = generate_random_lat_lon_pairs(root_lat=root_lat, root_lon=root_lon, radius_lat=lat_radius, radius_lon=lon_radius, n=n_unique)
    
    return generate_series_with_distribution(unique_pairs, distribution_name=distribution, num_records=num_records)