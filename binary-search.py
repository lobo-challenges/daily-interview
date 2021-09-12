def binarySearch(arr, target):
  start = 0
  end = len(arr) -1
  
  iter = 0
  while start <= end:
    middle = (start + end)//2
    print('Iteration: {}, start: {}, end: {}, middle: {}'.format(iter, start, end, middle))
    if target < arr[middle]:
      end = middle -1
    elif arr[middle] < target:
      start = middle +1
    else:
      return middle

    iter +=1

  return -1




arr = [1,2,3,4,5,6]
# arr = [1,2,3,4,5]
# print(binarySearch(arr, 1))
# print(binarySearch(arr, 2))
# print(binarySearch(arr, 3))
# print(binarySearch(arr, 4))
# print(binarySearch(arr, 5))
# print(binarySearch(arr, 0))
# print(binarySearch(arr, 6))