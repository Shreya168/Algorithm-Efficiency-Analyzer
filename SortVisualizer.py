import random
import time
import matplotlib.pyplot as plt


# Sorting Algorithms

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


# Radix Sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr



# Algorithm Complexity Analysis
def complexity_analysis():
    complexities = {
        'Bubble Sort': 'O(n^2)',
        'Selection Sort': 'O(n^2)',
        'Insertion Sort': 'O(n^2)',
        'Merge Sort': 'O(n log n)',
        'Quick Sort': 'O(n^2) average, O(n log n) best',
        'Heap Sort': 'O(n log n)',
        'Radix Sort': 'O(nk)'
    }

    print("Algorithm Complexities:")
    for algorithm, complexity in complexities.items():
        print(f"{algorithm}: {complexity}")


# User Input and Customization
def custom_sort():
    data_size = int(input("Enter the size of the dataset: "))
    min_value = int(input("Enter the minimum value for elements: "))
    max_value = int(input("Enter the maximum value for elements: "))

    data = generate_random_array(data_size, min_value, max_value)

    print("Select sorting algorithm:")
    for idx, algorithm in enumerate(algorithms, start=1):
        print(f"{idx}. {algorithm.__name__}")

    choice = int(input("Enter your choice: "))
    if 1 <= choice <= len(algorithms):
        chosen_algorithm = algorithms[choice - 1]
        sorted_data, time_taken = measure_time(chosen_algorithm, data)
        print(f"\nSorted data using {chosen_algorithm.__name__}:")
        print(sorted_data)
        print(f"\nTime taken: {time_taken} seconds")
    else:
        print("Invalid choice. Please select a valid algorithm.")


# Error Handling and Validation
def validate_input(value, prompt):
    while True:
        try:
            return int(value)
        except ValueError:
            print(f"Invalid {prompt}. Please enter a valid integer.")


def handle_user_input():
    data_sizes = validate_input(input("Enter data sizes (comma-separated): "), "data sizes").split(",")
    data_sizes = [int(size.strip()) for size in data_sizes]

    algorithms_to_run = validate_input(input("Enter algorithm indices to run (comma-separated): "),
                                       "algorithm indices").split(",")
    algorithms_to_run = [algorithms[int(idx.strip()) - 1] for idx in algorithms_to_run if
                         1 <= int(idx) <= len(algorithms)]

    plot_algorithm_performance(algorithms_to_run, data_sizes)


# Data Generation
def generate_random_array(size, min_value=0, max_value=1000):
    return [random.randint(min_value, max_value) for _ in range(size)]


# Performance Measurement
def measure_time(sort_function, data):
    start_time = time.time()
    sorted_data = sort_function(data)
    end_time = time.time()
    return sorted_data, end_time - start_time


# Visualization
def plot_algorithm_performance(algorithms, data_sizes):
    for algorithm in algorithms:
        times = []
        for size in data_sizes:
            data = generate_random_array(size)
            _, time_taken = measure_time(algorithm, data)
            times.append(time_taken)
        plt.plot(data_sizes, times, label=algorithm.__name__)

    plt.xlabel('Data Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.show()


# Compare Algorithms
algorithms = [bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort, radix_sort]
data_sizes = [10, 100, 1000, 5000]  # Adjust as needed

# Run algorithm performance comparison
plot_algorithm_performance(algorithms, data_sizes)

# # Add an option to run the new features
while True:
    print("Select an option:")
    print("1. Compare algorithm performance")
    print("2. Algorithm complexities")
    print("3. Custom sort")
    print("4. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        plot_algorithm_performance(algorithms, data_sizes)
    elif option == 2:
        complexity_analysis()
    elif option == 3:
        custom_sort()
    elif option == 4:
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
