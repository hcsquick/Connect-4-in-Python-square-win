#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:04:42 2022

@author: Henrique Quick
"""
import copy


def add_coin(board, coin, column):
    """
    Udates the state of the game after a move has been made and returns a new board.
    Aceppts as parameters a nested list representing the current state of the board, an string representing
    the player's coin and an interger representing the column in which the player is droppoing the coin.
   
    """
    
    pos = None # Position variable with a inicial value defined to avoid many conditionals.
    for index_value, value in enumerate(board):
        # loop with enumerate metothod to return the index and value of the coin.
        
        if board[index_value][column] == 0:
            # Verify if line and column are empty.
            # If it is true add position to the variable.
            pos = index_value
            #check availability of the position.
            
    new_board = copy.deepcopy(board)
    
    if pos is not None:
        # If pos is not empty coin drops in the next line available.
        new_board[pos][column] = coin
        
    # Return new_board updated.
    return new_board

def is_winner(board, coin):
    """
    Determines if player is the winner verifying the if the position of the coins is a square and returns True
    or False otherwise.
    Accepts as arguments the current state of the board as a nested list and coin as a string.
    
    """
    
    SQUARE_WIN = 4 # Validating a the number of coin with the sema value in a square for a win.
    len_board_height = len(board) - 1 # Validating players movement given length of the board.
    len_board_weight = len(board[0]) - 1 # Defining length of the rolls.
    
    # Iterating between rolls of the board where x = sublist and index_x = index of the sublist.
    for index_x, x in enumerate(board):
        # Iterating on the position of the coin given a roll.
        
        for index_y, y in enumerate(x):
            # To guarantee that the player's movement is valid for the given board.
            
            if index_x < len_board_height and index_y < len_board_weight:
                # Checking current state of the board in order to compare a square win. 
                verify_board = [
                    board[index_x][index_y], board[index_x + 1][index_y],
                    board[index_x][index_y + 1], board[index_x + 1][index_y + 1]
                    ]
                # Checking winner board
                if verify_board.count(coin) == SQUARE_WIN:
                    return True
    return False

def heuristic(board, coin):
    """
    Loops through the board and calculates the heuristic value of
    each movement possible for the round and return this value.
    
    """
    
    len_board_height = len(board) - 1 # Defining the hight of the columns.
    len_board_weight = len(board[0]) - 1 # Defining length of the rolls.
    
    reverse_coin = 'Y' if coin == 'R' else 'R'
    
    total_heuristic = 0
    
    # Reversing board to access the lists which contain player's movements.
    for index_x, x in reversed(list(enumerate(board))):
        
        for index_y, y in enumerate(x):
            # Checking current state of the board.
            if index_x < len_board_height and index_y < len_board_weight:
                verify_board = [
                    [board[index_x][index_y], board[index_x + 1][index_y]],
                    [board[index_x][index_y + 1], board[index_x + 1][index_y + 1]]
                    ]
               
                # Checking if there's an opponent's coin on the board.
                if verify_board[0][0] == reverse_coin or verify_board[1][0] == reverse_coin or verify_board[0][1] == reverse_coin or verify_board[1][1] == reverse_coin:
                    total_heuristic += 0
                    
                else:
                    # Checking AI coin and adding.
                    coins = 0
                    
                    for index_verify_x, verify_x in enumerate(verify_board):
                        
                        for index_verify_y, verify_y in enumerate(verify_x):
                            
                            if verify_board[index_verify_x][index_verify_y] == coin:
                                if coins == 0:
                                    coins = 1
                                else:
                                    coins *= 10
                   
                    total_heuristic += coins
            
    return total_heuristic

def ai_move(board, coin):
    """
    Generetes a list of all possible moves from the current board and
    returns the board with the highest heuristic value associated

    """
    
    best_board = None # Set a inicial value for the best board in order to compare. 
    best_heuristic = -1 # Set a inicial value for the best heuristic in order to compere.
    
    # Loop through a deep copy of the original board.
    for column in range(len(board[0])):
        
        new_board = add_coin(board, coin, column)
        heur_new_board = heuristic(new_board, coin)
        
        if heur_new_board > best_heuristic:
            
            best_board = new_board
            best_heuristic = heur_new_board
            
    return best_board

def moves_exist(board):
    """
    A move can still be made if any blank space exists on the top row.

    """
    if 0 in board[0]:
        return True
    return False

def nice_print(board):
    """
    Formats the board for nicer display.

    """
    
    for line in board:
        print(*line)
    
def play_game(rows, cols):
    """
    Plays a game with a human player against your AI.
    
    """
    # Instantiate an empty board.
    board = [([0]*cols) for i in range(rows)]
    
    # Continue playing as long as a legal move can still be made.
    while(moves_exist(board)):
        
        # AI plays first with the red tokens.
        board = ai_move(board, 'R')
        nice_print(board)
        
        # Check if the AI Player has won the game.
        if (is_winner(board, 'R')):
            print('AI Wins!')
            break
    
        # Player moves next with the yellow tokens.
        player_move = input('Enter your move: ')
        board = add_coin(board, 'Y', int(player_move))
       
        if (is_winner(board, 'Y')):
            print('You win!')
            break
    
                
                

   