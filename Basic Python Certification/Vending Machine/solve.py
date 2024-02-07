#!/bin/python3

import math
import os
import random
import re
import sys



# Vending Machine - OOP in Python

# Following requirements:
# It can be instantiated using the constructor VendingMachine(num_items, item_price) where num_items and denotes the number ofi tems in the machine, and item_price denotes the required number of coins to buy a single item.

# It has a method buy(req_items, money) that represents a buy request where req_items denotes the requested number of items , and money is the amount of the customer puts into the machine. Depending on the state of the machine, one of the following happens:

#   If there are enough items in the machine to serve the request and the given money is sufficient to buy the requested number of items, the number of items in the machinen is reduced by the requested number of items. The method returns an integer denotes the change given back after the purchase.

#   If there are fewer items in the machine than the requested number, it raises a ValueError exception with the message. "Not enough items in the machine". 

#   If there are enough items in the machine to serve the request but the given amount of money is less than their cost, it raises a ValueError exception with the message. "Not enough coins".breakpoint


class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price
        
    def buy(self, req_items, money):
        if req_items > self.num_items:
            return "Not enough items in the machine"
        elif money < req_items * self.item_price:
            return "Not enough coins"
        else:
            self.num_items -= req_items
            return money - (req_items * self.item_price)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")


    fptr.close()
