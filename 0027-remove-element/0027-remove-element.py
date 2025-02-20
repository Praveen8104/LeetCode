class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while i<len(nums):
                if nums[i]==val:
                   del nums[i]
                else:
                    i+=1
        return len(nums)

        # c=0
        
        # for i in range(len(nums)):
        #     if (nums[i]!=val):
                
        #         nums[c]=nums[i]
        #         c+=1
        # return c
