# Blackjack
# From 1 to 7 players compete against a dealer

import cards
import games


class BjCard(cards.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BjCard.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BjDeck(cards.Deck):
    """ A Blackjack Deck. """

    def populate(self):
        for suit in BjCard.SUITS:
            for rank in BjCard.RANKS:
                self.cards.append(BjCard(rank, suit))


class BjHand(cards.Hand):
    """ A Blackjack Hand. """

    def __init__(self, name, money=0):
        super(BjHand, self).__init__()
        self.name = name
        self.money = money

    def __str__(self):
        rep = self.name + ":\t" + super(BjHand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None

        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BjCard.ACE_VALUE:
                contains_ace = True

        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


class BjBank:
    def __init__(self):
        self.total = 0

    def in_bank(self):
        print('Total cache in bank = '+str(self.total))


class BjPlayer(BjHand):
    """ A Blackjack Player. """

    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def push(self):
        print(self.name, "pushes.")

    def bet(self, bet_value, bank):
        self.money -= bet_value
        bank.total += bet_value
        # print("I bet", bet_value, '!')


class BjDealer(BjHand):
    """ A Blackjack Dealer. """

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BjGame(object):
    """ A Blackjack Game. """

    def __init__(self, names):
        self.players = []
        for name in names:
            player = BjPlayer(name)
            self.players.append(player)
            player.money += 1000

        self.dealer = BjDealer("Dealer")
        self.bank = BjBank()
        self.deck = BjDeck()
        self.deck.populate()
        self.deck.shuffle()

        self.winners=0

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):

        for player in self.players:
            bet_value = games.ask_number(player.name + ', сколько хотите поставить? $', 0, player.money)
            player.bet(bet_value, self.bank)
        self.bank.in_bank()
        print('\n')

        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()  # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()  # reveal dealer's first

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                        self.winners+=1
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # remove everyone's cards
        for player in self.players:
            player.clear()
            self.winners=0
        self.dealer.clear()


def main():
    print("\t\tWelcome to Blackjack!\n")

    names = []
    number = games.ask_number("How many players? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()

    game = BjGame(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nPress the enter key to exit.")
