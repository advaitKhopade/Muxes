import random
import os
import openai
import requests
from bs4 import BeautifulSoup as Soup
from nltk.corpus import words
import sys

# Set the OpenAI API key from an environment variable for security.
openai.api_key = "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"
if not openai.api_key:
    print("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

class WordFlush:
    def __init__(self):
        self.words = words
        self.url = "https://raw.githubusercontent.com/cduica/Oxford-Dictionary-Json/master/dicts.json"
        self.word = ""  # boss word
        self.word_riddle = ""  # boss word riddle
        self.word_dict = {}
        self.word_set = set()
        self.word_list_file = "word_list.json"
        self.word_list_file_path = os.path.join(os.path.dirname(__file__), self.word_list_file)
        self.word_list_file_path = os.path.abspath(self.word_list_file_path)
        self.word_list_file_path = os.path.normpath(self.word_list_file_path)

    def get_words_from_api(self):
        self.word_freq = {}
        for word in self.words.words():
            if (len(word) > 4 and len(word) < 8) and word.isalpha() and word.islower() and word not in self.word_freq:
                self.word_freq[word] = self.word_freq.get(word, 0) + 1
        self.word_freq = dict(sorted(self.word_freq.items(), key=lambda x: x[1], reverse=True))

    def initialize_word_list(self):
        self.get_words_from_api()
        self.word_set = set(sorted(random.sample(list(self.word_freq.keys()), 5)))
        return self.word_set

def main():
    wf = WordFlush()
    word_set = wf.initialize_word_list()
    

    

    print("Remaining words:")
    print(word_set)

if __name__ == "__main__":
    main()
