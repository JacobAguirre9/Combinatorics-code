

# A common way to represent a poset as an iterable list data structure in Python would be to use a list of tuples, where each tuple contains an element and its relation to other elements.

# Here's an example of how you might represent a poset as a list of tuples:
poset = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd')]


def height_of_poset(poset):
    height = 0
    for element in poset:
        current_height = 1
        for other_element in poset:
            if other_element != element and other_element <= element:
                current_height += 1
        height = max(height, current_height)
    return height
