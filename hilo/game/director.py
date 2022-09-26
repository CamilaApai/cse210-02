from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        guess (string) : Wheter the player choose a higher or lower number.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = Card()
        self.guess = ""
        self.is_playing = True
        self.points = 300
        self.score = 0
        self.current_card = ""
       

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self.card.draw_card()
        self.do_outputs()

        while self.is_playing:
           self.get_inputs()
           self.do_updates()
           self.do_outputs()

    def get_input(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        guess = input("Higher or lower? [h/l] ")
        #self.do_outputs = (guess == "h" or "l")

        keep_playing = input("Play again? [y/n] ")
        self.is_playing = (keep_playing == "y")

       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.points = 0
        if not self.is_playing:
            return 

        guess = self.get_input().guess
        previous_card = self.card.value
        current_card = self.card.draw_card()

        if guess == "h":
            if current_card > previous_card:
                self.score = self.points + 100 
            else:
                self.score = self.points - 75

        elif guess == "l":
            if current_card < previous_card:
                self.score = self.points + 100 
            else:
                self.score = self.points - 75

        else:
            self.score == 0

        if self.score == 0:
            self.is_playing == False         

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

     
        print(f"The card is: {self.card.value}")
        print(f"Next card was: {self.current_card}")
        print(f"Your score is: {self.score}")
        self.is_playing = (self.points > 0)