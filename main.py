#!/usr/bin/env python3
# This runs the main program.
import blackjack
if __name__ == "__main__":
    print("What would you like to play? (blackjack, )")
    x = input(" >>> ")
    if x == "blackjack":
        print("Starting Blackjack.")
        blackjack.m()

