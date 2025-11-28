"""string module"""
import string
import json


TEXT = "There can be no covenants between men and lions."

def char_classifier(text: str) -> dict:
    categories = {}
    for c in text:
        if c in string.ascii_lowercase:
            key = "lowercase"
        elif c in string.ascii_uppercase:
            key = "uppercase"
        else:
            key = "other"
        """
        if key not in categories:
            categories[key] = set()
            categories[key].add(c)
        """
        # setdefault replacess the above
        categories.setdefault(key, set()).add(c)
    
    return categories 


def pretty_print(categories: dict[str, set]) -> None:
    for category in categories:
        print(f"{category}", " ".join(categories[category]))


if __name__ == "__main__":
    categories_dict = char_classifier(TEXT)
    pretty_print(categories_dict)