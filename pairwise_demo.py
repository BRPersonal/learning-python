# https://www.kdnuggets.com/lesser-known-python-functions-that-are-super-useful
from itertools import pairwise

# Let's analyze temperature changes
temperatures = [20, 23, 24, 25, 23, 22, 20]

# Calculate temperature changes between consecutive readings
changes = []
for prev, curr in pairwise(temperatures):
    change = curr - prev
    changes.append(change)

print("Temperature changes:", changes)

# find the largest temperature jump
max_jump = max(abs(curr - prev) for prev,curr in pairwise(temperatures))
print(f"Largest temperature change: {max_jump} degrees")