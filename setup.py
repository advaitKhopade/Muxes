import tkinter as tk
import random
import time


class WordSearchGame(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Word Search Game")
        self.geometry("500x550")

        self.rows = 16
        self.cols = 16
        self.words = ["PYTHON", "JAVA", "CPLUSPLUS", "RUBY", "HTML"]
        self.boss_word = random.choice(self.words)
        self.pawn_words = [word for word in self.words if word != self.boss_word]
        self.board_timer = None
        self.round_timer = None
        self.found_words = []

        self.create_widgets()
        self.create_wordsearch()
        self.draw_wordsearch()
        self.update_timers()
        self.shuffle_interval = 180000  # 3 minutes in milliseconds
        self.start_new_game()

    def start_new_game(self):
        self.boss_word = random.choice(self.words)
        self.found_words = []
        self.words_found_text.delete("1.0", tk.END)
        self.create_wordsearch()
        self.draw_wordsearch()
        self.riddle_label.config(text=f"Find the boss word: {self.boss_word}")
        self.restart_timers()
        # Call shuffle wordsearch every 3 minutes
        self.after(self.shuffle_interval, self.shuffle_wordsearch)

    def shuffle_wordsearch(self):
        self.start_new_game()

    def create_wordsearch(self):
        self.wordsearch = [[" " for _ in range(self.cols)] for _ in range(self.rows)]

        for word in self.words:
            placed = False
            while not placed:
                direction = random.choice(["horizontal", "vertical", "diagonal"])
                if direction == "horizontal":
                    start_row = random.randint(0, self.rows - 1)
                    start_col = random.randint(0, self.cols - len(word))
                    if all(
                        self.wordsearch[start_row][start_col + i] == " "
                        or self.wordsearch[start_row][start_col + i] == word[i]
                        for i in range(len(word))
                    ):
                        for i in range(len(word)):
                            self.wordsearch[start_row][start_col + i] = word[i]
                        placed = True
                elif direction == "vertical":
                    start_row = random.randint(0, self.rows - len(word))
                    start_col = random.randint(0, self.cols - 1)
                    if all(
                        self.wordsearch[start_row + i][start_col] == " "
                        or self.wordsearch[start_row + i][start_col] == word[i]
                        for i in range(len(word))
                    ):
                        for i in range(len(word)):
                            self.wordsearch[start_row + i][start_col] = word[i]
                        placed = True
                else:
                    start_row = random.randint(0, self.rows - len(word))
                    start_col = random.randint(0, self.cols - len(word))
                    if all(
                        self.wordsearch[start_row + i][start_col + i] == " "
                        or self.wordsearch[start_row + i][start_col + i] == word[i]
                        for i in range(len(word))
                    ):
                        for i in range(len(word)):
                            self.wordsearch[start_row + i][start_col + i] = word[i]
                        placed = True

        # Fill empty spaces with random letters
        for i in range(self.rows):
            for j in range(self.cols):
                if self.wordsearch[i][j] == " ":
                    self.wordsearch[i][j] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=480, height=480)
        self.canvas.pack()

        self.riddle_label = tk.Label(self, text=f"Find the boss word: {self.boss_word}")
        self.riddle_label.pack()

        self.entry_label = tk.Label(self, text="Enter boss word:")
        self.entry_label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()
        self.entry.focus_set()

        self.submit_button = tk.Button(
            self, text="Submit", command=self.check_boss_word
        )
        self.submit_button.pack()

        self.message_label = tk.Label(self, text="")
        self.message_label.pack()

        self.words_found_label = tk.Label(self, text="Words Found:")
        self.words_found_label.pack()

        self.words_found_text = tk.Text(self, height=4, width=40)
        self.words_found_text.pack()

        self.round_timer_label = tk.Label(self, text="Round Timer: 3:00")
        self.round_timer_label.pack()

        self.board_timer_label = tk.Label(self, text="Board Shuffling Timer: 0:30")
        self.board_timer_label.pack()

    def draw_wordsearch(self):
        self.rect_ids = []
        self.text_ids = []
        for i in range(self.rows):
            for j in range(self.cols):
                x1, y1 = j * 30, i * 30
                x2, y2 = x1 + 30, y1 + 30
                rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
                text_id = self.canvas.create_text(
                    x1 + 15,
                    y1 + 15,
                    text=self.wordsearch[i][j],
                    font=("Arial", 10, "bold"),
                )
                self.rect_ids.append(rect_id)
                self.text_ids.append(text_id)

    def check_boss_word(self):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if guess == self.boss_word and guess not in self.found_words:
            self.found_words.append(guess)
            self.words_found_text.insert(tk.END, f"{guess}\n")
            self.words_found_text.see(tk.END)
            self.message_label.config(
                text=f"Boss word {self.boss_word} found! You earned 10 points."
            )
            self.update_score()
            # Shuffle the board and change the boss word
            self.after(self.shuffle_interval, self.shuffle_wordsearch)
        else:
            self.message_label.config(text="Incorrect boss word. Try again.")

    def restart_timers(self):
        if self.round_timer is not None:
            self.after_cancel(self.round_timer)
        if self.board_timer is not None:
            self.after_cancel(self.board_timer)
        self.update_timers()

    def update_score(self):
        self.score = 10 * len(self.found_words)
        self.score_label.config(text=f"Score: {self.score}")

    def update_timers(self):
        self.round_time_left = 180
        self.board_shuffle_time_left = 30
        self.start_round_timer()
        self.start_board_timer()

    def start_round_timer(self):
        self.round_timer = self.round_time_left
        self.update_round_timer()

    def update_round_timer(self):
        minutes = self.round_timer // 60
        seconds = self.round_timer % 60
        self.round_timer_label.config(text=f"Round Timer: {minutes:02}:{seconds:02}")

        if self.round_timer > 0:
            self.round_timer -= 1
            self.after(1000, self.update_round_timer)
        else:
            self.round_timer_label.config(text="Round Timer: 0:00")
            self.board_timer_label.config(text="Board Shuffling Timer: 0:00")
            self.message_label.config(text="Time's up! Round over.")

    def start_board_timer(self):
        self.board_timer = self.board_shuffle_time_left
        self.update_board_timer()

    def update_board_timer(self):
        minutes = self.board_timer // 60
        seconds = self.board_timer % 60
        self.board_timer_label.config(
            text=f"Board Shuffling Timer: {minutes:02}:{seconds:02}"
        )

        if self.board_timer > 0:
            self.board_timer -= 1
            if self.board_timer % 30 == 0:
                self.create_wordsearch()
                self.draw_wordsearch()
            self.after(1000, self.update_board_timer)


if __name__ == "__main__":
    app = WordSearchGame()
    app.mainloop()
