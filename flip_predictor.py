from __future__ import division
from numpy import array, append, prod


class FlipPredictor(object):
    '''
    the FlipPredictor is initialized with a bag of coins that have varying probabilities of
    landing on heads. assuming a coin is selected at random and flipped repeatedly,
    the FlipPredictor will update the probability of each coin in its bag being the selected coin.

    challenge prompt:
    https://classroom.udacity.com/courses/st101/lessons/48452978/concepts/484806060923#
    '''
    def __init__(self, coins):
        self.p_coins_heads = array(coins)
        n = len(self.p_coins_heads)
        self.p_coins_selected = array([1/n] * n)

    def update(self, result):
        '''
        updates the probabilities of each coin being the selected coin,
        given a new flip result, either 'H' or 'T'.

        using bayes theorem, the new probability that a coin is the selected coin
        is determined by multiplying the probability of the result occurring
        given the coin was selected with the probability that coin was selected.
        this product is then divided by the probability of the result occurring across all coins.

        bayes theorem says:
        P(coin selected | result) = (P(result | coin selected) * P(coin selected)) / P(result)

        this function replaces the stats nomenclature with the following variables:
        new_p_coin_selected = (p_result_given_coin * p_coin_selected) / p_result
        '''
        p_result_given_coins = array([])

        for i in xrange(len(self.p_coins_heads)):
            p_heads = self.p_coins_heads[i]
            p_result_given_coin = p_heads if result == 'H' else 1 - p_heads
            p_result_given_coins = append(p_result_given_coins, p_result_given_coin)

        p_result = sum(p_result_given_coins * self.p_coins_selected)

        for i in xrange(len(self.p_coins_heads)):
            p_coin_selected = self.p_coins_selected[i]
            p_result_given_coin = p_result_given_coins[i]
            new_p_coin_selected = (p_result_given_coin * p_coin_selected) / p_result
            self.p_coins_selected[i] = new_p_coin_selected

    def pheads(self):
        '''
        returns the probability of the next flip being heads
        '''
        return sum(self.p_coins_heads * self.p_coins_selected)


# test code from challenge prompt:
# https://classroom.udacity.com/courses/st101/lessons/48452978/concepts/484806060923#
def test(coins,flips):
    f=FlipPredictor(coins)
    guesses=[]
    for flip in flips:
        f.update(flip)
        guesses.append(f.pheads())
    return guesses

def maxdiff(l1,l2):
    return max([abs(x-y) for x,y in zip(l1,l2)])

testcases=[
(([0.5,0.4,0.3],'HHTH'),[0.4166666666666667, 0.432, 0.42183098591549295, 0.43639398998330553]),
(([0.14,0.32,0.42,0.81,0.21],'HHHTTTHHH'),[0.5255789473684211, 0.6512136991788505, 0.7295055220497553, 0.6187139453483192, 0.4823974597714815, 0.3895729901052968, 0.46081730193074644, 0.5444108434105802, 0.6297110187222278]),
(([0.14,0.32,0.42,0.81,0.21],'TTTHHHHHH'),[0.2907741935483871, 0.25157009005730924, 0.23136284577678012, 0.2766575695593804, 0.3296000585271367, 0.38957299010529806, 0.4608173019307465, 0.5444108434105804, 0.6297110187222278]),
(([0.12,0.45,0.23,0.99,0.35,0.36],'THHTHTTH'),[0.28514285714285714, 0.3378256513026052, 0.380956725493104, 0.3518717367468537, 0.37500429586037076, 0.36528605387582497, 0.3555106542906013, 0.37479179323540324]),
(([0.03,0.32,0.59,0.53,0.55,0.42,0.65],'HHTHTTHTHHT'),[0.528705501618123, 0.5522060353798126, 0.5337142767315369, 0.5521920592821695, 0.5348391689038525, 0.5152373451083692, 0.535385450497415, 0.5168208803156963, 0.5357708613431963, 0.5510509656933194, 0.536055356823069])]

for inputs,output in testcases:
    if maxdiff(test(*inputs),output)<0.001:
        print 'Correct :)'
    else: print 'Incorrect :('