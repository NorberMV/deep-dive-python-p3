"""
First exercise
# input:
composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}

# output:
sorted_composers = {'Wolfgang': 35,
                    'Frederic': 39,
                    'Ludwig': 56,
                    'Johann': 65}
"""
# First version
# def sorting_dict(dict_input: dict) -> dict:
#     tuple_items = []
#     for i in dict_input.items():
#         tuple_items.append(i)

#     return dict(sorted(tuple_items, key=lambda x: x[1]))

# Second version
# def sorting_dict(dict_input: dict) -> dict:
#     return dict(sorted([i for i in dict_input.items()], key=lambda x: x[1]))


# # Third version
# def sorting_dict(dict_input: dict) -> dict:
#     sorted_dict = {
#         k:v
#         for k, v in sorted(dict_input.items(), key=lambda element: element[1])
#     }
#     return sorted_dict

# Bonus version
class Composer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return repr((self.name, self.age))


composer_objects = [
    Composer('Johann', 65),
    Composer('Ludwig', 56),
    Composer('Frederic', 39),
    Composer('Wolfgang', 35),
]


if __name__ == "__main__":

    # composers = {
    #     'Johann': 65,
    #     'Ludwig': 56,
    #     'Frederic': 39,
    #     'Wolfgang': 35
    # }
    # print(sorting_dict(composers))

    print(sorted(composer_objects, key=lambda elements: elements.age))
