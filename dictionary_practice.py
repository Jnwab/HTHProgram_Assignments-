Retail_prices = {"Chicken":1.59, "Beef":1.99, "Cheese":1.00, "Milk":2.50}
Video_games = { "Guilty Gear":"Fighting", "Mario Kart": "Racing", "Lego Worlds":"Creative", "Fornite":"Battle Royale"}
#Examples
print(Video_games["Guilty Gear"])

#Variable TIME. IV + V

Chicken = (Retail_prices["Chicken"])
Beef = (Retail_prices["Beef"])
Cheese = (Retail_prices["Cheese"])
Milk = (Retail_prices["Milk"])
#print("The Retail Price of Chicken is","$"+str(Chicken))
#print(Milk)
#The function bellow is mean to show the total price of whatever's in it.
def Full_price(Item1,Item2):
    price= Retail_prices[Item1]+Retail_prices[Item2] #Let's you acess the dicitionary and place it there.
    print("Total price of",Item1,"And",Item2,"is",(price))#USE COMMAS, would be kinda cold.
    if price>3:
        print(Item1,"is far too expensive here!")


Full_price("Chicken","Beef")