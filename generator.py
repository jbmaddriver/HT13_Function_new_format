# 2. написати свій генератор. Приймає int (кількість слів) а повертає рандомні слова.
#    Слова мають бути унікальні. Max int = 10_000.


from faker import Faker


def word_generator(word_count):
    if word_count > 10000:
        print("Error: Max value not more then 10,000")
        return
    fake = Faker()
    for _ in range(word_count):
        yield fake.word()


random_word_generator = word_generator(5)
print(list(random_word_generator))

