# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        first = 1
        last = n
        
        while (first < last):
            mid = last + (first -last) // 2
            if isBadVersion(mid) == False: #good
                first = mid+1
            else:
                last = mid

        return first
            
            
        """
        :type n: int
        :rtype: int
        """
        