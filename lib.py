# CUSTOM MODULE(/LIBRARY)
FACTOR = 5

class Monster:
    def __init__(self, name="Me", food="cookies"):
        self.name = name
        self.food = food


def spawn_monsters():
    return [Monster("Happy", "carrots"), 
            Monster("Bashful", "ice-creams"), 
            Monster("Wild", "cookies")]


def calculate_growthrate(adjustment=3):
    return 25 * FACTOR + adjustment

def _test_library():
    monster = Monster("Silly", "pizza")
    print(f"{monster.name} love {monster.food}!")

if __name__ == "__main__":  # only runs if this file is run directly, not when imported as a module
    _test_library()         # works because Python will set a special variable __name__ as "__main__" only when you run your code as a script
