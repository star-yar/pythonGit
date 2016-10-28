# игра война

import cards, games


#class W_Card(cards.Card):
#    numeral_rank = [11, 2, 3, 4, 5, 6, 7,
#                    8, 9, 10, 10, 10, 10]


class W_Deck(cards.Deck):
    pass


class W_Hand(cards.Hand):
    def __str__(self):
        rep = ''
        for card in self.cards:
            rep += str(card)
        return rep


class W_Player(object):
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
        self.hand=cards.Hand()

    @property
    def count_strength(self):
        RANKS = cards.Card.RANKS
        card_rank = (str(self.hand.cards[0]))[0:-1]
        strength = int(RANKS.index(card_rank))+1
        if strength == 1:
            strength=14
        return strength



class W_Game(object):
    '''a War Game.'''
    def __init__(self, names):
        self.players = []

        for name in names:
            player = W_Player(name)
            self.players.append(player)

        self.deck=W_Deck()

        self.deck.populate()
        self.deck.shuffle()

    def give_everyone_card(self, cards_to_deal=1):
        print('Раздаю карты...')
        for player in self.players:
            self.deck.deal([player.hand])

    def everyone_shows_card(self):
        for player in self.players:
            print(player.name, ': ', player.hand)
        print('\n')

    def choose_the_winner(self):
        strength_pool=[]
        for player in self.players:
            strength_pool.append(player.count_strength)
            max_strength=max(strength_pool)
        number_of_the_winner = strength_pool.index(max_strength)

        #returns name and pos in 'players' of the winner
        return number_of_the_winner, self.players[number_of_the_winner].name

def main(names=[]):
    #Main module of the game

    #creating players
    if not names:
        for new_player in range(1, (games.ask_number('Сколько человек играет? (2-999): ', 2,999)+1)):
            print('Игрок №', new_player,', ', end=' ')
            names.append(input('Введите имя '))
            game=W_Game(names)
    else:
        game = W_Game(names)

    #game starts
    print('\nLet the WAR begin!!!\n')
    #input('Press Enter to enjoy...')
    game.give_everyone_card()

    input('Ready for results?')
    game.everyone_shows_card()

    #Showing results
    print('Победу одерживает Игрок №', game.choose_the_winner()[0]+1, ' - ', game.choose_the_winner()[1])
    print('\n\nНажмите Enter чтобы выйти...')
    input()
    return('processing..')

main()