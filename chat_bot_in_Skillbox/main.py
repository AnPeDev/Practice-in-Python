import random
import nltk

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет!', 'Хай!', 'Добрый день'],
            'responses': ['Доброго времени суток', 'Прив', 'Хаюхай']
        },
        'bye': {
            'examples': ['Пока', 'До свидания', 'Увидимся'],
            'responses': ['Счатливо', 'Удачного дня', 'Приходите еще']
        },
        'how_are_you': {
            'examples': ['Как дела?', 'Как поживаешь?', 'Все норм?'],
            'responses': ['Все ОК', 'Хорошо', 'Супер']
        },
        'what_are_you_doing': {
            'examples': ['Чем занимаешься?', 'Что делаешь?', 'Чем занят?'],
            'responses': ['С тобой разговариваю', 'Высчитываю алгоритмы', 'Читаю двоичный код']
        },
        'what_plans': {
            'examples': ['Какие планы?', 'Какие планы на сегодня?', 'Какие планы на завтра?'],
            'responses': ['Общаться с тобой', 'Пойти погулять с тобой', 'Общаться с Алисой и Олегом']
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
                return random.choice(value['responses'])
    return 'Я ничего не понял'


question = input('Поздаровайтесь и начните общение: \n')
answer = get_intent(question)
print(answer)

while question != 'выход':
    question = input()
    answer = get_intent(question)
    print(answer)
