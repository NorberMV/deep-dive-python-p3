"""Counting the character appearance in a string"""
import json


def character_counter(text):
    counts = dict()

    for char in text:
        char = char.lower().strip()
        if char:
            counts[char] = counts.get(char, 0) + 1

    return counts


if __name__ == "__main__":
    text = "There can be no covenants between men and lions."
    counter_dict = character_counter(text)
    print(json.dumps(counter_dict, ensure_ascii=False, indent=4))
