"""
    *args allows any no. of positional arguments to
    be passed to the function. The asterisk unpacks
    the argument into a tuple
"""
def my_sum(*args):
    print(f"args type={type(args)}")
    total = sum(args)
    return total

"""
    **kwargs allows any no. of keyword arguments to
    be passed to the function. The double asterisk unpacks
    the argument into a dictionary
"""
def print_info(**kwargs):
    print(f"kwargs type={type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


"""
    You could also combine *args and **kwargs
    but args should come before kwargs
"""
def mixed_function(arg1, arg2, *args, **kwargs):
    print(f"arg1: {arg1}, arg2: {arg2}")
    print("Additional positional arguments:", args)
    print("Keyword arguments:", kwargs)

print(my_sum(1, 2, 3))  # Output: 6
print(my_sum(10, 20, 30, 40))  # Output: 100
print_info(name="Alice", age=30, city="New York")
mixed_function(1, 2, 3, 4, name="Bob", age=25)

