import random


class Card:
    """A piece of paper that has a number printed on it.

    The responsibility of the Card is to generate a value to display.

    Attributes:
        value (int): The number of the card.
    """

    def __init__(self):
        """Constructs a new instance of Card with a value attribute.

        Args:
            self (Card): An instance of Card.
        """
        self.value = 0

    def draw_card(self):
        """Generates a new random value.

        Args:
            self (Card): An instance of Card.
        """

        self.value = random.randint(1, 13)
        return self.value
