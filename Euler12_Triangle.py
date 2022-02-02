#Solution 1 BAAAAD:
# goal = 0
# triNum = 0
# for i in range (0,100000):
#     goal = 0
#     triNum +=i
#     for j in range (1, triNum + 1):
#         if triNum%j ==0:
#             goal+=1
#         if goal == 500:
#             print(goal)
#             print(triNum)
#             print('----')
#             exit()
            

import math
import time

start_time = time.time()

#Solution 2:
goal = 0
triNum = 0
def square(triNum):
    return math.sqrt(triNum)


for i in range (0,999999999):
    goal = 0
    triNum +=i
    for j in range (1, int(square(triNum))+1):
        if triNum%j == 0:
            goal +=1
    goal *= 2
    if goal >= 500:
        print(triNum)
        print(goal)
        print('it took ',time.time() - start_time)
        exit()









