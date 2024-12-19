class Trie:
    def words_with_prefix(self, prefix):
        words = []
        current = self.root
        for letter in prefix:
            if letter not in current:
                return []
            current = current[letter]
        
        return self.search_level(current, prefix, words)

    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        keys = sorted(cur.keys())
        for key in keys:
            if key != self.end_symbol:
                self.search_level(cur[key], cur_prefix + key, words)
        return words
    
    def add(self, word):
        current = self.root

        for character in word:
            if character not in current:
                current[character] = {}
            current = current[character]
        
        current[self.end_symbol] = True

        return
    
    def exists(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]

        return self.end_symbol in current
    #Improve understanding - O(n * m) Complexity
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches

    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch in variations:            #only added lines 61 + 62 to filter and replace variations
                    ch = variations[ch]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches
    
    #Mostly correct in essence, gaps in logic
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            if len(current) != 1 or self.end_symbol in current:
                break
            for key, child in current.items():
                if key != self.end_symbol:
                    prefix += key
                    current = child
                    break
        return prefix

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"