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
  right rotation of 'array' by 'shift' indexes using reverse algorithm
  
  i) reverse whole array, i in [0, sizeOf(array)]
  ii) reverse array chunk for i in [0, shift)
  iii) reverse array chunk for i in [shift,  sizeOf(array) ]
  END return array
  """
  def rightRotation(self, shift, array):
    arraySize = len(array)
    shift = shift % arraySize

    print("Array, start: {}".format(array))
    reverseArrayChunk(array, 0, arraySize)
    print("Array, after reversing whole array( i) ): {}".format(array))
    reverseArrayChunk(array, 0, shift)
    print("Array, after reversing LEFT chunk ( ii) ): {}".format(array))
    reverseArrayChunk(array, shift, arraySize)
    print("Array, after reversing RIGHT chunk ( iii) ): {}".format(array))
    return array



input = [1,2,3,4,5]
shift = 3

print(Solution().rightRotation(shift, input))
