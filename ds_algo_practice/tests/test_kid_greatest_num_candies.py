import pytest

from ds_algo_practice.kid_greatest_num_candies import Solution

@pytest.mark.parametrize(
    ("candies", "extraCandies", "expected_output"),
    [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4,2,1,1,2], 1, [True, False, False, False, False]),
        ([12,1,12], 10, [True, False, True])
    ]
)
def testKidsWithCandies(candies, extraCandies, expected_output):
    sol = Solution()
    assert expected_output == sol.kidsWithCandies(candies, extraCandies)
