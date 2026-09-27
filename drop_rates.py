from fractions import Fraction
import random


def roll(monster):

    for table, rates in monster.items():
        max_denom = 0
        for item, value in rates.items():
            if value.denominator > max_denom:
                max_denom = value.denominator

        drops = []
        for item, value in rates.items():
            item_chance = int(value.numerator * (max_denom / value.denominator))
            drops.extend([item] * item_chance)
            drops.extend([None] * (value.denominator - value.numerator))

        if table == "always":
            for item in drops:
                print("You received: " + item)

        if table == "preroll":
            rand_index = random.randrange(len(drops))
            item_received = drops[rand_index]
            print(item_received)
            if item_received:
                print("You received: " + item_received)


if __name__ == '__main__':
    brutus = {
        "always": {"Bull bones": Fraction("1") / Fraction("1"),
                   "Raw t-bone steak": Fraction("1") / Fraction("1")
        },
        "preroll": {
            "Mooleta": Fraction("1") / Fraction("150"),
            "Bottomless Milk Bucket": Fraction("1") / Fraction("37.5"),
            "Cow Slippers": Fraction("1") / Fraction("150")
        }

    }

    roll(brutus)
    