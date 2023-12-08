from dataclasses import dataclass
from enum import Enum
from collections import defaultdict
from functools import cmp_to_key

PART = 1
RANKS = "AKQJT98765432"[::-1]
RANKS_JOKE  = "AKQT98765432J"[::-1]
FILE = "./input.txt"

class HandType(Enum):
    Five = 6
    Four = 5
    FullHouse = 4
    Three = 3
    TwoPair = 2
    OnePair = 1
    HighCard = 0

@dataclass
class Hand:
    bid: int
    val: str
    hand_type: HandType

def hand_cmp(item1: Hand, item2: Hand):
    if item1.hand_type.value > item2.hand_type.value:
        return 1
    elif item1.hand_type.value < item2.hand_type.value:
        return -1
    else:
        ranks = RANKS if PART == 1 else RANKS_JOKE
        for c1, c2 in zip(item1.val, item2.val):
            if ranks.find(c1) > ranks.find(c2):
                return 1
            elif ranks.find(c1) < ranks.find(c2):
                return -1
    return 0

def parse():
    data = open(FILE).readlines()
    cards = []

    for line in data:
        hand, bid = line.split()

        counts = defaultdict(int)

        for c in hand:
            counts[c] += 1

        hand_type = None
        cards_count = len(hand)


        if PART == 2:
            if hand == "JJJJJ":
                hand_type = HandType.Five
            elif 'J' in hand:
                del counts["J"]

                # Most common letter
                x = hand.replace("J", sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][0])

                # Recount after applying changes
                counts = defaultdict(int)
                for c in x:
                    counts[c] += 1

        distinct_count = len(counts.items())
        counts_values = list(counts.values())


        if distinct_count == cards_count:
            hand_type = HandType.HighCard
        elif distinct_count == 1:
            hand_type = HandType.Five
        elif distinct_count == 2 and any([True for x in counts_values if x == 1]):
            hand_type = HandType.Four
        elif counts_values[0] == 3 and counts_values[1] == 2 or counts_values[0] == 2 and counts_values[1] == 3:
            hand_type = HandType.FullHouse
        elif distinct_count == 3 and any([True for x in counts_values if x == 3]):
            hand_type = HandType.Three
        elif distinct_count == 4 and len([True for x in counts_values if x == 1]) == 3:
            hand_type = HandType.OnePair
        else:
            hand_type = HandType.TwoPair

        card = Hand(int(bid), hand, hand_type)
        cards.append(card)

    return cards

def sum_cards(cards):
    acc = 0

    cards.sort(key=cmp_to_key(hand_cmp))

    for i, card in enumerate(cards):
        acc += (i+1) * card.bid

    return acc

def part1():
    cards = parse()
    print(sum_cards(cards))

def part2():
    global PART
    PART = 2

    cards = parse()
    print(sum_cards(cards))


if __name__ == "__main__":
    FILE = "./input.txt"

    part1()
    part2()
