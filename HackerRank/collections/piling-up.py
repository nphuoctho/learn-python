"""
Pilling Up!

Input:
2
6
4 3 2 1 3 4
3
1 3 2

Output:
Yes
No
"""

import sys
from collections import deque

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))
        d = deque(blocks)

        last = sys.maxsize

        while len(d) != 0:
            left = d[0]
            right = d[-1]

            if left <= last and right <= last:
                if left >= right:
                    chosen = left
                    d.popleft()
                else:
                    chosen = right
                    d.pop()
            elif left <= last:
                chosen = left
                d.popleft()
            elif right <= last:
                chosen = right
                d.pop()
            else:
                print("No")
                break

            last = chosen
        else:
            print("Yes")
