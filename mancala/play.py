#!/usr/bin/env python3 
from os import sys, path
from mancala import Match, HumanPlayer
from ai_profiles import VectorAI

def main():
    """ Script to begin a match of Mancala. """
    print("Welcome to Mancala!")
    match = Match(player1_type=HumanPlayer, player2_type=VectorAI)
    match.handle_next_move()

if __name__ == "__main__":
    main()
