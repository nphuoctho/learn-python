from collections import deque

if __name__ == "__main__":
    n = int(input())

    d = deque()
    for _ in range(n):
        s = list(input().split())

        match s[0]:
            case "append":
                d.append(s[1])
            case "appendleft":
                d.appendleft(s[1])
            case "pop":
                d.pop()
            case "popleft":
                d.popleft()
    print(*d)
