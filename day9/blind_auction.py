import os

auction_bids = []

def auction():
    i = 3
    while i > 0:
        i -= 1
        name = input("Enter name: ")
        bid = int(input("Enter bid: "))
        auction_bids.append({"Name": name, "Bid": bid})
        os.system('clear')

def getHighest():
    highest_bid = []
    for key in auction_bids:
        highest_bid.append(key['Bid'])
    print(max(highest_bid))
    

auction()
getHighest()
