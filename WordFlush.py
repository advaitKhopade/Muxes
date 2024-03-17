import random
import os
import requests
from bs4 import BeautifulSoup as Soup
import openai
from nltk.corpus import words

class WordFlush:
    def __init__(self):
        self.words = words
        self.url = "https://www.dictionary.com/list/A"
        self.word = ""                          #boss word
        self.word_riddle = ""                #boss word riddle
        self.word_dict = {}
        self.word_set = set()
        self.word_list_file = "word_list.json"
        self.word_list_file_path = os.path.join(os.path.dirname(__file__), self.word_list_file)
        self.word_list_file_path = os.path.abspath(self.word_list_file_path)
        self.word_list_file_path = os.path.normpath(self.word_list_file_path)

    def get_words_from_api(self):
        self.word_freq = {}
        for word in self.words.words():
            if len(word) > 4:
                self.word_freq[word] = self.word_freq.get(word, 0) + 1

        self.word_freq = dict(sorted(self.word_freq.items(), key=lambda x: x[1], reverse=True))

    def initialize_word_list(self):
        self.get_words_from_api()
        self.word_set = set(random.sample(self.word_freq.keys(), 5))
        return self.word_set

    def get_word_riddles(self):
        riddle_prompt = f"Generate 5 creative riddles for the following words: {', '.join(self.word_set)}. Each riddle should have two parts: a clue and the answer. Use words not in the list to provide hints and explanations. "
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=riddle_prompt,
            temperature=0.5,
            max_tokens=150,
            frequency_penalty=0.5,
            presence_penalty=0.5,
            best_of=5
        )

        riddles = response.choices[0].text.strip().split('\n\n')
        riddle_dict = {}

    def get_word_riddles(self):
        riddles = []  # Define the variable "riddles" as an empty list
        riddle_dict = {}  # Define the variable "riddle_dict" as an empty dictionary
        for i, riddle in enumerate(riddles):
            riddle_clue = riddle.split('\n')[0].strip().split('.')[1].strip()
            riddle_answer = riddle.split('\n')[1].strip()

            if riddle_clue not in riddle_dict:
                riddle_dict[riddle_clue] = self.word_set.copy()

            riddle_dict[riddle_clue].remove(riddle_answer)

        return riddle_dict
