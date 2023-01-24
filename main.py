import sys
import random
from src.entity.entity import Entity
from src.constants.constants import ACTION_DICT, REVERSE_ACTION_DICT, COMPUTER, PLAYER
from src.printers import printers
from src.logger.logger import get_logger

logger = get_logger("my_logger")


def get_computer_action():
    """Get a random action for Computer"""

    return random.randint(0, 2)


def play_game(computer, player):
    """Initiates a game instance between given two entities
    :params: playing entities
    """

    try:
        computer_action = get_computer_action()
        computer.action = computer_action
        player_input = printers.take_player_input()
        logger.info("Player entered: {}".format(player_input))
        if player_input.upper() in ACTION_DICT:
            logger.info("Battling..")
            printers.print_computer_action(REVERSE_ACTION_DICT[computer_action])
            player.action = ACTION_DICT[player_input.upper()]
            player.fight(computer)
            printers.print_points(computer, player)
        elif player_input.upper() == "Q" or player_input.upper() == "QUIT":
            logger.info("Exiting the Game..")
            sys.exit(0)
        else:
            logger.warning("Player entered invalid input")
            print("Please enter valid input - [R]/[P]/[S]")
            play_game(computer, player)

        play_game(computer, player)
    except Exception as e:
        logger.error("Exception occurred: {}".format(e))


def main():
    printers.header()
    while True:
        try:
            key = printers.introduction()
            if key.lower() == 's':
                logger.info("Game has started")
                computer = Entity(COMPUTER)
                player = Entity(PLAYER)
                play_game(computer, player)
            elif key.lower() == 'q':
                logger.info("Exiting the game..")
                sys.exit(0)
            else:
                logger.warning("Player entered invalid input - [S]/[Q]")
                print("Please enter valid input")
        except Exception as e:
            logger.error("Exception occurred: {}".format(e))


if __name__ == "__main__":
    main()
