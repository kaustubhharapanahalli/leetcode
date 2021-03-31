class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_pal = int(str(x)[::-1])
        if not x_pal <= (2 ** 31 - 1):
            return False

        return True if x == x_pal else False