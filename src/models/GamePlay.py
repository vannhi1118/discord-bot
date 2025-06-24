from constants import ErrorCode
import os

# __file__ is the path to the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../data/words.txt")

# Load once at startup
word_set = {}
raw_set = set()
with open(file_path, encoding="utf-8") as f:
    raw_set = set(line.strip().lower() for line in f if line.strip())
    for word in raw_set:
        if len(word.split()) < 2:
            word_set[word] = {s for s in raw_set if s.startswith(word)}

class GamePlay:
    def __init__(self):
        self.last_word = None
        self.last_user = None
        self.words_used = set()

    def __repr__(self):
        return f"GamePlay(last_word={self.last_word}, last_user={self.last_user}, words_used={self.words_used})"
    
    def add_word(self, composite_word, user):
        print(f"Checking compossite word: {composite_word} by {user}")
        if composite_word in self.words_used:
            return ErrorCode.USED_WORD
        if self.last_word and not composite_word.startswith(self.last_word):
            return ErrorCode.INVALID_WORD
        if composite_word not in raw_set:
            return ErrorCode.NON_EXISTENT_WORD
        if self.last_user and self.last_user == user:
            return ErrorCode.LAST_USER
        
        self.last_word = composite_word.split()[-1]
        self.last_user = user
        self.words_used.add(composite_word)
        print(f"Added word: {self.last_word} by {self.last_user}")
        return True

    def reset(self):
        self.last_word = None
        self.last_user = None
        self.words_used.clear()
        print("GamePlay reset")

    def is_game_end(self, last_word):
        print(f"Checking possible composite words: {word_set[last_word] if last_word in word_set else 'not found'}")
        if last_word not in word_set or len(word_set[last_word]) < 2:
            return True
        return False