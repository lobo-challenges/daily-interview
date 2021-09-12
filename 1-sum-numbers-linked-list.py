"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
Here is the function signature as a starting point (in Python):
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

def addTwoDigit(val1, val2, carry):
  sum = val1 + val2 + carry
  if sum > 9:
    return sum - 10, 1
  else:
    return sum, 0

def printList(list):

  while list:
    print(list.val),
    list = list.next

class Solution:
  


  def addTwoNumbers(self, l1, l2):

    digitResult = 0
    carry = 0
    resultList = ListNode(0)
    resultListHead = resultList
    while l1 or l2:
      print("curr l1: ")
      printList(l1)
      print("curr l2: ")
      printList(l2)
      digitResult, carry = addTwoDigit(l1.val, l2.val, carry)
      print("Result: {}, carry: {}".format(digitResult, carry))
      resultList.val = digitResult
      resultList.next = ListNode(0)
      print("resultList.val: {}, resultList.next: {}".format(resultList.val, resultList.next))
      resultList = resultList.next
      print("resultList.val: {}, resultList.next: {}".format(resultList.val, resultList.next))
      l1 = l1.next
      l2 = l2.next

    return resultListHead
  
  def addTwoNumbersClean(self, l1, l2):

    digitResult = 0
    carry = 0
    currNode = ListNode(0)
    resultListHead = currNode
    while l1 or l2:
      if l1 == None:
        l1 = ListNode(0)
      
      if l2 == None:
        l2 = ListNode(0)

      digitResult, carry = addTwoDigit(l1.val, l2.val, carry)
      currNode.val = digitResult
      currNode.next = ListNode(carry)
      
      currNode = currNode.next
      l1 = l1.next
      l2 = l2.next

    return resultListHead


if __name__ == "__main__":

  l1 = ListNode(5)
  l1.next = ListNode(4)
  l1.next.next = ListNode(3)
  
  l2 = ListNode(5)
  l2.next = ListNode(6)
  l2.next.next = ListNode(6)
  l2.next.next.next = ListNode(1)
  # l1 = ListNode(2)
  # l1.next = ListNode(4)
  # l1.next.next = ListNode(3)
  
  # l2 = ListNode(5)
  # l2.next = ListNode(6)
  # l2.next.next = ListNode(4)
  
  # result = Solution().addTwoNumbers(l1, l2)
  result = Solution().addTwoNumbersClean(l1, l2)
  printList(result)
  # 7 0 8