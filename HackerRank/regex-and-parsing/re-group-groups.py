import re

if __name__ == "__main__":
    s = input()
    m = re.search(r"([a-zA-Z0-9])\1+", s)
    print(m.group(1)) if m else print(-1)
