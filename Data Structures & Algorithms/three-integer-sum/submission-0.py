class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i , a in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and a == nums[i-1]:
                continue
            while l < r:
                total = a + nums[l] + nums[r]
                if total==0:
                    res.append([a,nums[l] ,nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l -1]:
                        l += 1
                elif total > 0: 
                    r -= 1
                elif total < 0:
                    l += 1  
        return res           




