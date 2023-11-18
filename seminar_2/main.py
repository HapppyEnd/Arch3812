"""Main module."""
from random import randint
from generators import (BronzeGenerator, ChestSurpriseGenerator, GemGenerator,
                        GoldGenerator, NothingGenerator, PlatinumGenerator,
                        SapphireGenerator, SilverGenerator)

if __name__ == '__main__':
    rewards = [BronzeGenerator(), ChestSurpriseGenerator(), NothingGenerator(),
               SapphireGenerator(), SilverGenerator(), GoldGenerator(),
               PlatinumGenerator(), GemGenerator()]

    for i in range(15):
        random_int = randint(0, 55)
        if random_int < 50:
            rewards[random_int // 10].create_item().open()
        elif random_int in [50, 51, 52]:
            rewards[5].create_item().open()
        elif random_int in [53, 54]:
            rewards[6].create_item().open()
        else:
            rewards[7].create_item().open()
