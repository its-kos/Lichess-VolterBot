import berserk
from gameInst import Game

BASE_URL = "https://lichess.org"
session = berserk.TokenSession(open("token.txt", "r").read())
client = berserk.Client(session)

class Volter():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.active_games = []

    def listenForEvents(self):
        print("Bot is up!")
        for event in client.bots.stream_incoming_events():
            if event['type'] == 'challenge':
                if event['challenge']['variant']['key'] == 'Standard':
                    client.bots.accept_challenge(event['challenge']['id'])
                else:
                    client.bots.decline_challenge(event['challenge']['id'])
            elif event['type'] == 'gameStart':
                self.initGame(client, event)
            elif event['type'] == 'gameFinish':
                pass

    def initGame(self, client, event):
        Game(client, event).run()