#!/usr/bin/env python3
# This runs the main program.
import blackjack.blackjack as blackjack
import bjp.bjp as bjp
if __name__ == "__main__":
    print("What would you like to play? (blackjack, blackjack-proper)")
    x = input(" >>> ")
    if x == "blackjack":
        print("Starting Blackjack.")
        blackjack.m()
    elif x == "blackjack-proper":
        print("Starting Blackjack-proper")
        bjp.m()

