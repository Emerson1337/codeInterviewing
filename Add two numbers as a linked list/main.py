# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
      # Fill this in.
      aux = l1
      aux2 = l2
      vector = []
      vector2 = []
      while aux:
        vector.insert(0, aux.val)
        aux = aux.next
        
      string = str(vector).strip('[]')
      string = string.replace(', ', '')
      number = int(string)
        
      while aux2:
        vector2.insert(0, aux2.val)
        aux2 = aux2.next
        
      string2 = str(vector2).strip('[]')
      string2 = string2.replace(', ', '')
      number2 = int(string2)

      anwser = number + number2
      stringAnwser = str(anwser)
      stringAnwser = stringAnwser[::-1]
      resposta = ListNode(stringAnwser[0])
      resposta.next = ListNode(stringAnwser[1])
      resposta.next.next = ListNode(stringAnwser[2])

      return resposta

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val),
  result = result.next
# 7 0 8