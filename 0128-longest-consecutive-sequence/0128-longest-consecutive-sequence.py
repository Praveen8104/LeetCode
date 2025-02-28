class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        print(nums)
        cnt = 1
        res = 1
        for i in range(1, len(nums)):

            if nums[i] == nums[i-1]:
                continue

            if nums[i] == nums[i - 1] + 1:
                cnt += 1
            
            else:
                cnt = 1

            res = max(res,cnt)
            
            print(i-1,cnt)

        return res
