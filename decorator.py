from time import time,sleep

def measure(f):
    def timing_decorator(*args, **kwargs):
        start = time()
        result = f(*args,**kwargs)
        end = time()
        print(f"Time taken {end - start} milliseconds")
        return result
    return timing_decorator

@measure
def slow_function(p) -> str:
    sleep(0.7)
    print("I am first")
    return f"Finished {p}"

@measure
def add_two_numbers(x1:int,x2:int) -> None :
    sum = x1 + x2
    print(f"sum of {x1} and {x2} is {sum}")

if __name__ == "__main__":
    print(slow_function("test"))
    print("-" * 50)
    print(add_two_numbers(4,5))



