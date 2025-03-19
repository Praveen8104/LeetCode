class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        i=0
        size=len(nums)
        while i<size-2:

            if nums[i]==0:
                c=c+1

                for j in range(i,i+3):
                    if nums[j]==0:
                        nums[j]=1
                    else:
                        nums[j]=0
            i=i+1
        if 0 in nums[size-2:]:
            return -1
        
        return c