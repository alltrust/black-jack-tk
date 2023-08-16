import random
import tkinter

def deal_card(frame, deck):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    return next_card


def score_hand(hand):
    score = 0
    ace_in_hand = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace_in_hand:
            ace_in_hand = True
            card_value = 11
        score += card_value
        if score > 21 and ace_in_hand:
            score -= 10
            ace_in_hand = False
    return score


def deal_dealer(dealer_score_label, result_text):
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw")


def deal_player(player_score_label, result_text):
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)

    if player_score > 21:
        result_text.set("Dealer wins")

def restart_game(result_text, dealer_score_label):
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    dealer_card_frame.destroy()
    player_card_frame.destroy()

    dealer_card_frame = create_card_frame(0)
    player_card_frame = create_card_frame(2)
 
    result_text.set("")
    
    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
   

def create_card_frame(row:int, card_frame):
    new_card_frame = tkinter.Frame(card_frame, background="green")
    new_card_frame.grid(row=row, column=1, sticky='ew', rowspan=2)
    return new_card_frame

def shuffle(deck):
    random.shuffle(deck)
