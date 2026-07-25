class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # Traverse both strings from right to left
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            res.append(str(total % 2))  # Result bit (0 or 1)
            carry = total // 2          # Carry bit (0 or 1)
            
        # Since we built the string backwards, reverse it
        return "".join(reversed(res))