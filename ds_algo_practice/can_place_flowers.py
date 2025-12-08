"""
Docstring for ds_algo_practice.can_place_flowers
Reference: https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def canPlaceFlowers(self, dflowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        for index, bed in enumerate(dflowerbed):
            if bed != 1:
                if ((index == 0) or (dflowerbed[index - 1] == 0)) and ((index == len(dflowerbed) - 1) or dflowerbed[index + 1] == 0):
                    dflowerbed[index] = 1
                    n -= 1 # plotted one flower

            if n == 0:
                break

        return n == 0
