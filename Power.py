# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        power = abs(exponent)
        result = base
        for _ in range(power-1):
            result *= base
        if exponent < 0:
            result = 1/result
        return result


if __name__ == "__main__":
    base = 4.4
    exponent = -3
    solution = Solution()
    result = solution.Power(base, exponent)
    print(result)