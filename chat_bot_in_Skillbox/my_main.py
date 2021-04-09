# import random

# Намерения (Поздороваться или попрощаться)
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

# Перебрать библиотеку BOT_CONFIG:


def get_intent(text):
    for intent, value in BOT_CONFIG['intents'].items():
        print(intent)
        for example in value['examples']:
            print(example)
        print('-----------')
        for response in value['responses']:
            print(response)
        print('-----------')


get_intent('')
