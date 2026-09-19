class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            maxf = max(maxf, window[s[r]] )
            if (r - l + 1) - maxf > k:
                window[s[l]] -= 1
                l += 1
            res = max(res , r - l + 1)
        return res