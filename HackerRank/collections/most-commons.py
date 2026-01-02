from collections import Counter

if __name__ == "__main__":
    s = input().strip()
    counter = Counter(s)
    print(counter.items())

    sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:3]
    for key, value in sorted_counter:
        print(f"{key} {value}")
