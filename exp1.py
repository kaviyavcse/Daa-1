import time

# Interpolation Search Function
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:

        if low == high:
            if arr[low] == target:
                return low
            else:
                return -1

        # Avoid division by zero
        if arr[high] == arr[low]:
            break

        # Interpolation formula
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# Dataset sizes
sizes = [1000, 5000, 10000, 50000, 100000]

print("Size\tExecution Time (seconds)")

for size in sizes:
    # Create sorted dataset
    arr = list(range(size))

    # Target element
    target = size - 1

    # Measure execution time
    start = time.perf_counter()

    result = interpolation_search(arr, target)

    end = time.perf_counter()

    print(f"{size}\t{end - start:.8f}")

# Test Example
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70

index = interpolation_search(arr, target)

if index != -1:
    print("\nElement found at index:", index)
else:
    print("\nElement not found.")
