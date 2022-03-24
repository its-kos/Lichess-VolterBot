from cmath import inf
import chess
import threading
import random

finished_states = ['aborted', 'mate', 'resign', 'stalemate', 'timeout', 'draw', 'outoftime', 'unknownFinish']

class Engine(threading.Thread):
    def __init__(self, client, event, **kwargs):
        super().__init__(**kwargs)
        self.game_id = event['game']['gameId']
        self.client = client
        self.stream = client.bots.stream_game_state(event['game']['gameId'])
        self.current_state = next(self.stream)
        self.board = chess.Board()
        self.color = event['game']['isMyTurn']

    def run(self):
        my_move = None
        if self.color:
            my_move = self.minimax(5, inf, -inf)
            self.board.push_san(my_move)
            self.client.bots.make_move(self.game_id, my_move)
        for event in self.stream:
            print(event)
            if event['type'] == 'gameState':
                if event['status'] == 'started':
                    event_move = event['moves'].split(" ")[-1]
                    if event_move != my_move:
                        self.board.push_san(event['moves'].split(" ")[-1])
                        my_move = self.findMove()
                        self.board.push_san(my_move)
                        self.client.bots.make_move(self.game_id, my_move)
                elif event['status'] in finished_states:
                    return
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def minimax(self, depth, alpha, beta):
        if depth == 0 or self.board.is_checkmate():
            return None, self.evaluate()

        moves = list(self.board.legal_moves())
        best_move = random.choice(moves)

        if self.color:
            max_eval = -inf
            for move in moves:
                self.board.push_san(move)
                current_eval = self.minimax(depth - 1, alpha, beta, False)[1]
                self.board.pop()
                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move = move
                alpha = max(alpha, current_eval)
                if beta <= alpha:
                    break
            return best_move, max_eval
        else:
            min_eval = inf
            for move in moves:
                self.board.push_san(move)
                current_eval = self.minimax(depth - 1, alpha, beta, True)[1]
                self.board.pop()
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move = move
                beta = min(beta, current_eval)
                if beta <= alpha:
                    break
            return best_move, max_eval



    def evaluate(self):
        if self.color:
            return self.board.whiteScore - self.board.blackScore
        else:
            return self.board.blackScore - self.board.whiteScore

    def findMove(self):
        move = None
        return move

    def handle_chat_line(self, chat_line):
        pass