'''
In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand.
A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456

Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand.
If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand.
If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.
'''

# Part 1
# Find the rank of every hand in your set. What are the total winnings?

CARD_RANK = {"A": 14,
             "K": 13,
             "Q": 12,
             "J": 11,
             "T": 10,
             "9": 9,
             "8": 8,
             "7": 7,
             "6": 6,
             "5": 5,
             "4": 4,
             "3": 3,
             "2": 2}

class Node:
    def __init__(self, hand, bid, htype):
        self.hand = hand
        self.bid = bid
        self.htype = htype
        self.parent = None
        self.lower = None
        self.higher = None

def hand_type(hand):
    card_counter = {k:0 for k in CARD_RANK}
    for card in hand:
        card_counter[card] += 1
        
    max_match = max(card_counter.values())
    
    if max_match == 5:
        return 1
    elif max_match == 4:
        return 2
    elif max_match == 3:
        if 2 in card_counter.values():
            return 3
        else:
            return 4
    elif len[k for k,v in card_counter.items() if v > 0] == 3:
        return 5
    elif max_match == 2:
        return 6
    else:
        return 7

def camel_tree(cards):
    top_node = Node(cards[0][0],cards[0][1],cards[0][2])
    cur_node = top_node
    
    for c in cards[1:]:
        if c[2] < cur_node.hand_type:
            cur_node.lower = Node(c[0],c[1],c[2])
            # need a sorted binary tree creation function here

# parse tree to get ranks of each hand (leftmost is the weakest == 1, rightmost is strongest == max)
# can also calc winnings with bid * rank

with open("day7_example.txt","r") as f:
    raw = f.readlines()
    camel_cards = [(row.split()[0],int(row.split()[1])) for row in raw]
    camel_cats = [(c[0],c[1],hand_type(c[0])) for c in camel_cards]

    
