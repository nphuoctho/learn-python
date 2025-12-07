#!/bin/python3

import os


# Complete the solve function below.
def solve(s: str) -> str:
    words = s.split(" ")
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)

    fptr.write(result + "\n")

    fptr.close()
