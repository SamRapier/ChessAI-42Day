# ChessAI-42Day

 Chess game with a AI which is taught through reinforcement learning and self-play

I've decided to make a chess game, which can be played by two people. However, the main aim is to teach an AI to play chess using my implementation. I want to teach the AI using reinforcement learning and self-play; it improves by playing games of chess against itself.

## Current Plan for Game structure

- Written in Python
- Each piece is an object
- Each set is an object
- Positions are held as tuples
- Game shall calculate the legal moves for a board state
- After each move, the game will print the board state and legal moves
- Players have a time limit (currently 2 mins)
- Game has a turn counter (currently 100)

## Current Plan for AI

My current plan, is for each state of the board, we calculate the legal moves for the current player. The board state will be fed into the Neural Network and the legal moves (or actions) will also be provided. Each action will have a reward associated with it (not necessarily a positive reward) and the Neural Network will learn which moves maximise the reward. The Neural networks will play against each other with a time limit and a total number of moves limit. At the end, either by time, move limit or win, the best NN will be chosen to the play again. Some kind of generation must be implemented, I'm not quite sure where this will occur, whether it be when the NN actually plays or at the start of a new game.

## Current Plan for UI

Looking into using Processing for Python to create a UI, still undecided.
