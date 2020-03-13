

continent =0 

def Intro():
    print("Welcom to survival")
    print(" ")
    print("The point of tbe game is to survive.")
    print(" ")
    print("Type the number of what you want to select.")
    print(" ")
    print("Locations: ")
    print("1: North America")
    print("2: South America")
    print("3: Europe")
    print("4: Africa")
    print("5: Asia")
    print("6: Antarctica")
    print("7: Australia")
        
    continent = input("Where do you want to go? ")
    if(continent == '1'):
        NorthAmerica()
    elif(continent == '2'):
        SouthAmerica()
    elif(continent == '3'):
        Europe()
    elif(continent == '4'):
        Africa()
    elif(continent == '5'):
        Asia()
    elif(continent == '6'):
        Antarctica()
    elif(continent == '7'):
        Australia()
    else:
        print("Invalid. Not a choice.")
        Intro()

    
    
        
    


       
def NorthAmerica():
    print("Cities: ")
    print("1: New York City")
    print("2: Kansas City")
    print("3: Las Angeles")
    print("4: Mexico City")
    print("5: Vancouver")
    print("6: Toronto")

    route = input(str("Which city do you want to go to? "))
    if(route == '1'):
        NewYork()

def SouthAmerica():
    print("Cities: ")
    print("Rio De Jeniro")
    print("Benous Aires")
    print("Lima")

    route = input(str("Which city do you want to go to? "))

        
def Europe():
    print("Cities: ")
    print("London")
    print("Paris")
    print("Rome")

def Africa():
    print("Cities: ")
    print("Cairo")
    print("Kinshasa")
    print("Cape Town")

    route = input(str("Which city do you want to go to? "))

def Asia():
    print("Cities: ")
    print("Hong Kong")
    print("Tokyo")
    print("Seoul")

    route = input(str("Which city do you want to go to? "))

def Antarctic():
    i =0
    while(i==0):
        print("YOU DIE")
def Australia():

    print("YOU BURN TO DEATH")


def NewYork():
    print("You now have COVID-19")

    route = input("Do you self corintine? Yes = 1 or N0 = 2?")

    if(route == "1"):
        print("You gain weight and die of diebetas!")
    elif(route == "2"):
        print("You are arrested for spreading the virus")

def KansasCity():
    i = 0
    while(i <100):
        print("You win the game!")
        i+=1
def LasAngelos():
    print("There is a homeless person sitting of the side of the road.")
    print("Whhat do you do?")
    print("1: Give the person money and walk away.")
    print("2: Aviod eye contact and proceed to run away as fast as you can.")
    print("3: Yell at the persom to get a job.")
    print("4: Sit down to talk with the person.")

    op = input("What do you choose?")

    if(op == '1'):
        print("Yah. Ypu helped somebody.")
    elif(op == '2'):
        print("As you are running away, you get hit by a car and die.")
        

Intro()





