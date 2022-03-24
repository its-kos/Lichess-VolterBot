# Volter Bot

Welcome to Volter bot. A simple chess bot for the [Lichess](https://lichess.org/) website. 

## Description

Using the [API](https://lichess.org/api) provided by Lichess, this bot can accept and play multiple challenges (chess matches). For now the moves are random but adding logic and training the bot are in the works so stay tuned... 

## Getting Started

### Dependencies for using the bot

* Python 3
* A lichess account that you need to upgrade to a BOT status. Find instrucions [here](https://lichess.org/api#operation/botAccountUpgrade)
* Your (secret) API token from Lichess. Generate one [here](https://lichess.org/account/oauth/token) (You need to be logged in using your BOT account)

### Setup

**(Using Anaconda and environments is highly recommended)**

* (Optional but recommended) Create an environment for the project and navigate to that folder
* Use ```pip install -r requirements.tx``` to get all required modules
* Create a *"token.txt"* file and paste your Lichess API token there

### Executing program

* Run ```python main.py``` and your bot should be up and running.

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info:

So far just me :)
[@its-kos](https://github.com/its-kos)

## Version History

* 0.1
    * Initial Commit
    * Basic functionality
    * Can accept and play multiple chess matches
    * Can only play random moves

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE.md file for details

## Acknowledgments

For more information have a look here:
* [Berserk](https://github.com/rhgrant10/berserk)
* [API](https://lichess.org/api)
