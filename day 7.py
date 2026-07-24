class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split() automatically ignores trailing and leading spaces
        words = s.split()
        return len(words[-1])