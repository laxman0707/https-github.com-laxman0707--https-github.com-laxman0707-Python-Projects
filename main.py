from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bidlist={}
biddingfinished=False
def findhighestbidder(bidding_record):
  highestbid=0
  winner=""
  for bid in bidding_record:
    bidamount=bidding_record[bid]
    if bidamount > highestbid:
      highestbid=bidamount
      winner=bid
  print(f"the winner  {winner} is with bidamount ${highestbid}")

while not biddingfinished:
  key=input("what is the name?: \n" )
  value=int(input("what is the bid amount? \n $"))
  bidlist[key]=value
  print(bidlist)
  shouldcontinue=input("yes or no?")
  if shouldcontinue=="no":
    biddingfinished=True
    findhighestbidder(bidlist)
  elif shouldcontinue=="yes":
    clear()