import random
import tkinter
from load_images import load_images


def _deal_card(frame):
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


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
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


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)

    if player_score > 21:
        result_text.set("Dealer wins")

def intiial_deal():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

def restart_game():
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

    intiial_deal()


def create_card_frame(row: int):
    new_card_frame = tkinter.Frame(card_frame, background="green")
    new_card_frame.grid(row=row, column=1, sticky='ew', rowspan=2)
    return new_card_frame


def shuffle():
    random.shuffle(deck)


def play():
    intiial_deal()
    mainWindow.mainloop()


# check if this is the modue that is running

mainWindow = tkinter.Tk()

# screen and frames setup for dealer and player
mainWindow.title("Blackjack")
mainWindow.geometry("640x480")
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken',
                           borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green",
              fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label,
              background="green", fg="white").grid(row=1, column=0)

# embedded frame to hold card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()


tkinter.Label(card_frame, text="Player", background='green',
              fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label,
              background="green", fg="white").grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(
    button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(
    button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_btn = tkinter.Button(
    button_frame, text="New Game", command=restart_game)
new_game_btn.grid(row=0, column=2)

shuffle_btn = tkinter.Button(button_frame, text="Shuffle", command="shuffle")
shuffle_btn.grid(row=0, column=3)


cards = []
load_images(cards)

deck = list(cards)

shuffle()

dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()


