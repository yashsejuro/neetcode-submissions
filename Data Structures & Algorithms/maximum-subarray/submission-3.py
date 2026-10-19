class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_sum = nums[0]
        for i in nums[1::]:
            current = max(i,current+i)
            max_sum = max(max_sum,current)
        return max_sum