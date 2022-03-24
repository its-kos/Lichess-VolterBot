import berserk
from game import Game

BASE_URL = "https://lichess.org"
session = berserk.TokenSession(open("../token.txt", "r").read())
client = berserk.Client(session)

def listenForEvents():
        print("Bot is up!")
        for event in client.bots.stream_incoming_events():
            if event['type'] == 'challenge':
                if event['challenge']['variant']['key'] == 'standard':
                    client.bots.accept_challenge(event['challenge']['id'])
                else:
                    client.bots.decline_challenge(event['challenge']['id'])
            elif event['type'] == 'gameStart':
                print("Before task")
                game = Game(client, event)
                game.start()
            elif event['type'] == 'gameFinish':
                pass

if __name__ == '__main__':
    listenForEvents()

