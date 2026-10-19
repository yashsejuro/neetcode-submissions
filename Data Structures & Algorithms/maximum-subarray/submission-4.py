class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        max_c = nums[0]
        for i in nums[1::]:
            cur = max(i,i+cur)
            max_c = max(cur,max_c)
        return max_c