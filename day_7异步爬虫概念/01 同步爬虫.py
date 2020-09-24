class Solution:
    def isPalindrome(self, x):

        x = str(x)
        y = x[::-1]
        if x == y:
            return 'true'
        else:
            return 'false'
obj = Solution()

print(obj.isPalindrome(121))