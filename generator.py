# 2. написати свій генератор. Приймає int (кількість слів) а повертає рандомні слова.
#    Слова мають бути унікальні. Max int = 10_000.

from faker import Faker


def word_generator(word_count):
    if word_count > 10000:
        print("Error: Max value not more than 10,000")
        return
    fake = Faker()
    generated_words = set()

    while len(generated_words) < word_count:
        word = fake.word()
        if word not in generated_words:
            generated_words.add(word)
            yield word


print(len(set(word_generator(500))))
print(len(list(word_generator(500))))

