def binary_search(array, target, low, high):
  if low > high:
    return -1

  mid = (low + high) // 2

  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, low, mid - 1)
  else:
    return binary_search(array, target, mid + 1, high)
array = [1,2,3,4,5,6,7,8]
target = 5
low = 0
high = len(array)-1
print(binary_search(array,target,low,high))
