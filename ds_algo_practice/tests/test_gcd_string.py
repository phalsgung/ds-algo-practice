import pytest

from ds_algo_practice.gcd_string import Solution

@pytest.mark.parametrize(
    ("str1", "str2", "expected_output"),
    [
        ("ABABAB", "ABAB", "AB"),
        ("ABCABC", "ABC", "ABC"),
        ("LEET", "CODE", ""),
        ("AAAAAB", "AAA", ""),
        ("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXX")
    ]
)
def testGcdOfStrings(str1, str2, expected_output):
    sol = Solution()
    assert expected_output == sol.gcdOfStrings(str1, str2)
