"""This is what setdefault does under the hood"""

def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]


if __name__ == "__main__":
    d = dict(zip("abc", range(1, 4)))
    print(d)
    print(insert_if_not_present(d, "a", 100))
    print(d.setdefault("©ƒç", 100))