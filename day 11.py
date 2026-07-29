class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: If 1 row or string length is less than numRows, no zigzag needed
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through each character and bounce between rows
        for char in s:
            rows[current_row] += char
            
            # Change direction at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            current_row += 1 if going_down else -1
            
        # Combine all rows into a single string
        return ''.join(rows)