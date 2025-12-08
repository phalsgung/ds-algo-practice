"""
Reference: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        max_candies = max(candies)
        for kid_candies in candies:
            if (kid_candies + extraCandies) >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
