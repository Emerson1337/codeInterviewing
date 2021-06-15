class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
    def searchBinary(lista, item):
      start = 0
      last = len(lista)-1
      found = False
      pos = -1
      while start <= last and not found:
        mid = (start+last)//2
        if item == lista[mid]:
          pos = mid
          found = True
        if item > lista[mid]:
          start = mid-1
        else:
          last = mid-1
      
      return pos

    foundNumberPos = searchBinary(arr, target)
    aux = foundNumberPos
    aux2 = foundNumberPos
    while arr[aux] == target:
      aux+=1

    while arr[aux2] == target:
      aux2-=1
    lastOcurrence = aux-1
    firstOcurrence = aux2+1
    return [firstOcurrence, lastOcurrence]

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]