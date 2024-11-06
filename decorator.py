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
def slow_function(p):
    sleep(0.7)
    print("I am first")
    return f"Finished {p}"

if (__name__ == "__main__"):
    print(slow_function("test"))



