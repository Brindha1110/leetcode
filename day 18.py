class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes (e.g., -121 -> 121-)
        # Numbers ending in 0 (except 0 itself) cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original = x

        while x > 0:
            digit = x % 10
            reversed_num = (reversed_num * 10) + digit
            x //= 10

        return original == reversed_num