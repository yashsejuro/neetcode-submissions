class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_maps ={}
        for i,num in enumerate(nums):
            complement = target - num
            if (complement in seen_maps):
                return[seen_maps[complement],i]
            seen_maps[num] = i
        