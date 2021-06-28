from typing import Counter


City_Names = ["San Francisco", "Atlanta", "Brooklyn", "Seattle", "Memphis", "Tampa", "Boston", "Hollywood", "Denver", "New Orleans"]

Ben10_Aliens =["Heat Blast", "Four Arms", "Diamond Head","UpChuck","Way Big","XLR8","Upgrade","Rath","Ditto","Ghost Freak", "RipJaw", "Eye Guy"]

three_aliens = Ben10_Aliens[0:2]

City_Names.append("New Jersey")
City_Names.extend(["Santa Cruz", "Selma", "Chicago" ])
City_Names.insert(7,"Washington Dc")

#if 5>2 or "Limbo" in "Daily Exercise": IF STATEMENTS
    #print("Booyah")
#for i in range(10): #loops, base loop anyways.
    #print("LET IT RIP")

#6/2/21, Using a While loop in order to access the index
#Access the value of index
#Make sure you're using index properly
def CitiesOfAmerica(Listofchoice):
    counter = 0
    while counter < len(Listofchoice):
        print(Listofchoice[counter])
        counter += 1
CitiesOfAmerica(City_Names)

def OrganizeCity(ListofChoice):
    print(len(ListofChoice[0]))
    counter = 0
    for city in ListofChoice:
        if(len(ListofChoice[counter]) > len(ListofChoice[counter+1])):
            counter+=1
        else:
            ListofChoice.remove(city)
            ListofChoice.append(city)
            counter+=1

