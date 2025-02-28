class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            pro = 1
            for j in range(len(nums)):
                if nums[i] != nums[j]:
                    pro*=nums[j]
            l.append(pro)
        return l
            