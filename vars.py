import random
import time

#Setting the new person
def newpers():
    global people #Getting the list of people that are alive/not asleep
    if people != []:
        #Randomising the person
        random.shuffle(people)
        temp = random.randint(1,len(people))-1
        cperson = people[temp] #setting the new person
    return cperson

#The code for opening the door
def opendoor():
    global health, cperson, cperson2, cworld, people, newpers; index2 = 0 #Getting the global code/setting local variables
    print(f"{cperson} trys to open the door") #Telling the player
    if cperson != f"{magenta}Elijah{rc}": #If the cperson is not Elija they die
        print(f"{cperson}{red} was crushed by the door and has now died{rc}") #Telling the player they dun messed up
        people.remove(cperson) #Removing the cperson from people
        #Removing the health
        for i in people:
            if i == cperson:
                health.remove(health[index2])
                break
            index2 += 1
        cperson = newpers(); cperson2 = newpers() #Setting the cperson and cperson2
        print(f"{yellow}You are now {cperson}{rc}") #Telling the player who they are now
    else:
        print(f"it starts to fall and they manage to get out of the way.") #Telling the player that elija no die
    if cworld[1] == 0 and len(people) > 1: #if people asleep and there is more then 1 person alive
        print("In all the noise everyone else wakes up.") #wake up
        cworld[1] = 1 #tell the code people woke up
    cworld[0] = 1 #Telling code the door broke
    return cworld, cperson, health, people, cperson2

#taking a random amount of health
def renheathc():
    global people, health, cperson2
    temp = random.randint(0,2) #Getting how much health it will take
    index2 = 0; died = 0 #setting local vars
    for i in people: #finding the person index
        if i == cperson2:
            if health[index2]-temp > 0: #checking if the health would kill them
                health[index2] -= temp #If not subtract there health
                break
            else:
                died = 1 #Telling the computer they died
                cperson2 = newpers() #Getting a new person
                health.remove(health[index2]) #removing there health
                people.remove(people[index2]) #removing them from people
            break
        index2 += 1 #incromenting the index2 variable
    return health, temp, cperson2, people, died

def perchange():
    global people, health, newpers, error #getting variables
    word = ""; index2 = 1 #setting local variables
    for i in people: #for everyone in people
        word += f"({index2}) {i}" #Add the index of them and the person to a print
        if index2 < len(people): #if it is not the last person to be added
            word += ", " #add this
        index2 += 1
    while True:
        user_input = str.lower(input(f"Who do you want? {word}\n")) #asking the player who they want to be
        if user_input.isnumeric(): #checking that they inputed a number
            user_input = int(user_input)-1 #if they did remove 1 from there input to make it a proper index
            break
        else:
            print(error) #if they didnt print error
    cperson = people[user_input] #setting there cperson
    print(f"{yellow}you are now {cperson}{rc}") #Conferming who they are
    return cperson

#Sleep fuction
def sleep():
    global error, cperson, cperson2, people, health; wl = 0 #getting global variables/Setting local ones
    while True:
        #Setting up the problem
        user_input = str.lower(input(f"({cperson}) - Lets just sleep, its hard to see in the dark. We will probably be able to get out faster during the day.\n({cperson}) - Couldn't whoever took us here find us?\nDo you want to sleep? ({yellow}y{rc}, {red}n{rc})\n"))
        if user_input == "n": #if they dont want to sleep
            print(f"({cperson2}) - No I don't think we should!\n({cperson2}) - Well then lets take a vote!")
            num = 0
            for i in people: #For everyone that is alive
                num += random.randint(0,1) #they get a random yes or no vote
            if num > len(people)/2: #if there are more yes votes then half of people
                wl = 1 #Then they win
                print("Well its decided then we will escape tonight!") #Telling the player
            else:
                wl = 0 #they lose
                print("Well its decided then we will escape tomarrow morning!\nThe next Morning") #Telling the player
        if user_input == "y" or wl == 1: #If the player wanted to sleep/the vote was yes
            print("Every one goes to sleep") #telling the player
            cperson2 = newpers() #Getting a new cperson2
            health, temp, cperson2, people, died = renheathc() #Removing a random amount of health
            time.sleep(random.randint(1,20)/100) #sleepig a random amount of time 0.01 to 2 seconds
            if died == 0: #if they didnt die
                print(f"({cperson2}) - {red}AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH (They lost {temp} health){rc}") #Tell the player how much they got hurt
                died = -1 #Setting died to -1 so nothing else trigers
            elif died == 1: #if they did die
                print(f"{cperson2} {red}lost {temp} heart(s) and has now died.{rc}") #Tell the player by how much and who
                cperson2 = newpers() #getting a new cperson2
                died = -1 #Setting die so nothing triggers
            break
        else:
            print(error) #Else print error
    return health,people,cperson,cperson2

#Vars

#The variables for changing the color that is printed in terminal
red =  "\033[1;31m"
green =  "\033[1;32m"
yellow =  "\033[1;33m"
blue =  "\033[1;34m"
magenta =  "\033[1;35m"
cyan =  "\033[1;36m"
white =  "\033[1;37m"
rc = "\033[1;0m"

#The starting people that can be used
people = [f'{blue}Sophia{rc}', f'{magenta}Liam{rc}', f'{green}Olivia{rc}', f'{magenta}Elijah{rc}', f'{magenta}Oliver{rc}']
"""
Sophia = small bad but good swim flex
Liam = fat
Olivia = smart
Elijah = small but strok
Oliver = big but strok
"""
#The health for everyone random amount 3 to 5
health = [random.randint(3,5), random.randint(3,5), random.randint(3,5), random.randint(3,5), random.randint(3,5)]
escapedb = [] #Setting the escapedb to use later
healthdb = [] #Setting the healthdb to use later
cperson = newpers() #setting cperson
cperson2 = newpers() #Setting cperson2
error = f"{red}Error, try inputing again{rc}" #Setting the error msg for later\
cworld = [0, 0, 0] #Setting the cworld to use later
escape = 0 #Setting escape to use later