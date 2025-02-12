"""
    *args allows any no. of positional arguments to
    be passed to the function. The asterisk packs
    the arguments into a tuple
"""
def my_sum(*args):
    print("-" * 30)
    print(f"args type={type(args)}")
    total = sum(args)
    return total

"""
    **kwargs allows any no. of keyword arguments to
    be passed to the function. The double asterisk packs
    the arguments into a dictionary
"""
def print_info(**kwargs):
    print("-" * 30)
    print(f"kwargs type={type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


"""
    You could also combine *args and **kwargs
    but args should come before kwargs. kwargs should be placed last
"""
def mixed_function(arg1, arg2, *args, **kwargs):
    print("-" * 30)
    print(f"arg1: {arg1}, arg2: {arg2}")
    print("Additional positional arguments:", args)
    print("Keyword arguments:", kwargs)

def sum_of_four(num1:int, num2:int, num3:int, num4:int) -> int:
    print("-" * 30)
    print(f"num1={num1}, num2={num2}, num3={num3}, num4={num4}")
    return num1 + num2 + num3 + num4

def display(name:str, age:int, city:str) -> None:
    print("-" * 30)
    print(f"name={name}, age={age}, city={city}")

if __name__ == "__main__":
    print("sum=",my_sum(1, 2, 3))  # Output: 6
    print("sum=",my_sum(10, 20, 30, 40))  # Output: 100
    print_info(name="Alice", age=30, city="New York")
    dict = {
        "name" : "George",
        "age" : 30,
        "city" : "chennai"
    }
    # ** unpacks dict to provide keyword arguments.
    # arg names should not be misspelt and no extra arguments and no less arguments
    display(**dict)

    # * unpacks tuple to provide positional arguments
    tup = (4,5,6,7)
    result = sum_of_four(*tup)
    print("sum=", result)

    mixed_function(1, 2, 3, 4,5, name="Bob", age=25, email="bob@gmail.com")

