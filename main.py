from email import header
import requests

BASE_URL = "https://lichess.org"

def init():
    print("Bot is up!")
    token = open("token.txt", "r").read()
    listenForChallenges(token)


def listenForChallenges(token):
    r = requests.get(BASE_URL + '/api/stream/event', headers={"Authorization": f'Bearer {token}'})
    print(r.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()

