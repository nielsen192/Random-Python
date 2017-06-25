from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    'Siraj',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    ouput_adapter='chatterbot.ouput.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    database='./database.json'
)

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")

print('Type something to begin...')

while True:
    try:
        bot_input = bot.get_response(None)
        print(bot_input)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


