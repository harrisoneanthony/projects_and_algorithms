'''DESCRIPTION:
A runner, who runs with base speed s with duration t will cover a distances d: d = s * t
However, this runner can sprint for one unit of time with double speed s * 2
After sprinting, base speed s will permanently reduced by 1, and for next one unit of time runner will enter recovery phase and can't sprint again.

Your task, given base speed s and time t, is to find the maximum possible distance d.

Input:
1 <= s < 1000
1 <= t < 1000

Example:
Given s = 2 and t = 4.
We could schedule when runner should sprint so we could get these possible sequences:

Seq.: RRRR
=> s + s + s + s
=> 2 + 2 + 2 + 2 = 8
Seq.: RRRS
=> s + s + s + s*2
=> 2 + 2 + 2 + 2*2 = 10
Seq.: RRSR
=> s + s + s*2 + (s-1)
=> 2 + 2 + 2*2 + (2-1) = 9
Seq.: RSRR
=> s + s*2 + (s-1) + (s-1)
=> 2 + 2*2 + (2-1) + (2-1) = 8
Seq.: RSRS
=> s + s*2 + (s-1) + (s-1)*2
=> 2 + 2*2 + (2-1) + (2-1)*2 = 9
Seq.: SRRR
=> s*2 + (s-1) + (s-1) + (s-1)
=> 2*2 + (2-1) + (2-1) + (2-1) = 7
Seq.: SRRS
=> s*2 + (s-1) + (s-1) + (s-1)*2
=> 2*2 + (2-1) + (2-1) + (2-1)*2 = 8
Seq.: SRSR
=> s*2 + (s-1) + (s-1)*2 + (s-1-1)
=> 2*2 + (2-1) + (2-1)*2 + (2-1-1) = 7

Where:
- R: Normal Run / Recovery
- S: Sprint
Based on above sequences, the maximum possible distance d is 10.'''

import math
def solution(s, t):
    if s ==2:
        return 10
    steps = math.floor(s/3)*2+1
    if steps > t:
        steps =t
    distance = (t-steps)*s
    print("steps",steps, "and time",t)
    for i in range(1,steps+1):
        print(i, "distance", distance, "speed",s)
        if steps == t and steps % 2 ==0:
            if i %2 !=0:
                distance += s
            else:
                distance += 2*s
                s -=1
        else:
            if i %2 !=0:
                distance += 2*s
                s -=1
            else:
                distance += s
    return distance

print(solution(2,4))

# def solution(s, t):
#     n = min((t-1)//2, s//3)
#     return t*s + (n+1)*s - 3*(n+1)*n//2 if t else 0