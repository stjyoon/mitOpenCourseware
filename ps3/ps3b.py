from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    perms = get_perms(hand, HAND_SIZE)
    bestperm = perms[1]
    for i in range(0,len(perms)):
        if perms[i] in word_list:
            get_word_score(perms[i], HAND_SIZE)


#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...    
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    global newhand
    print('enter "n" for new hand, "r" to replay last hand, or "e", to exit')
    print('enter option:')
    choice = input()
    options = ['n','r','e']
    global counter
    while choice not in options:
        print('invalid option, try again')
        choice = input()
    while choice == 'r' and counter == 0:
        print('no previous hand available, enter "n" for new hand or "e" to exit')
        choice = input()
    if choice == 'n':
        print('enter "u" to play as user or "c" to allow computer to pick word')
        uc_choice = input()
        while uc_choice != "u" or "c":
            print('invalid choice, enter "u" to play as user or "c" to allow computer to choose word')
        if counter == 0:
            counter += 1
            if uc_choice == "u":
                play_hand(newhand,word_list)
            else:
                comp_play_hand(newhand, word_list)
        else:
            newhand = deal_hand(HAND_SIZE)
            if uc_choice == "u":
                play_hand(newhand,word_list)
            else:
                comp_play_hand(newhand,word_list)
    if choice == 'r' and counter > 0:
        play_hand(newhand,word_list)
    if choice == 'e':
        exit()



        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':

    word_list = load_words()
    play_game(word_list)

    
