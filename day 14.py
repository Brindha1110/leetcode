class Solution(object):

    def reverse(self, x):
        MIN_INT = -(2**31)  # -2147483648
        MAX_INT = 2**31 - 1  # 2147483647

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            pop = x % 10
            x //= 10

            # Overflow Check
            if res > MAX_INT // 10 or (
                res == MAX_INT // 10 and pop > 7
            ):
                return 0

            res = res * 10 + pop

        return res * sign