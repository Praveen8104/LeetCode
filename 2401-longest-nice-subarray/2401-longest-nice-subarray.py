class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i = 0
        cum = 0
        res = 0
        for j, num in enumerate(nums):
            while cum & num != 0:
                cum -= nums[i]
                i += 1
            cum += num
            res = max(res, j - i + 1)
        return res