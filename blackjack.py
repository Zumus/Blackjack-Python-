import random


deck = {"1H": 1, "2H": 2, "3H": 3, "4H": 4, "5H": 5, "6H": 6, "7H": 7, "8H": 8, "9H": 9, "10H": 10, "JH": 10, "QH": 10, "KH": 10, "AH": 11,
        "1D": 1, "2D": 2, "3D": 3, "4D": 4, "5D": 5, "6D": 6, "7D": 7, "8D": 8, "9D": 9, "10D": 10, "JD": 10, "QD": 10, "KD": 10, "AD": 11,
        "1S": 1, "2S": 2, "3S": 3, "4S": 4, "5S": 5, "6S": 6, "7S": 7, "8S": 8, "9S": 9, "10S": 10, "JS": 10, "QS": 10, "KS": 10, "AS": 11,
        "1C": 1, "2C": 2, "3C": 3, "4C": 4, "5C": 5, "6C": 6, "7C": 7, "8C": 8, "9C": 9, "10C": 10, "JC": 10, "QC": 10, "KC": 10, "AC": 11}


def deal_card(hand):
    x = random.sample(deck.keys(), 1)
    x = x[0]
    y = deck[x] 
    hand.update({x:y})

def check_game_over(player_hand, computer_hand): #working
    global done
    global player_score
    global computer_score
    if player_score == 21 and computer_score < 21:
        print("Blackjack! Player wins!")
        return True
        end()
    elif player_score < 21 and computer_score == 21:
        print("Blackjack! Computer wins!")
        return True
        end()
    elif player_score == 21 and computer_score == 21:
        print("Double Blackjack! Tie.")
        return True
    elif player_score > 21 and computer_score < 21:
        print("Player broke 21. Computer wins!")
        return True
        end()
    elif player_score < 21 and computer_score > 21:
        print("Computer broke 21. Player wins!")
        return True
        end()
    else:
    	done = False 
    	return False

def ask(): #working
    global player_score
    done = False
    print("Your hand:", player_hand)
    choice = input("Would you like another card? (y/n)")
    if choice in ["y", "yes", "Y", "Yes", "YES"]:
        deal_card(player_hand)
        player_score = 0
        for key in player_hand:
            player_score = player_score + player_hand[key]
        check_game_over(player_hand, computer_hand)
        if True:
            end()
        if False:
            ask()
    if choice in ["n", "no", "N", "No", "NO"]: #PROBLEM AREA
        computer_play()
        check_game_over(player_hand, computer_hand)
        if done == True:
            end()
        if done == False:
            end()


def main():
    global player_score
    player_score = 0
    global computer_score
    computer_score = 0

    #initializing hands----------------
    global player_hand
    player_hand = dict(random.sample(deck.items(), 2))
    global computer_hand
    computer_hand = dict(random.sample(deck.items(), 2)) 

    if player_score == 0:
        for key in player_hand:
            player_score = player_score + player_hand[key]
    if computer_score == 0:
        for key in computer_hand:
            computer_score = computer_score + computer_hand[key]

    #-----------------------------------

    check_game_over(player_hand, computer_hand)
    ask()

#need function for computer actions after player stops taking cards
def computer_play():
    while computer_score < 16:
        deal_card(computer_hand)
        check_game_over(player_hand, computer_hand)
    end()

def end():
    print("Final Score:")
    print("Player:", player_score)
    print("Computer:", computer_score)
    quit()

    
main()