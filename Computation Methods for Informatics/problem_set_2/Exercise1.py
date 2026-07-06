from bitarray import bitarray
from hashlib import sha3_256, sha256, blake2b
import string
import json
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

class BloomFilter:
    def __init__(self, size=10000000, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bloom_filter = bitarray(size)
        self.bloom_filter.setall(0)
        self.dictionary_words = set()

    def my_hash(self, s):
        return int(sha256(s.lower().encode()).hexdigest(), 16) % self.size

    def my_hash2(self, s):
        return int(blake2b(s.lower().encode()).hexdigest(), 16) % self.size

    def my_hash3(self, s):
        return int(sha3_256(s.lower().encode()).hexdigest(), 16) % self.size
    
    def add_word(self, s):
        hash = self.my_hash(s)
        self.bloom_filter[hash] = 1

        if self.num_hashes >= 2:
            hash2 = self.my_hash2(s)
            self.bloom_filter[hash2] = 1

        if self.num_hashes == 3:
            hash3 = self.my_hash3(s)
            self.bloom_filter[hash3] = 1
    
    def check_word(self, s):
        hash = self.my_hash(s)
        if not self.bloom_filter[hash]:
            return False

        if self.num_hashes >= 2:
            hash2 = self.my_hash2(s)
            if not self.bloom_filter[hash2]:
                return False

        if self.num_hashes == 3:
            hash3 = self.my_hash3(s)
            if not self.bloom_filter[hash3]:
                return False

        return True
    
    def spell_check(self, s):
        suggestions = []
        alphabet = string.ascii_lowercase
        for i in range(len(s)):
            for letter in alphabet:
                word_suggestion = s[:i] + letter + s[i+1:]
                if(self.check_word(word_suggestion)):
                    suggestions.append(word_suggestion)
        return suggestions
        
    def load_dictionary(self):
        with open('problem_set_2/words.txt') as f:
            for line in f:
                word = line.strip()
                self.add_word(word)
                self.dictionary_words.add(word)
    
    def evaluate_performance(self):
        with open('problem_set_2/typos.json') as f:
            data = json.load(f)

        good_suggestions = 0
        false_positives = 0
        suggestions_count = 0

        for word in data:
            typed_word = word[0]
            correct_word = word[1]
            if typed_word == correct_word:
                continue
            suggestions = self.spell_check(typed_word)
            if correct_word in suggestions and len(suggestions) <= 3:
                good_suggestions += 1
            if self.check_word(typed_word) and typed_word != correct_word:
                false_positives += 1
            suggestions_count += 1

        good_suggestion_percent = good_suggestions/suggestions_count * 100
        print(f'{good_suggestion_percent = }')
        misidentified_percent = false_positives/suggestions_count * 100
        print(f'{misidentified_percent = }')
        return good_suggestion_percent, misidentified_percent

#self-check example
bloom_filter_1e7_1hash = BloomFilter(size=10000000, num_hashes=1)
bloom_filter_1e7_1hash.load_dictionary()
print(f'{bloom_filter_1e7_1hash.check_word("flower") = }')
print(f'{bloom_filter_1e7_1hash.spell_check("floeer") = }')

bloom_filter_1e7_2hash = BloomFilter(size=10000000, num_hashes=2)
bloom_filter_1e7_2hash.load_dictionary()
print(f'{bloom_filter_1e7_2hash.check_word("flower") = }')
print(f'{bloom_filter_1e7_2hash.spell_check("floeer") = }')

bloom_filter_1e7_3hash = BloomFilter(size=10000000, num_hashes=3)
bloom_filter_1e7_3hash.load_dictionary()
print(f'{bloom_filter_1e7_3hash.check_word("flower") = }')
print(f'{bloom_filter_1e7_3hash.spell_check("floeer") = }')

#Q1c ----------------------------------------------------------------------------------------

size_list = [10 ** i for i in range(2, 11)]
num_hashes_options = [1, 2, 3]
results = {}

for num_hashes in num_hashes_options:
    results[num_hashes] = []
    for size in tqdm(size_list):
        bloom_filter = BloomFilter(size=size, num_hashes=num_hashes)
        bloom_filter.load_dictionary()
        good_suggestion_percent, misidentified_percent = bloom_filter.evaluate_performance()
        results[num_hashes].append((good_suggestion_percent, misidentified_percent))

colors = ['b', 'g', 'r', 'c', 'm', 'y']

plt.figure(figsize=(12, 6))
for i, (num_hashes, data) in enumerate(results.items()):
    good_suggestion_percent, misidentified_percent = zip(*data)
    plt.plot(size_list, good_suggestion_percent, label=f'Good Suggestion % {num_hashes} hashes)', color=colors[2 * i])
    plt.plot(size_list, misidentified_percent, label=f'Misidentified % {num_hashes} hashes', color=colors[2 * i + 1])

plt.axhline(y=85, color='black', linestyle='--')
plt.xscale('log')
plt.xlabel('Bits in Bloom Filter')
plt.title('Effect of Filter Size and Number of Hash Functions')
plt.legend()
plt.show()