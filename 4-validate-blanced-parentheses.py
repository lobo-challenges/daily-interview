class Solution:

  def __init__(self):
    self.corresponding = {
                          ')': '(',
                          ']': '[',
                          '}': '{'}
    
    self.leftSymbol = ['(', '[', '{']
    self.rightSymbol = [')', ']', '}']
    
  
  def isLeft(self, myChar):
    # return myChar in self.leftSymbol # using list: O(n=3), verify if an element is in a list
    return myChar in self.corresponding.values() # using hash: O(n=3), has to check for each value if the input is in there
    
  def isRight(self, myChar):
    # return myChar in self.rightSymbol # using list: O(n=3), verify if an element is in a list
    return myChar in self.corresponding # using hash: O(1), verify if an input is a key in a hash
  
  def isValid(self, s):
    # empty string is valid
    #- Open brackets are closed by the same type of brackets.
    #- Open brackets are closed in the correct order.
    if s == '':
      return True

    openSymbols = []

    for myChar in s:
      # print("myChar: {}".format(myChar))
      if self.isLeft(myChar): # O(3)
        openSymbols.append(myChar) # push
      elif self.isRight(myChar): # O(3)
        
        if len(openSymbols) < 1:
          return False
        
        lastSymbol = openSymbols[-1]
        correspondingLeftSymbol = self.corresponding[myChar] #O(1)

        if correspondingLeftSymbol == lastSymbol:
          openSymbols.pop()
        else:
          return False

      else:
        raise Exception("Invalid entry")

    if len(openSymbols) == 0:
      return True 
    else: 
      return False
      
# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

s = "(((((((((("
# should return False
print(Solution().isValid(s))

s = ")))))"
# should return False
print(Solution().isValid(s))

s = "([)"
# should return False
print(Solution().isValid(s))
