# Problem: https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        
        y = 1
        pal = True

        if (len(x)%2==0):
          time = len(x) / 2
        else:
          time = (len(x) / 2) - 0.5

        time = int(time)

        for i in range(time):
          if (x[y-1]==x[-y]):
            pal = True
          else:
            pal = False
          y += 1
        
        return pal

x = -10
v = Solution().isPalindrome(x)

print(v)
