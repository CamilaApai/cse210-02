from game.card import Card


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (class): A random card to be displayed.
        is_playing (boolean): Whether or not the game is being played.
        guess (string) : Whether the player choose a higher or lower number.
        score (int): The score for one round of play.
        current_card(int) = A random second card to be displayed after the first one.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.guess = ""
        self.is_playing = True
        self.score = 300
        self.current_card = 0

    def start_game(self):
        """Starts the game by drawing the first card and running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        self.card.draw_card()

        while self.is_playing:
            self.do_outputs()
            self.do_updates()

    def get_input(self):
        """Ask the user if they think the next card will be higher or lower than the first one and return its answer.

        Args:
            self (Director): An instance of Director.
        """
        self.guess = input("Higher or lower? [h/l] ")
        return self.guess

    def do_updates(self):
        """Displays the next card, and updates the player scores.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        guess = self.get_input()
        previous_card = self.card.value
        self.card.draw_card()
        self.current_card = self.card.value

        if guess == "h":
            if self.current_card > previous_card:
                self.score += 100
            elif self.current_card < previous_card:
                self.score -= 75
            else:
                self.is_playing

        elif guess == "l":
            if self.current_card < previous_card:
                self.score += 100
            elif self.current_card > previous_card:
                self.score -= 75
            else:
                self.is_playing

        if self.score <= 0:
            self.is_playing == False

    def do_outputs(self):
        """Displays the previous and current card, and the score. 

        Args:
            self (Director): An instance of Director.
        """

        while self.is_playing:
            print("The card is: {}".format(self.card.value))
            self.do_updates()
            print("Next card was: {}".format(self.current_card))
            print("Your score is: {}".format(self.score))
            self.play_again()

    def play_again(self):
        """Asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if self.score > 0:
            keep_playing = input("Play again? [y/n] ")
            print()
            if keep_playing == "y":
                self.is_playing
            else:
                self.is_playing = False
        else:
            self.is_playing = False
