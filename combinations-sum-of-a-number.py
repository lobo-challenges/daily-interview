class Solution:

  def __init__(self, steps, possibleSteps):
    self.staircaseSteps = steps
    self.possibleSteps = possibleSteps
    self.solution = []


  def computeAndPrintPossibleWays(self):
    noMoreCombinations = False
    while not noMoreCombinations:

      target = self.staircaseSteps - 1
      currSum = 0
      while currSum < target:
        
      # noMoreCombinations = True

    
    return None


N = 4
possibleSteps = [1,2]
print(Solution(N, possibleSteps).computeAndPrintPossibleWays())