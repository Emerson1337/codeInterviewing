class Solution:
  def isValid(self, s):
    # Fill this in.
    awnser = []
    for i in s:
      if(i == '('):
        awnser.append(1)
      elif(i == ')'):
        awnser.pop()
      if(i == '{'):
        awnser.append(1)
      elif(i == '}'):
        awnser.pop()
      if(i == '['):
        awnser.append(1)
      elif(i == ']'):
        awnser.pop()

    if len(awnser) == 0:
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