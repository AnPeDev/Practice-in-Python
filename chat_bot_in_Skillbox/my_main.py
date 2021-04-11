import random
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

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


# question = input()
# answer = get_intent(question)
# print(answer)

# question = ''
# while question != 'выход':
#     question = input()
#     intent = get_intent_by_ml_model(question)

#     if 'out_responses' in BOT_CONFIG['intents'][intent]:
#         print(random.choice(BOT_CONFIG['intents'][intent]['out_responses']))
#     elif 'ersponse' in BOT_CONFIG['intents'][intent]:
#         print(random.choice(BOT_CONFIG['intents'][intent]['ersponse']))
#     else:
#         print(random.choice(BOT_CONFIG['intents'][intent]['responses']))


def bot(question):
    intent = get_intent_by_ml_model(question)
    return random.choice(BOT_CONFIG['intents'][intent]['responses'])


# question = ''
# while question != 'выход':
#     question = input()
#     print(bot(question))


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, _: CallbackContext) -> None:
    """Chat bot ML"""
    question = update.message.text
    reply = bot(question)
    update.message.reply_text(reply)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1717048778:AAH6qaH0CGEfyb9TNoeT0Z9rO-lwFAZsU5w")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


main()
