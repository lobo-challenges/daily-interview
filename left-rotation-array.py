def reverseArrayChunk(array, inclusiveStart, exclusiveEnd):
  start = inclusiveStart
  end = exclusiveEnd - 1
  while start < end:
    aux = array[start]
    array[start] = array[end]
    array[end] = aux
    start += 1
    end -= 1
  return array

class Solution:
  """
  Left rotation of 'array' by 'shift' indexes using reverse algorithm
  
  i) reverse array chunk for i in [0, shift)
  ii) reverse array chunk for i in [shift,  sizeOf(array) ]
  iii) reverse whole array, i in [0, sizeOf(array)]
  END return array
  """

  def leftRotation(self, shift, array):
    arraySize = len(array)
    shift = shift % arraySize
    print("Array, start: {}".format(array))
 
    reverseArrayChunk(array, 0, shift) #i
    print("Array, after reversing LEFT chunk: {}".format(array))
    reverseArrayChunk(array, shift, arraySize) #ii
    print("Array, after reversing RIGHT chunk: {}".format(array))
    reverseArrayChunk(array, 0, arraySize) #iii
    print("Array, after reversing whole array: {}".format(array))
    return array


input = [1,2,3,4,5]
shift = 7

print(Solution().leftRotation(shift, input))