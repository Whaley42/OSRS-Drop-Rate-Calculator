from fractions import Fraction
import random

def roll_table(table):

    max_denom = 0
    for item, value in table.items():
        if value.denominator > max_denom:
            max_denom = value.denominator

    drops = []
    for item, value in table.items():
        item_chance = int(value.numerator * (max_denom / value.denominator))
        drops.extend([item] * item_chance)
        drops.extend([None] * (value.denominator - value.numerator))

    rand_index = random.randrange(len(drops))
    item_received = drops[rand_index]
    return item_received

def roll(monster):

    items_received = []
    for item in monster["always"]:
        items_received.append(item)

    item_received = roll_table(monster["preroll"])
    if not item_received:
        item_received = roll_table(monster["main"])
    
    if item_received:
        items_received.append(item_received)

    item_received = roll_table(monster["tertiary"])

    if item_received:
        items_received.append(item_received)

    return items_received
            

def run_simulation(monster, amount):

    item_counts = {}
    for i in range(amount):
        items_received = roll(monster)
        for item in items_received:
            if item in item_counts:
                item_counts[item] += 1
            else: 
                item_counts[item] = 1
    
    print(item_counts)


if __name__ == '__main__':
    brutus = {
        "always": {"Bull bones": Fraction("1") / Fraction("1"),
                   "Raw t-bone steak": Fraction("1") / Fraction("1")
        },
        "preroll": {
            "Mooleta": Fraction("1") / Fraction("150"),
            "Bottomless Milk Bucket": Fraction("1") / Fraction("37.5"),
            "Cow Slippers": Fraction("1") / Fraction("150")
        },
        "main": {
            "Iron Full helm": Fraction("1") / Fraction("40.5"),
            "Iron Platebody": Fraction("1") / Fraction("40.5"),
            "Iron Platelegs": Fraction("1") / Fraction("81"),
            "Iron Plateskirt": Fraction("1") / Fraction("81"),
            "Iron Arrow": Fraction("1") / Fraction("8.1"),
            "Air Rune": Fraction("1") / Fraction("8.1"),
            "Mind Rune": Fraction("1") / Fraction("10.13"),
            "Chaos Rune": Fraction("1") / Fraction("40.5"),
            "Potato Seed": Fraction("1") / Fraction("8.1"),
            "Acorn": Fraction("1") / Fraction("16.2"),
            "Raw t-bone steak (m)": Fraction("1") / Fraction("8.1"),
            "Cowhide": Fraction("1") / Fraction("8.1"),
            "Oak logs": Fraction("1") / Fraction("16.2"),
            "Logs": Fraction("1") / Fraction("16.2")
        },
        "tertiary": {
            "Clue Scroll (beginner)": Fraction("1") / Fraction ("15"),
            "Clue Scroll (easy)": Fraction("1") / Fraction ("40"),
            "Beef": Fraction("1") / Fraction ("1000"),
        }

    }

    
    run_simulation(brutus, 100)
    