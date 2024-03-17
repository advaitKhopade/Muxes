import random
import WordDictionary

class UserInterface:
    def __init__(self):
        self.guessed_words = set()
        self.boss_word = ""
        self.boss_word_points = 0

    def add_guessed_word(self, word):
        if word not in self.guessed_words and word not in WordDictionary().word_dict:
            self.guessed_words.add(word)

    def set_boss_word(self, word):
        self.boss_word = word

    def add_boss_word_points(self, points):
        self.boss_word_points += points

    def get_boss_word_points(self):
        return self.boss_word_points

    def get_score(self):
        return sum(WordDictionary().word_dict.get(word, 0) for word in self.guessed_words) + self.boss_word_points

    def reset(self):
        self.guessed_words = set()
        self.boss_word = ""
        self.boss_word_points = 0

def main():
    wf = WordDictionary()
    user_iface = UserInterface()

    # Initialize the word set
    word_set = wf.initialize_word_list()

    # Randomly select a boss word
    boss_word = random.choice(list(word_set))

    #