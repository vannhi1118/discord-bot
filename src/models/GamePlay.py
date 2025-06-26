from constants import ErrorCode
import os

# __file__ is the path to the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../data/Viet74K.txt")

# Load once at startup
word_set = {}
raw_set = set()
with open(file_path, encoding="utf-8") as f:
    raw_set = set(line.strip().lower() for line in f if line.strip())
    for word in raw_set:
        split_word = word.split()
        if len(split_word) < 2:
            word_set[word] = {s for s in raw_set if s.split()[0] == word and len(s.split()) == 2}

class GamePlay:
    def __init__(self):
        self.last_word = None
        self.last_user = None
        self.words_used = set()

    def __repr__(self):
        return f"GamePlay(last_word={self.last_word}, last_user={self.last_user}, words_used={self.words_used})"
    
    def add_word(self, composite_word, user):
        print(f"Checking composite word: {composite_word} by {user}")
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
        print(f"Checking endgame for last_word: {last_word}")
        if last_word not in word_set or len(word_set[last_word]) < 2 or self.words_used >= word_set[last_word]:
            return True
        print("Game is still ongoing")
        return False
    
    def get_hint(self, keyword):
        """Get a hint for a keyword."""
        print(f"Finding hints for last_word: {keyword}")
        if keyword in word_set:
            print(f"All possible options for {keyword}: {word_set[keyword]}")
            first_match = next((word for word in word_set[keyword] if word not in self.words_used), None)
            return first_match