import pytest

from ds_algo_practice.can_place_flowers import Solution


@pytest.mark.parametrize(
    ("flowerbed", "n", "expected_output"),
    [
        ([1,0,0,0,1], 1, True),
        ([1,0,0,0,1], 2, False),
        ([0,0,0,0,0,1,0,0], 0, True)
    ]
)
def testCanPlaceFlowers(flowerbed, n, expected_output):
    sol = Solution()
    assert expected_output == sol.canPlaceFlowers(flowerbed, n)
