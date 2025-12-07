if __name__ == "__main__":
    s: str = input()

    checks = [
        lambda s: any(c.isalnum() for c in s),
        lambda s: any(c.isalpha() for c in s),
        lambda s: any(c.isdigit() for c in s),
        lambda s: any(c.islower() for c in s),
        lambda s: any(c.isupper() for c in s),
    ]

    for func in checks:
        print(func(s))
