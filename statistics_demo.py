# https://www.kdnuggets.com/lesser-known-python-functions-that-are-super-useful
from statistics import mean, fmean
import time

# Let's compare fmean with regular mean
# Imagine we're analyzing daily temperature readings
temperatures = [
    21.5, 22.1, 23.4, 22.8, 21.8,
    23.2, 22.7, 23.1, 22.6, 21.9
] * 100000  # Create a large dataset

# Let's compare speed and precision
start_time = time.perf_counter()
regular_mean = mean(temperatures)
regular_time = time.perf_counter() - start_time

start_time = time.perf_counter()
fast_mean = fmean(temperatures)
fast_time = time.perf_counter() - start_time

print(f"Regular mean: {regular_mean:.5f} (took {regular_time:.4f} seconds)")
print(f"fmean: {fast_mean:.5f} (took {fast_time:.4f} seconds)")