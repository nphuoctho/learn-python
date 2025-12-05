if __name__ == "__main__":
    n: int = int(input().strip())
    lst: list[int] = list(map(int, input().split()))
    t: tuple[int, ...] = tuple(lst)
    print(hash(t))
