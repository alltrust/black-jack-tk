import tkinter

def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for suit in suits:
        for card_num in range(1, 11):
            name = 'blackjack/cards/{}_{}.{}'.format(str(card_num), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card_num, image,))

        for card in face_cards:
            name = 'blackjack/cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))
