import random
import nltk

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет!', 'Хай!', 'Добрый день'],
            'resposes': ['Доброго времени суток', 'Прив', 'Хаюхай']
        },
        'bye': {
            'examples': ['Пока', 'До свидания', 'Увидимся'],
            'resposes': ['Счатливо', 'Удачного дня', 'Приходите еще']
        }
    }
}


def clean(text):
    return ''.join([simbol for simbol in text.lower() if simbol in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '])


def match(example, text):
    return nltk.edit_distance(clean(text), clean(example)) / len(example) < 0.4


def get_intent(text):
    for intent, value in BOT_CONFIG['intents'].items():
        for example in value['examples']:
            if match(example, text):
                return random.choice(value['resposes'])
    return 'Я ничего не понял'


question = input()
answer = get_intent(question)
print(answer)

while question != 'выход':
    question = input()
    answer = get_intent(question)
    print(answer)
