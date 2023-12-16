# 2. написати свій генератор. Приймає int (кількість слів) а повертає рандомні слова.
#    Слова мають бути унікальні. Max int = 10_000.


import random
import nltk
from nltk.corpus import words


def word_generator(count):
    if count > 10000:
        print("Error: Max value not more than 10,000")
        return
    word_list = words.words()
    generated_words = set()
    while len(generated_words) < count:
        word = random.choice(word_list).lower()
        if word.isalpha() and word not in generated_words:
            generated_words.add(word)
            yield word


nltk.download('words')
print(len(set(word_generator(9000))))
print(len(list(word_generator(9000))))
print(list(word_generator(100)))