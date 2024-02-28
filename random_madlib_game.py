# Selects a random madlib from madlib folder
print("\n")

from madlib_selection import michael_bay, pizza_day, zoo_day
import random

if __name__ == "__main__":
    m = random.choice([michael_bay, pizza_day, zoo_day])
    m.madlib()

print("\n")

