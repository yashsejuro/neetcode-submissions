class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]
        for i in nums[1:]:
            if i < 0:
                cur_max , cur_min = cur_min , cur_max
            cur_max = max(i,cur_max * i)
            cur_min = min(i , cur_min * i)
            ans = max(ans,cur_max)
        return ans
