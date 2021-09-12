def isPalindrome(candidate):
  start = 0
  end = len(candidate) - 1
  while start < end:
    if not candidate[start] == candidate[end]:
      return False
    start +=1
    end -=1
  return True #O(n/2) ~= O(n)

class Solution: 
    def longestPalindrome(self, s): # 
      
      longestPalindromeString = ''
      maxPalindromeLenfound = 1
      
      stringSize = len(s)
      # declare boolean table (all false)
      isPalindromeTable = [[False for x in range(stringSize)] for y in range(stringSize)]
      # set true for strings of size 1
      for index in range(stringSize):
        isPalindromeTable[index][index] = True
      # set true for strings of size 2 where both letters are the same
      for index in range(stringSize-1):
        if s[index] == s[index+1]:
          isPalindromeTable[index][index+1] = True
          maxPalindromeLenfound = 2
      
      for currSubstringLen in range(3, stringSize+1):
      # cases 1 and 2 already considered, start in 3
        print('Curr len: ', currSubstringLen)
        for start in range(0, stringSize-currSubstringLen+1):
          end = start + currSubstringLen -1
          print("start: {}, exEnd: {}... stringSize: {}, curr: {},...... STRING: {}".format(start,end, stringSize, currSubstringLen,s[start:end+1]))
        
          # currSubstring is palindrome if inner substring excluding extremes is a palindrome AND the extremes are the same
          if isPalindromeTable[start+1][end -1] and (s[start] == s[end]):
            isPalindromeTable[start][end] = True
            # store current best answer
            maxPalindromeLenfound = currSubstringLen
            longestPalindromeString = s[start:end+1]

      
      return longestPalindromeString
    
    def longestPalindromeBruteForce1(self, s): # O(n^2*n/2)  ~= O(n^3)
      
      longestPalindromeString = ''
      maxPalindromeLenfound = 0
      for start in range(0, len(s)):
        for end in range(start+1, len(s) + 1):
          candidate = s[start:end]
          if isPalindrome(candidate) and maxPalindromeLenfound < len(candidate):
            maxPalindromeLenfound = len(candidate)
            longestPalindromeString = candidate

      return longestPalindromeString
        
# Test program
s = "tracecars"
s = "abaxx"
# print(str(Solution().longestPalindrome(s)))
print(str(Solution().longestPalindromeBruteForce(s)))
# racecar