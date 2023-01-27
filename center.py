#TO USE CODE GO TO "fullstory.py" THAT IS WHERE ALL FUNCTIONS WORK
import vars as v #Importing the vars code for my variables and fuctions

def ccenter(people,health,escapedb,healthdb,cperson,cworld,cperson2): #Deffening my ccenter so it can be called in the full story
    counter = 0; escape = 0 #setting local variables
    if cworld[1] == 0: #if everyone is asleep then only cperson does stuff
        #give the player options
        user_input = str.lower(input(f"{cperson} walks straight and into a corn field, they can ({v.yellow}1{v.rc}) Keep going, ({v.yellow}2{v.rc}) Go to sleep, or ({v.yellow}3{v.rc}) Turn back, ({v.yellow}4{v.rc}) {v.magenta}Change character{v.rc}\n"))
    elif cworld[1] == 1: #if everyone is awake then they all get the option
        #give the player options
        user_input = str.lower(input(f"The group walks straight and into a corn field, they can ({v.yellow}1{v.rc}) Keep going, ({v.yellow}2{v.rc}) Go to sleep, or ({v.yellow}3{v.rc}) Turn back, ({v.yellow}4{v.rc}) {v.magenta}Change character{v.rc}\n"))
    while True:
        if user_input == "1": #Checking if the player wanted to go farther
            if counter >= 2: #Check if this is the third time in a row
                if cworld[1] == 0: #See if the group is awake or not
                    print(f"{cperson} escapes to the other side of the field into a train yard") #If only one person
                    escapedb.append(cperson) #Add the player to the list of people that escapes
                    index2 = 0 #setting a local variable
                    for i in people:
                        if i == cperson:
                            healthdb.append(health[index2]) #add there health to the escaped people heath list
                            health.remove(health[index2]) #remove the health from the health list
                        index2 += 1
                    people.remove(cperson) #removing cperson from the list of people
                    cperson = v.newpers() #getting a new cperson
                    print(f"{v.yellow}You are now {cperson}{v.rc}") #Telling the player who they are
                    break
                if cworld[1] == 1: #If their awake
                    print("The whole group escaped into the train yard") #They all leave
                    escapedb += people #Adding people to the list of escaped
                    people = [] #Setting people to empty to leave the while
                    healthdb += health #Adding all there health to the escaped list
                    health = [] #Emptying the health list
                    escape = 1 #escape = 1 to break out of a list
                    break
            else:
                counter += 1 #telling the computer you went into the field
                if cworld[1] == 0: #if awake or asleep
                    print(f"{cperson} wanders farther into the field") #tell the player what they did
                elif cworld[1] == 1:
                    print(f"The group wanders farther into the field")
        elif user_input == "2": #if the player wanted to sleep
            health, people, cperson, cperson2 = v.sleep() #do the sleep function
        elif user_input == "3": #if the player wanted to leave
            if cworld[1] == 0: #awake or asleep
                print(f"{cperson} walks back out of the field.") #walk back
            elif cworld[1] == 1:
                print(f"The group walks back out of the field.")
            counter = 0 #Telling the computer you did something other then farther
            break
        elif user_input == "4": #If they wanted to change there person
            cperson = v.perchange()
        else:
            print(v.error)
        if cworld[1] == 0:#awake or not
            #What user can do if they put a bad input
            user_input = str.lower(input(f"{cperson} can ({v.yellow}1{v.rc}) Keep going, ({v.yellow}2{v.rc}) Go to sleep, or ({v.yellow}3{v.rc}) Turn back, ({v.yellow}4{v.rc}) {v.magenta}Change character{v.rc}\n"))
        if cworld[1] == 1:
            user_input = str.lower(input(f"The group can ({v.yellow}1{v.rc}) Keep going, ({v.yellow}2{v.rc}) Go to sleep, or ({v.yellow}3{v.rc}) Turn back, ({v.yellow}4{v.rc}) {v.magenta}Change character{v.rc}\n"))
    return cperson,escape,cperson2,people,health,escapedb,healthdb