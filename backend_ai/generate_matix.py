import random
import string


def initialize_grid(size):
    return [["." for _ in range(size)] for _ in range(size)]


def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


def can_place_word(grid, word, row, col, dx, dy):
    if dx == 0 and dy == 0:
        return False
    length = len(word)
    end_row = row + length * dy
    end_col = col + length * dx
    if end_row < 0 or end_row > len(grid) or end_col < 0 or end_col > len(grid[0]):
        return False
    for i in range(length):
        new_row, new_col = row + i * dy, col + i * dx
        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            return False
        if grid[new_row][new_col] != "." and grid[new_row][new_col] != word[i]:
            return False
    return True


def place_word(grid, word, row, col, dx, dy):
    for i in range(len(word)):
        new_row, new_col = row + i * dy, col + i * dx
        grid[new_row][new_col] = word[i]


def fill_with_random_letters(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                grid[i][j] = random.choice(string.ascii_lowercase)


def create_crossword(grid_size, words):
    grid = initialize_grid(grid_size)
    directions = [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]  # Right, Down, Left, Up, Diagonal down-right, Diagonal up-left, Diagonal down-left, Diagonal up-right
    for word in words:
        placed = False
        random.shuffle(directions)  # Shuffle directions for each word for randomness
        for dx, dy in directions:
            if placed:
                break
            for row in range(grid_size):
                for col in range(grid_size):
                    if can_place_word(grid, word, row, col, dx, dy):
                        place_word(grid, word, row, col, dx, dy)
                        placed = True
                        break
                if placed:
                    break
    fill_with_random_letters(grid)
    return grid


# Example usage
grid_size = 16
words = ["hello", "world", "python", "code"]
crossword = create_crossword(grid_size, words)
print_grid(crossword)
