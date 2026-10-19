from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = Counter(nums)
        for i in n.values():
            if i >= 2:
                return True
        return False
                