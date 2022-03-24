import chess
import threading
import random

finished_states = ['aborted', 'mate', 'resign', 'stalemate', 'timeout', 'draw', 'outoftime', 'unknownFinish']

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
                elif event['status'] in finished_states:
                    return
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def make_move(self, move):
        self.board.push_san(move)
        self.client.bots.make_move(self.game_id, move)

    def handle_chat_line(self, chat_line):
        pass