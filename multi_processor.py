"""
This script takes advantage of multi-core systems
For any cpu-bound tasks, multi-processing (running in multiple cores) will benefit
For io-bound tasks,you should use asyncio

https://www.youtube.com/watch?v=ipzZS1tDIls&t=500s
"""
import time
import os
from typing import Any,Callable
from multiprocessing import Pool

def expensive_function(n:int) -> int:
    for _ in range(100_000):
        n *= 2
    return n

def run_in_single_core(numbers: list[int]) -> list[int]:
    return [expensive_function(n) for n in numbers]

#no memory leaks or zombie processes - all taken care
def run_in_multi_core(numbers: list[int]) -> list[int]:
    with Pool() as pool:
        return pool.map(expensive_function, numbers)

#timing function
#func - a function that takes any no .of arguments and returns a list of integers
#args - positional arguments to be passed to a function
def get_time(func: Callable[...,list[int]], *args:Any) -> float:
    start = time.perf_counter()
    func(*args) #call the function
    end = time.perf_counter()
    total_time = end - start

    print(f"{func.__name__}: {total_time:.3f} seconds")
    return total_time

def main():
    print("Cpu Count:", os.cpu_count())
    numbers: list[int] = list(range(1,21))

    #verify that we get same results
    assert run_in_single_core(numbers) == run_in_multi_core(numbers)

    #single process benchmark
    single_time:float =  get_time(run_in_single_core,numbers)

    # multi process benchmark
    multi_time:float = get_time(run_in_multi_core, numbers)

    print(f"Speedup: {single_time / multi_time:.2f}x")

if __name__ == "__main__":
    main()



