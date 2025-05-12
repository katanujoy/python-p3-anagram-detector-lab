# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        # Sort the original word's characters
        sorted_word = sorted(self.word)
        
        # Check each word in the possible_anagrams list
        matches = []
        for candidate in possible_anagrams:
            if sorted(candidate) == sorted_word:
                matches.append(candidate)
        
        return matches
