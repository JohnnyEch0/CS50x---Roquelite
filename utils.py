""" This file contains utility functions and classes that are used in the game. """
import random

def get_input(text, options):
    while True:
        answer = input(f"{text}\n")
        answer = answer.upper()
        # options may have exit="Any other key"
        if answer in options or "Any other key" in options:
            # print(f"\n")
            return answer
        elif answer == "ESC":
            print(f"Goodbye!")
            exit()
        else:
            print(f"Unvalid Input.    ")

class Vector2:
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.data = [self.x, self.y]

    def __iadd__(self, other):
        if isinstance(other, Vector2):
            self.x += other.x
            self.y += other.y
            self.data = [self.x, self.y]
            return self
        else:
            raise TypeError("Addition is only supported with Vector2")

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


    def __getitem__(self, index):
        if isinstance(index, int):
            if 0 <= index < 2:
                return self.data[index]  # Access components using an internal list
            else:
                raise IndexError("Index out of range")
        else:
            raise TypeError("Indices must be integers")

    def __setitem__(self, index, value):
        if isinstance(index, int):
            if 0 <= index < 2:
                self.data[index] = value
            else:
                raise IndexError("Index out of range")
        else:
            raise TypeError("Indices must be integers")

def random_choice(dataset):
    return random.choices(list(dataset.keys()), weights=list(dataset.values()))[0]

def random_choice_list_tuple(dataset):
    """ dataset is a list of tuples, where the first element of the tuple is the choice and the second element is the weight """
    weights = [item[1] for item in dataset]
    choices = [item[0] for item in dataset]
    return random.choices(choices, weights=weights)[0]