class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_c = nums[0]
        max_c = nums[0]
        ans = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_c , min_c = min_c,max_c
            max_c = max(num , max_c * num)
            min_c = min(num,min_c * num)
            ans = max(ans,max_c)
        return ans