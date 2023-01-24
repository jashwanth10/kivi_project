def introduction():
    return input("Enter (S)tart / (Q)uit:")


def take_player_input():
    print("Please enter your input!" + print_prompt())
    return input("Enter (R)ock / (P)aper / (S)cissor:")


def print_computer_action(action):
    print("#####################")
    print("Computer chose: {}".format(action))
    print("#####################")


def header():
    print("-----------------------------------")
    print("Welcome to Rock-Paper-Scissor game!")
    print("-----------------------------------")


def print_prompt():
    return "\t\t\t\t\tPress (Q)uit to quit the game"


def print_points(computer, player):
    print("######################################")
    print("Scoreboard: Computer - {}, Player - {}".format(computer.points, player.points))
    print("######################################")
