from genericpath import exists
import random
from telnetlib import WONT
from colorama import Fore, Style


def tic_tac_toe():
    global playing
    global go_again
    global won
    won = False
    playing = False
    go_again = False
    turn_count = 0

    pos1 = [1]
    pos2 = [2]
    pos3 = [3]
    pos4 = [4]
    pos5 = [5]
    pos6 = [6]
    pos7 = [7]
    pos8 = [8]
    pos9 = [9]

    selection = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    rules_or_play = input(
        "\nWelcome to tic-tac-toe! "
        "Type rules for how to play "
        "or play to start playing.\n\n"
    )

    if rules_or_play == "rules":
        print(
            "\nYou play as o's and the computer plays as x's, "
            "to win you need to create a line of 3 o's either vertically, "
            "horizontally, or diagonally. The computer wins if it scores "
            "3  x's in a row and it is a tie if all squares are taken up "
            "with no winners.\n"
        )

        read_rules_play = input("Would you like to play? (y/n)\n\n")

        if read_rules_play in ("Yes", "yes", "y", "Y", "ok", "OK"):
            playing = True
        else:
            exit

    elif rules_or_play == "play":
        playing = True

    else:
        print("\nSorry I do not understand")
        tic_tac_toe()

    if playing == True:
        print(
            "You go first! Here is the grid:\n\n"
            " 1 | 2 | 3 \n"
            "---+---+---\n"
            " 4 | 5 | 6 \n"
            "---+---+---\n"
            " 7 | 8 | 9 \n\n"
        )

        def user_turn():

            global go_again

            match user_choice:
                case "1":
                    if pos1[0] != "o" and pos1[0] != "x":
                        pos1.clear()
                        pos1.append("o")
                        selection.remove(1)
                        go_again = False
                    else:
                        print(Fore.RED + "\nThat position is already taken!")
                        go_again = True
                case "2":
                    if pos2[0] != "o" and pos2[0] != "x":
                        pos2.clear()
                        pos2.append("o")
                        selection.remove(2)
                        go_again = False
                    else:
                        print(Fore.RED + "\nThat position is already taken!")
                        go_again = True
                case "3":
                    if pos3[0] != "o" and pos3[0] != "x":
                        pos3.clear()
                        pos3.append("o")
                        selection.remove(3)
                        go_again = False
                    else:
                        print(Fore.RED + "\nThat position is already taken!")
                        go_again = True
                case "4":
                    if pos4[0] != "o" and pos4[0] != "x":
                        pos4.clear()
                        pos4.append("o")
                        selection.remove(4)
                        go_again = False
                    else:
                        print(Fore.RED + "\nThat position is already taken!")
                        go_again = True
                case "5":
                    if pos5[0] != "o" and pos5[0] != "x":
                        pos5.clear()
                        pos5.append("o")
                        selection.remove(5)
                        go_again = False
                    else:
                        print(Fore.RED + "\nThat position is already taken!")
                        go_again = True
                case "6":
                    if pos6[0] != "o" and pos6[0] != "x":
                        pos6.clear()
                        pos6.append("o")
                        selection.remove(6)
                        go_again = False
                    else:
                        print(Fore.RED + "\nThat position is already taken!")
                        go_again = True
                case "7":
                    if pos7[0] != "o" and pos7[0] != "x":
                        pos7.clear()
                        pos7.append("o")
                        selection.remove(7)
                        go_again = False
                    else:
                        print(Fore.RED + "\nThat position is already taken!")
                        go_again = True
                case "8":
                    if pos8[0] != "o" and pos8[0] != "x":
                        pos8.clear()
                        pos8.append("o")
                        selection.remove(8)
                        go_again = False
                    else:
                        print(Fore.RED + "\nThat position is already taken!")
                        go_again = True
                case "9":
                    if pos9[0] != "o" and pos9[0] != "x":
                        pos9.clear()
                        pos9.append("o")
                        selection.remove(9)
                        go_again = False
                    else:
                        print(Fore.RED + "\nThat position is already taken!")
                        go_again = True
                case _:
                    print(Fore.RED + "\nSorry that was not a valid value.")
                    go_again = True

            print(Style.RESET_ALL)

            print(
                "\n"
                "Your move:\n"
                f" {pos1[0]} | {pos2[0]} | {pos3[0]} \n"
                "---+---+---\n"
                f" {pos4[0]} | {pos5[0]} | {pos6[0]} \n"
                "---+---+---\n"
                f" {pos7[0]} | {pos8[0]} | {pos9[0]} \n"
            )

        def computer_turn():

            computer_choice = random.choice(selection)

            match str(computer_choice):
                case "1":
                    pos1.clear()
                    pos1.append("x")
                    selection.remove(1)
                case "2":
                    pos2.clear()
                    pos2.append("x")
                    selection.remove(2)
                case "3":
                    pos3.clear()
                    pos3.append("x")
                    selection.remove(3)
                case "4":
                    pos4.clear()
                    pos4.append("x")
                    selection.remove(4)
                case "5":
                    pos5.clear()
                    pos5.append("x")
                    selection.remove(5)
                case "6":
                    pos6.clear()
                    pos6.append("x")
                    selection.remove(6)
                case "7":
                    pos7.clear()
                    pos7.append("x")
                    selection.remove(7)
                case "8":
                    pos8.clear()
                    pos8.append("x")
                    selection.remove(8)
                case "9":
                    pos9.clear()
                    pos9.append("x")
                    selection.remove(9)

            print(
                "\n"
                "Computer move:\n"
                f" {pos1[0]} | {pos2[0]} | {pos3[0]} \n"
                "---+---+---\n"
                f" {pos4[0]} | {pos5[0]} | {pos6[0]} \n"
                "---+---+---\n"
                f" {pos7[0]} | {pos8[0]} | {pos9[0]} \n"
            )

        def winner():

            global won

            if (
                pos1[0] == pos2[0] == pos3[0] == "o"
                or pos4[0] == pos5[0] == pos6[0] == "o"
                or pos7[0] == pos8[0] == pos9[0] == "o"
                or pos1[0] == pos4[0] == pos7[0] == "o"
                or pos2[0] == pos5[0] == pos8[0] == "o"
                or pos3[0] == pos6[0] == pos9[0] == "o"
                or pos1[0] == pos5[0] == pos9[0] == "o"
                or pos3[0] == pos5[0] == pos7[0] == "o"
            ):

                print("Congratulations, you win!\n")
                playing = False
                won = True

            elif (
                pos1[0] == pos2[0] == pos3[0] == "x"
                or pos4[0] == pos5[0] == pos6[0] == "x"
                or pos7[0] == pos8[0] == pos9[0] == "x"
                or pos1[0] == pos4[0] == pos7[0] == "x"
                or pos2[0] == pos5[0] == pos8[0] == "x"
                or pos3[0] == pos6[0] == pos9[0] == "x"
                or pos1[0] == pos5[0] == pos9[0] == "x"
                or pos3[0] == pos5[0] == pos7[0] == "x"
            ):
                print("Unfortunately you lose.\n")
                playing = False
                won = True

            elif turn_count >= 8:
                print("It is a tie.\n")
                playing = False
                won = True

    while playing:

        user_choice = input("Where would you like to put your piece? ")
        user_turn()

        while go_again == True:
            user_choice = input("Where would you like to put your piece? ")
            user_turn()

        winner()
        turn_count += 1

        if won == True:
            playing = False
            close = input("Press any key to close the application ")
            break

        computer_turn()
        winner()
        turn_count += 1

        if won == True:
            playing = False
            close = input("Press any key to close the application ")
            break


tic_tac_toe()
