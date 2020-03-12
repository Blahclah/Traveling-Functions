

continent =0 

def Intro():
    print("Locations: ")
    print("1: North America")
    print("2: South America")
    print("3: Europe")
    print("4: Africa")
    print("5: Asia")
    print("6: Antarctica")
    print("7: Australia")
        
    continent = input("Where do you want to go? ")
    if(continent == 'North America'):
        NorthAmerica()
    elif(continent == 'South America'):
        SouthAmerica()
    elif(continent == 'Europe'):
        Europe()
    elif(continent == 'Africa'):
        Africa()
    elif(continent == 'Asia'):
        Asia()
    elif(continent == 'Antarctica'):
        Antarctica()
    elif(continent == 'Australia'):
        Australia()
    else:
        print("Invalid. Not a choice.")
        Intro()

    
    
        
    


       
def NorthAmerica():
    print("Cities: ")
    print("New York City")
    print("Kansas City")
    print("Las Angeles")
    print("Mexico City")
    print("Vancouver")
    print("Toronto")

    route = input(str("Which city do you want to go to? "))

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
    print("You have have to self corintine")

    rount = input("Do you self corintine? Y or N?")

    if(route == 'Y'):
        print("You gain weight and die of diebetas!")
    elif(route == 'N'):
        print 



Intro()





