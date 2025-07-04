from collections import deque 

NumTestCases = int(input())

for Testcase in range(0, NumTestCases):
    LengthBlocks = input()
    Blocks = deque(map(int, input().split()))
    PileList = []
    PileListPointer = -1
    # print("For Loop:", Testcase)

    # print(Blocks[0])
    # print(Blocks[-1])
    
    while( len(Blocks) > 0 ):
        #Pop Left
        if(Blocks[0] >= Blocks[-1]):
            if(not PileList):
                PileList.append(Blocks.popleft())
                PileListPointer+=1

            elif( PileList[PileListPointer] >= Blocks[0] ):
                PileList.append(Blocks.popleft())
                PileListPointer+=1
                # print("1st If")

            else:
                print("No")
                break
            
        # Pop Right
        elif(Blocks[0] < Blocks[-1]):
            # print("PileList: ", PileList, PileListPointer)
            # print("Blocks: ", Blocks)
            if(not PileList):
                PileList.append(Blocks.pop())
                PileListPointer+=1

            elif( PileList[PileListPointer] >= Blocks[-1] ):
                PileList.append(Blocks.pop())
                PileListPointer+=1
                # print("2nd If")

            else:
                # print("PileList[PileListPointer]: ", PileList[PileListPointer])
                # print("Blocks[-1]: ", Blocks[-1])
                print("No")
                break

    if len(Blocks) == 0:
        print("Yes")