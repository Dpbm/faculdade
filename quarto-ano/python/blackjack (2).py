from typing import Self, List
from copy import deepcopy
from enum import Enum
from random import shuffle

class CardValues(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    QUEEN = 10
    KING = 10
    VALET = 10

class Suits(Enum):
    DIAMONS=1
    HEARTS=2
    CLUBS=3
    SPADES=4

class Card:
    def __init__(self, suit:Enum, value:Enum):
        self._suit = suit
        self._value = value

    def clone(self) -> Self:
        return deepcopy(self)

    @property
    def value(self):
        return self._value.value

    def __str__(self):
        return "A %s of %s"%(self._value.name.lower(), self._suit.name.lower())

Hand = List[Card]

class Game:
    def __init__(
        self, 
        suits_options:Enum, 
        card_values_options:Enum
    ):
        self._hand = []

        self._init_hand(
            suits_options,
            card_values_options
        )

    def _init_hand(
        self, 
        suits_options:Enum, 
        card_values_options:Enum
    ):
        for suit in suits_options.__members__.values():
            for card in card_values_options.__members__.values():
                self._hand.append(Card(suit, card))

        shuffle(self._hand)

    @property
    def hand(self) -> Hand:
        return self._hand

    def get_next_card(self) -> Card:
        return self._hand.pop()

class Agent:
    def __init__(self):
        self._cards = []

    def add_card(self,card:Card):
        self._cards.append(card)

    @property
    def total_sum(self):
        return sum([card.value for card in self._cards])


if __name__ == "__main__":
    game = Game(Suits, CardValues)
    agent = Agent()

    c = game.get_next_card()
    agent.add_card(c)

    print(agent.total_sum)


