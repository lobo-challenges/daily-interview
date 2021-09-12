class Solution: 
  
  def getRange(self, arr, target):
    # arr is already sorted with possible duplicates, return -1 if no target found
    firstIdx = -1
    lastIdx = -1

    # solution O(n)
    for idx in range(len(arr)):
      currVal = arr[idx]
      if currVal == target:
        isFirstOccurrence = firstIdx == -1 and lastIdx == -1
        if isFirstOccurrence:
          firstIdx = idx
          lastIdx = idx
        else :
          lastIdx = idx


    if lastIdx == -1 and lastIdx == -1:
      return -1
    else:    
      return [firstIdx, lastIdx]
  
  def getRangeBinarysearchWithLinear(self, arr, target):
    firstIdx = -1
    lastIdx = -1

    # solution O(lg(n)+k) where k is the number of occurrences (worst case is O(n) if k = n)
    start = 0
    end = len(arr)-1
    
    iter = 0
    while start <= end:
      middle = (start + end)//2
      # print('iteration: {}, start: {}, middle:{}, end: {}'.format(iter, start, middle, end))
      # print('target: {}, currEleement: {}'.format(target, arr[middle]))
      if target < arr[middle]:
        end = middle - 1
      elif arr[middle] < target:
        start = middle + 1
      else:
        start = end + 1 # to break the while in the last interation
        #found an element, assign firstIdx and secondIdx accordingly and search to the left and to the right
        # print('new target found at {}, update indexes'.format(middle))
        firstIdx = middle
        lastIdx = middle

        while firstIdx > -1 and arr[firstIdx] == target:
          firstIdx -=1
        firstIdx +=1 #correct the index in last iteration
        
        while lastIdx < len(arr) and arr[lastIdx] == target:
          lastIdx +=1
        lastIdx -=1 #correct the index in last iteration

        # print('first: {}, last: {}'.format(firstIdx, lastIdx))
      
      iter +=1



    if lastIdx == -1 and lastIdx == -1:
      return -1
    else:    
      return [firstIdx, lastIdx]

  def getRangeBinarysearchTwice(self, arr, target):
    
    def binarySearchCheckRepetition(myArray, myTarget, directionleft=True): #O(2log(n+k/2)) + ????? a constant for the repetitions?
      start = 0
      end = len(myArray)-1
      while start <= end:
        middle = (start+end)//2
        
        if myTarget < myArray[middle]:
          end = middle - 1
        elif myArray[middle] < myTarget:
          start = middle + 1
        else:
          # found target in 'middle', keep searching in the given direction
          if directionleft:
            
            predecessor = middle - 1
            if predecessor > -1 and myArray[predecessor] == target:
              end = middle
            else:
              return middle

          else: 
            
            successor = middle + 1
            if successor < len(myArray) and myArray[successor] == target:
              start = middle
            else:
              return middle
      return -1

    # one to find the first occurrence, another to find the last
    firstIdx = binarySearchCheckRepetition(arr, target, True)
    lastIdx = binarySearchCheckRepetition(arr, target, False)

    if lastIdx == -1 and lastIdx == -1:
      return -1
    else:    
      return [firstIdx, lastIdx]
  
print('\n######## linear search')# linear search
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1, 2, 3, 4, 5]
x = 3
print(Solution().getRange(arr, x))
# [2, 2]

arr = [1, 2]
x = -1
print(Solution().getRange(arr, x))
# -1

arr = [1]
x = 1
print(Solution().getRange(arr, x))
# [0 , 0]



print('\n######## binary search (with a linear search)') # binary search (with a linear search)
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRangeBinarysearchWithLinear(arr, x))
# [1, 4]

arr = [1, 2, 3, 4, 5]
x = 3
print(Solution().getRangeBinarysearchWithLinear(arr, x))
# [2, 2]

arr = [2, 2]
x = 2
print(Solution().getRangeBinarysearchWithLinear(arr, x))
# [0, 1]

arr = [1, 2]
x = -1
print(Solution().getRangeBinarysearchWithLinear(arr, x))
# -1

arr = [1]
x = 1
print(Solution().getRangeBinarysearchWithLinear(arr, x))
# [0 , 0]


print('\n######## binary search twice')# binary search twice
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRangeBinarysearchTwice(arr, x))
# [1, 4]

arr = [1, 2, 3, 4, 5]
x = 3
print(Solution().getRangeBinarysearchTwice(arr, x))
# [2, 2]

arr = [1, 2]
x = -1
print(Solution().getRangeBinarysearchTwice(arr, x))
# -1

arr = [1]
x = 1
print(Solution().getRangeBinarysearchTwice(arr, x))
# [0 , 0]