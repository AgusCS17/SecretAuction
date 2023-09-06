import art
import os
def highest_bid(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_ammount = bid_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder   
    print(f"The winner is {winner} with bid ${highest_bid}")
     
end_of_auction = False
data ={}

print(art.logo)
print("Welcome to secret auction ?")

while not end_of_auction:
    nama = str(input("What is your name? "))
    money = int(input("what's your bid? $"))
    data[nama] = money

    decision = input("Are there any other bidder? yes or no ").lower()

    if decision == "no":
        end_of_auction= True
        highest_bid(data)
        
    elif decision == "yes":
        os.system('cls')


 