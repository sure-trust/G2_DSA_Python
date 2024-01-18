def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Element not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Element found at index mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Search the left half
    else:
        return binary_search(arr, target, mid + 1, high)  # Search the right half

# Example usage:
my_list = [6, 7, 8, 9, 10, 11, 12, 13, 14]
target_element = 10

result = binary_search(my_list, target_element, 0, len(my_list) - 1)

if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")

