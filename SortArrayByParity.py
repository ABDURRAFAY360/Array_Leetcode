# Question
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.
# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start=0
        end = len(nums)-1
        for i in range(0,len(nums)):
            if(nums[start] % 2 == 0):
                start=start+1
            else:
                temp = nums[end]
                nums[end] = nums[start]
                nums[start] = temp
                end=end-1
        return nums