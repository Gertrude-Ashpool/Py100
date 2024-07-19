# The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

from art import logo
from replit import clear

#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")
bid_ongoing=True
bids={}

def find_highest_bidder(bidding_record):
    #create variables to keep the highest bid
    #and the name of the winner
    highest_bid = 0
    winner = ""
    #iterate through the entries in the dictionary
    for bidder in bidding_record:
        #store the value of the current dictionary entry in a temporary variable
        bid_amount = bidding_record[bidder]
        #check if the current bid is higher than all the previous bids
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of $ {highest_bid}")

#collect bids as long as user confirms for there to be more bidders
while bid_ongoing==True:
    bidder_name=input("What is your name?: ")
    bid=int(input("what is your bid?: $ "))
    #add an entry to the dictionary of bids
    bids[bidder_name]=bid
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'. \n ")
    if should_continue == "no":
        bid_ongoing = False
        #call the function to establish the highetst bid
        #pass over the collected bids as an argument
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

            
