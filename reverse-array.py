class Solution:

  def reverseArray(self, array):
    """
    reverse array in place
    """
  
    start = 0
    end = len(array) -1
    while start < end:
      aux = array[start]
      array[start] = array[end]
      array[end] = aux 
      start += 1
      end -= 1
    
    return array


input = [1, 2, 3, 4, 5]

print(Solution().reverseArray(input))



