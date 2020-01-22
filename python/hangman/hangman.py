# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = "".ljust(len(self.word), "_")


    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError(f"The game is finished with a {self.status} for the player.")

        if char in self.word and char not in self.masked_word:
            positions = [p for p, c in enumerate(self.word) if c == char]

            for index in positions:
                self.masked_word = self.masked_word[:index] + char + self.masked_word[index+1:]

            if self.masked_word == self.word:
                self.status = STATUS_WIN
        
        else:
            self.remaining_guesses -= 1
            
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE


    def get_masked_word(self):
        return self.masked_word


    def get_status(self):
        return self.status
