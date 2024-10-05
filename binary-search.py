def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    upper_bound = left if left < len(arr) else None

    if upper_bound is not None:
        return (iterations, arr[upper_bound]) if upper_bound < len(arr) else (iterations, None)

    return iterations, None


sorted_array = [0.1, 0.4, 0.7, 1.2, 2.5, 3.6, 5.0]
target_value = 0.3
result = binary_search(sorted_array, target_value)

print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
