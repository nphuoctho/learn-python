def minion_game(string: str):
    vowels = "AEIOU"
    u1_score = 0
    u2_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            u1_score += length - i
        else:
            u2_score += length - i

    if u1_score > u2_score:
        print(f"Kevin {u1_score}")
    elif u2_score > u1_score:
        print(f"Stuart {u2_score}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
