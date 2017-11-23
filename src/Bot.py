# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from dict import conversations
from utils import speak

class Bot:
    def __init__(self):
        self.bot = ChatBot(
            "Zakas",
            logic_adapters= [
                {'import_path': 'chatterbot.logic.BestMatch'},
                {'import_path': 'chatterbot.logic.TimeLogicAdapter'},
                {'import_path': 'chatterbot.logic.MathematicalEvaluation'},
                {'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                 'threshold': 0.60,
                 'default_response': 'I am sorry, but I do not understand.'}
            ],
            # input_adapter="chatterbot.input.TerminalAdapter",
            # output_adapter="chatterbot.output.TerminalAdapter"
        )

        self.bot.set_trainer(ListTrainer)

        for c in conversations:
            self.bot.train(c)

    def respondTo(self, words):
        response = self.bot.get_response(words)
        speak(str(response))

if __name__ == '__main__':
    b = Bot()
    b.respondTo("How old are you?")
