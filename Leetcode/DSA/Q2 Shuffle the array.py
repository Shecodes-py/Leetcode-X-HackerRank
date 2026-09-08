"""Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn]."""

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        final = []
        
        for i in range(n): 
            fina = nums[i]
            fina2 = nums[n+i]
            
            final.append(fina)
            final.append(fina2)

        return final
