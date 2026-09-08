"""Given a binary array nums, return the maximum number of consecutive 1's in the array."""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = 0
        # counter = 0
        Hstreak = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                n += 1
                if n > Hstreak:
                    Hstreak = n
            else: 
                Hstreak = n
                n = 0
    
        return Hstreak

        