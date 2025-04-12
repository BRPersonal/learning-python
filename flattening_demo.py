#https://www.kdnuggets.com/lesser-known-python-functions-that-are-super-useful

from itertools import chain

"""
When working with nested data structures (lists within lists, or any nested iterables), 
flattening them efficiently can be challenging.

While list comprehensions are common, they create intermediate lists that consume memory
chain.from_iterable solves this by providing a memory-efficient way to flatten nested 
structures by creating an iterator.
"""

# Let's say we're processing data from multiple sources
sales_data = [
	[('Jan', 100), ('Feb', 150)],
	[('Mar', 200), ('Apr', 180)],
	[('May', 210), ('Jun', 190)]
]

# Flatten the data efficiently
flat_sales = list(chain.from_iterable(sales_data))
print("Flattened sales data:", flat_sales)

# List comprehension approach (creates intermediate list):
#It is like this
#   for (sublist in sales_data)
#       for(item in sublist)
#           flat_list.append(item)
flat_list = [item for sublist in sales_data for item in sublist]
print("list comprehension:  ", flat_list)

