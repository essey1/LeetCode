class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        mark = len(digits)

        # Go from right to left
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] -= 1
                mark = i  # everything from here becomes 9

        # Fix cascading effects backward
        for i in range(mark, len(digits)):
            digits[i] = 9

        # Handle any digits that became negative (rare edge case)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] -= 1
                for j in range(i, len(digits)):
                    digits[j] = 9

        return int(''.join(map(str, digits)))
