import threading
import berserk
import chess
import random

BASE_URL = "https://lichess.org"

## Make sure to create a "token.txt" file in the same directory as this script and paste the your Lichess API token there ##
session = berserk.TokenSession(open("token.txt", "r").read())
client = berserk.Client(session)

class Game(threading.Thread):
    def __init__(self, client, event, **kwargs):
        super().__init__(**kwargs)
        self.game_id = event['game']['gameId']
        self.client = client
        self.stream = client.bots.stream_game_state(event['game']['gameId'])
        self.current_state = next(self.stream)
        self.board = chess.Board()
        self.turn = event['game']['isMyTurn']

    def run(self):
        my_move = None
        if self.turn:
            my_move = str(random.choice(list(self.board.legal_moves)))
            self.make_move(my_move)
        for event in self.stream:
            print(event)
            if event['type'] == 'gameState':
                if event['status'] == 'started':
                    event_move = event['moves'].split(" ")[-1]
                    if event_move != my_move:
                        self.board.push_san(event['moves'].split(" ")[-1])
                        my_move = str(random.choice(list(self.board.legal_moves)))
                        self.make_move(my_move)
                elif event['status'] == 'mate':
                    pass
                elif event['status'] == '':
                    pass
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def make_move(self, move):
        self.board.push_san(move)
        client.bots.make_move(self.game_id, move)

    def handle_chat_line(self, chat_line):
        pass

def listenForEvents():
    for event in client.bots.stream_incoming_events():
        if event['type'] == 'challenge':
            client.bots.accept_challenge(event['challenge']['id'])
        elif event['type'] == 'gameStart':
            game = Game(client, event)
            game.run()
        elif event['type'] == 'gameFinish':
            game = Game(client, event)
            game.run()

if __name__ == '__main__':
    print("Bot is up!")
    listenForEvents()

