import numpy as np

def generate_random_noise_with_properties(min_val=0, max_val=1, mean=0, std_dev=1, amplitude=1, frequency=1, slope=0, num_samples=100):
    # Generate random white noise
    noise = np.random.normal(0, 1, num_samples)  # Generating noise with mean 0 and std_dev 1
    
    # Generate time series properties (sinusoidal signal)
    time = np.arange(num_samples)
    signal = amplitude * np.sin(2 * np.pi * frequency * time)
    
    # Calculate the actual slope of the signal
    actual_slope = np.polyfit(time, signal, 1)[0]
    
    # Adjust the amplitude of the sinusoidal signal to match the target slope
    adjusted_amplitude = amplitude * (slope / actual_slope)
    signal *= adjusted_amplitude
    
    # Add the sinusoidal signal to the white noise
    data = noise + signal
    
    # Scale the data to fit within the specified range
    data_range = max_val - min_val
    data_min = np.min(data)
    data_max = np.max(data)
    data_scaled = (data - data_min) / (data_max - data_min) * data_range + min_val
    
    # Adjust mean and standard deviation
    data_scaled_mean = np.mean(data_scaled)
    data_scaled_std_dev = np.std(data_scaled)
    data_scaled = (data_scaled - data_scaled_mean) * (std_dev / data_scaled_std_dev) + mean
    
    return data_scaled
