def bubble_sort(arr):
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.

    Args:
    arr: List of integers to be sorted.

    Returns:
    It actually does not return, but since the array is passed by 
    reference, the array changes are reflected in the calling place
    """

    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [5, 8, 1, 0, 3, 9]
bubble_sort(arr)
print(arr)
