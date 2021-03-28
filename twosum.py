from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, element in enumerate(nums):
            diff = target - element
            if diff in d:
                return [d[diff], i]
            d[element] = i

        return []
