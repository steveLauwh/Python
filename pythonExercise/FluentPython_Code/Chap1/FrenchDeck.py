#!/usr/bin/env python3
# coding:utf-8

""" Chap 1
一摞有序的纸牌
集合类 collections-namedtuple

特殊方法(双下方法)
"""
from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamods clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for rank in self.ranks
										for suit in self.suits]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]

#beer_card = Card('7', 'diamods')

#print(beer_card)

deck = FrenchDeck()

#print(len(deck))

#print(deck[0])

#print(deck[-1])

#print(choice(deck))

#print(choice(deck))

#print(choice(deck))

#print(deck[:3])

#print(deck[12::13])

# for card in deck:
# 	print(card)

# for card in reversed(deck):
# 	print(card)

#print(Card('Q', 'hearts') in deck)

#print(Card('A', 'beats') in deck)

suit_values = dict(spades=3, hearts=2, diamods=1, clubs=0)
def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
	print(card)
