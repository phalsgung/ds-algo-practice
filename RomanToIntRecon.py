class Solution:
    def romanToInt(s: str) -> int:
        RomanToNumberDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        Number = 0

        for index, letter in enumerate(s):
            if s[index] in [ "I", "X", "C" ]:
                # Condition for Letter being last char in s
                if index == (len(s)-1):
                    Number+=RomanToNumberDict[s[index]]
                    return Number

                #Check next Index for matching Letters that go with present Letter
                if index != (len(s)-1) and RomanToNumberDict[s[index]] < RomanToNumberDict[s[index + 1]]:
                    Number-=RomanToNumberDict[s[index]]
            
                else:
                    # Simple Addition
                    Number+=RomanToNumberDict[s[index]]
            else:
                Number+=RomanToNumberDict[s[index]]

        return Number
        

def ReconRomanToInt():
    with open("RomanToInt.csv", "r") as fileReader:
        for Line in fileReader:
            Line = Line.strip()
            # print("Reading:", Line)
            Num, Roman = Line.split(",")
            if(Num == "Arabic"):
                continue
            Sol = Solution.romanToInt(Roman)
            if Sol == int(Num):
                # print("Passed for:", Num, Roman)
                pass
            else:
                print("Failed for:", Num, Roman, "Got:", Sol)

if __name__ == '__main__':
    ReconRomanToInt()
    # print(Solution.romanToInt("XV"))


