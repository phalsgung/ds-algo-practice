class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        # if string are not equal but lengths are equal, there is no possibility of substring
        if len(str1) == len(str2):
            return ""

        gcd_num = math.gcd(len(str2), len(str1))
        # possible_gcd_str = str1[:gcd_num]

        # final check if all occurences of both string match
        if str1.replace(str1[:gcd_num], "") == "" and str2.replace(str1[:gcd_num], "") == "":
            return str1[:gcd_num]
        else:
            return ""


if __name__ == "__main__":
    str1 = "ABABAB"
    str2 = "ABAB"
    output = gcdOfStrings(str1, str2)
    print(output)
