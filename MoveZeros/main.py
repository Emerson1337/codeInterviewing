class Solution:
  def moveZeros(self, nums):
    # Fill this in.
    count = 0
    size = len(nums)
    for num in range(0, size):
      if (nums[num] != 0):
        nums[count] = nums[num]
        count+=1
    for i in range(count, size):
      nums[i] = 0

    return nums;

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]