import lib # import custom module (lib.py) in same directory as this file (import.py)

print(lib.FACTOR)

print(lib.calculate_growthrate(2))

monsters = lib.spawn_monsters()

new_monster = lib.Monster("Crazy", "sashimi")
monsters.append(new_monster)

for monster in monsters:
    print(f"{monster.name} love {monster.food}!")
