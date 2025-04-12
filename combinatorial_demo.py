#https://www.kdnuggets.com/lesser-known-python-functions-that-are-super-useful

#You can use the itertools.product function for generating all possible combinations
# of input iterables.
from itertools import product

# Available options for a custom laptop
processors = ['i5', 'i7', 'i9']
ram = ['8GB', '16GB', '32GB']
storage = ['256GB', '512GB', '1TB']

# Generate all possible combinations
configurations = list(product(processors, ram, storage))

print("Possible laptop configurations:")
for config in configurations: #each config is a tuple
    print(f"Processor: {config[0]}, RAM: {config[1]}, Storage: {config[2]}")

