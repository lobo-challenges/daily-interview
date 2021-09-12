def checkIfStringHasNoRepeatedChar(s):
  sameCharFound = True
  charFound = {}
  if len(s) == 1:
    return True
  for myChar in s:
    if myChar in charFound:
      return False
    charFound[myChar] = True

  return sameCharFound

class Solution:
  def lengthOfLongestSubstring(self, s):
    maxLenResultFound = 1 # all letters the same
    
    currString = ''
    currMaxLengthString = ''
    for start in range(0, len(s)):
      for end in range(start + 1, len(s) + 1):
        currString = s[start:end]
        if checkIfStringHasNoRepeatedChar(currString) and maxLenResultFound < len(currString):
          currMaxLengthString = currString
          maxLenResultFound = len(currString)

           

    print("Final Str: {}".format(currMaxLengthString))
    print("Final len: {}".format(maxLenResultFound))

    return maxLenResultFound

  # should implement a more efficient algorithm, the brute force + check is n^3 worse case 
  def lengthOfLongestSubstringBetter(self, s):
    maxLenResultFound = 1 # all letters the same
    stringSize = len(s)
    
    nonRepeatedCharSubstring = [[False for x in range(0,stringSize)] for y in range(0, stringSize)]
    
    for index in range(0, stringSize):
      nonRepeatedCharSubstring[index][index] = True

    def isCharIn(target, string):
      for myChar in string:
        if myChar == target:
          return True
      return False 
    
    for substringSize in range(1, stringSize + 1):
      print(substringSize)
      for index in range(0, stringSize - substringSize):
        start = index
        end = index + substringSize - 1
        isNonRepeated = nonRepeatedCharSubstring[start][end]
        currStr = s[start:end+1]
        nextChar = s[end+1]
        print("start: {}, end: {}".format(start, end))
        print("currString: ", currStr)
        print("nextChar: ", nextChar)
        if isNonRepeated and (not isCharIn(nextChar, currStr)):
          nonRepeatedCharSubstring[index][end+1] = True
          maxLenResultFound = substringSize + 1
          print("New non repepated found: {}, size: {}".format(currStr + nextChar, maxLenResultFound))
    return maxLenResultFound


print(Solution().lengthOfLongestSubstringBetter('abrkaabcdefghijjxxx'))
# print(Solution().lengthOfLongestSubstringBetter('abrkaabcdefghijjxxa'))
# 10
# print(Solution().lengthOfLongestSubstring('a'))
# print(Solution().lengthOfLongestSubstring('aa'))
# print(Solution().lengthOfLongestSubstring('ax'))
# print(Solution().lengthOfLongestSubstring('abrkagwc'))








# print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
# print(Solution().lengthOfLongestSubstring('a'))
# print(Solution().lengthOfLongestSubstring('aa'))
# print(Solution().lengthOfLongestSubstring('ax'))
# print(Solution().lengthOfLongestSubstring('abrkagwc'))