from collections import Counter

if __name__ == "__main__":
    n = int(input())

    w_arr = []
    for i in range(n):
        w_arr.append(input())

    w_counter = Counter(w_arr)
    count = [counter for key, counter in w_counter.items()]

    print(len(set(w_arr)))
    print(*w_counter.values())
