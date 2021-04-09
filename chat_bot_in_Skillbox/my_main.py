import random
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

with open(r'chat_bot_in_Skillbox/BIG_BOT_CONFIG.json', 'r', encoding='utf-8') as f:
    BOT_CONFIG = json.load(f)

# with open('/content/test.json', 'w') as f:
#    json.dump({'test': 'value'}, f)

X = []
y = []

for intent, value in BOT_CONFIG['intents'].items():
    if 'inc_examples' in value:
        examples = list(set([example.lower()
                             for example in value['inc_examples']]))
    else:
        examples = list(set([example.lower()
                             for example in value['examples']]))
    X += examples
    y += [intent] * len(examples)

vectorizer = TfidfVectorizer()
X_transformed = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_transformed, y, test_size=0.2, random_state=42)

classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)


def clean(text):
    return ''.join([simbol for simbol in text.lower() if simbol in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '])


def match(example, text):
    return nltk.edit_distance(clean(text), clean(example)) / len(example) < 0.4


def get_intent(text):
    for intent, value in BOT_CONFIG['intents'].items():
        for example in value['examples']:
            if match(example, text):
                return intent


def get_intent_by_ml_model(text):
    return classifier.predict(vectorizer.transform([text]))[0]


question = input()
answer = get_intent(question)
print(answer)

question = ''
while question != 'выход':
    question = input()
    intent = get_intent_by_ml_model(question)

    if 'out_responses' in BOT_CONFIG['intents'][intent]:
        print(random.choice(BOT_CONFIG['intents'][intent]['out_responses']))
    elif 'ersponse' in BOT_CONFIG['intents'][intent]:
        print(random.choice(BOT_CONFIG['intents'][intent]['ersponse']))
    else:
        print(random.choice(BOT_CONFIG['intents'][intent]['responses']))
