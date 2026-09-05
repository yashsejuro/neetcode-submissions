from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = Counter(nums)
        for count in n.values():
            if count >= 2:
                return True
        return False