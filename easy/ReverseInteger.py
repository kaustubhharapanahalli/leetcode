class Solution:
    def reverse(self, x: int) -> int:
        num_str = str(abs(x))
        ret_num = int(num_str[::-1])
        if x < 0:
            ret_num = ret_num * -1
        return (
            ret_num
            if (ret_num >= -(2 ** 31) and ret_num <= (2 ** 31 - 1))
            else 0
        )
