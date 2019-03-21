import math,string,itertools,fractions,heapq,collections,re,array,bisect,random # noqa


class BlackjackWinner:

    BLACKJACK_MULTIPLIER = 1.5

    def winnings(self, bet, dealer, dealer_blackjack, player, player_blackjack): # noqa

        if dealer > player:
            if dealer > 21 and player <= 21 and player_blackjack:
                return bet * self.BLACKJACK_MULTIPLIER
            if dealer > 21 and player <= 21:
                return bet
            elif dealer > 21 and player > 21:
                return -bet
            elif dealer <= 21:
                return -bet
        elif player > dealer:
            if player > 21 and dealer <= 21:
                return -bet
            elif player > 21 and dealer > 21:
                return -bet
            elif player < 21 and player_blackjack:
                return bet * self.BLACKJACK_MULTIPLIER
            else:
                return bet
        elif player == dealer:
            if dealer_blackjack:
                return -bet
            elif player_blackjack:
                return bet * self.BLACKJACK_MULTIPLIER
            else:
                return -bet



#Powered by KawigiEdit-pf 2.3.0!
