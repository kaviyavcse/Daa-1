import random
import sys

# Increase recursion depth for testing worst-case arrays
sys.setrecursionlimit(2000)


def partition(arr, low, high):
    """
    Lomuto Partition Scheme:
    Uses the element at arr[high] as the pivot to partition the subarray.
    Elements <= pivot are moved to the left, larger elements to the right.
    """
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    # Place pivot in its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quicksort(arr, low, high):
    """
    Standard Quicksort using the last element as the fixed pivot.
    Worst-case time complexity: O(n^2) when input is sorted or reverse-sorted.
    """
    if low < high:
        pivot_idx = partition(arr, low, high)

        # Recursively sort elements before and after partition
        deterministic_quicksort(arr, low, pivot_idx - 1)
        deterministic_quicksort(arr, pivot_idx + 1, high)


def randomized_quicksort(arr, low, high):
    """
    Randomized Quicksort selects a random pivot and swaps it with the last element.
    Expected time complexity: O(n log n) even on worst-case input configurations.
    """
    if low < high:
        # Randomly select pivot index and swap with high
        rand_idx = random.randint(low, high)
        arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

        pivot_idx = partition(arr, low, high)

        # Recursively sort elements before and after partition
        randomized_quicksort(arr, low, pivot_idx - 1)
        randomized_quicksort(arr, pivot_idx + 1, high)


# --- Demonstration & Testing ---
if __name__ == "__main__":
    # Test 1: Random array
    sample_data = [10, 7, 8, 9, 1, 5, 3]

    arr1 = sample_data.copy()
    deterministic_quicksort(arr1, 0, len(arr1) - 1)
    print("1. Deterministic Quicksort Output :", arr1)

    arr2 = sample_data.copy()
    randomized_quicksort(arr2, 0, len(arr2) - 1)
    print("2. Randomized Quicksort Output    :", arr2)

    # Test 2: Already sorted array (Worst-case scenario for Deterministic)
    sorted_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    arr3 = sorted_data.copy()
    deterministic_quicksort(arr3, 0, len(arr3) - 1)
    print("\n3. Sorted Input (Deterministic)   :", arr3)

    arr4 = sorted_data.copy()
    randomized_quicksort(arr4, 0, len(arr4) - 1)
    print("4. Sorted Input (Randomized)      :", arr4)
