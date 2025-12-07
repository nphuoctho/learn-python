def split_and_join(line: str):
    w = line.strip().split(" ")
    return "-".join(w)


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
