#!/usr/bin/env python3


def main():
    round = 0
    answer = " "
    while round<3 and answer != "brian":
        round += 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ..."')
        if answer.lower() == 'brian':
            print("Correct")
            break
        elif round == 3:
            print("Sorry, the answerwas Brian.")
            break
        else:
            print("Sorry!, Try again!")

main()

