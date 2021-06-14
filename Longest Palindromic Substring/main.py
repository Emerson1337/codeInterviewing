class Solution: 
    def longestPalindrome(self, s):
      # Fill this in.
      allPalin = []
      vector = []
      for i in range(0, len(s)+1):
        for o in range(i, len(s)+1):
          teste = s[i:o]
          if s[i:o] == teste[::-1]:
            vector.extend(s[i:o])
            if len(vector) == len(s):
              break
            vector = []
          else: 
            allPalin.append(vector)
      awnser = max(allPalin)
      return ''.join(awnser)
      
        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar