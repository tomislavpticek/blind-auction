from replit import clear

auction = {}

print ("Welcome to the auction")
while True:
  name = input("Enter your name: ")
  bid = int(input("Enter your bid: $"))
  clear()
  auction[name] = bid
  
  cont = input("Are there any other bidders? Type 'no' to finish the auction or press enter to start a new bid: ")

  clear()
  
  if(cont.lower() == "no"):
    break

max_bid=0
for key in auction:
  if(auction[key] > max_bid):
    max_bid = auction[key]

winners = []
for key in auction:
  if(auction[key] == max_bid):
    winners.append({key: auction[key]})

if (len(winners) > 1):
  print("We have a tie between the following bidders:")
  for item in winners:
    for key in item:
      print(f"{key}")

else:
  for item in winners:
    for key in item:
      print(f"The winning bid goes to {key} with ${item[key]}")
