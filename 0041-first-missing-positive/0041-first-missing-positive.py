class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums1=set(nums)
        i=1
        while i in nums1:
            i+=1
        return i