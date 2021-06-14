class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    vector = []
    values = []
    count = 0
    pos = 0
    for character in s:
      if character in vector:
        values.append(count)
        vector = []
        count = 0
        if character != s[pos+1]:
          count += 1
      else:
        vector.append(character)
        count += 1
      pos+=1
    return max(values)
      


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10