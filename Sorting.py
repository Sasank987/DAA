import random
import time

def selection_sort(arr):
    swaps = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                swaps += 1

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return swaps

# Generate random array
arr = [random.randint(1, 1000) for _ in range(1000)]

# Measure execution time for selection sort
start_time = time.time()
num_swaps = selection_sort(arr)
end_time = time.time()

# Print results
print("Randomly generated array:", arr)
print("Sorted array:", arr)
print("Execution Time: %.17f seconds" % (end_time - start_time))
print("Number of Swaps: %d" % num_swaps)

# Compare with built-in sort
start_time = time.time()
arr.sort()  # Built-in sort for comparison
end_time = time.time()

print("\nBuilt-in sort Execution Time: %.8f seconds" % (end_time - start_time))

