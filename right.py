import vars as v
import random
import time

def rright(people, health, escapedb, healthdb, cperson, cworld, cperson2): #Deffiniton for the rringt to use in the main file
    escape = 0; wl = 0 #Setting local vars
    if cworld[1] == 0: #If there asleep
        user_input = str.lower(input(f"{cperson} walks up to a river that seems to be deep and is moving super fast.\n{cperson} can ({v.yellow}1{v.rc}) Go to sleep, ({v.yellow}2{v.rc}) Cross here, ({v.yellow}3{v.rc}) Look for a crossing, ({v.yellow}4{v.rc}) Go back, ({v.yellow}5{v.rc}) {v.magenta}Change character{v.rc}.\n"))
    elif cworld[1] == 1: #if not
        user_input = str.lower(input(f"The group walks up to a river that seems to be deep and is moving super fast.\n{cperson} can ({v.yellow}1{v.rc}) Go to sleep, ({v.yellow}2{v.rc}) Cross here, ({v.yellow}3{v.rc}) Look for a crossing, ({v.yellow}4{v.rc}) Go back, ({v.yellow}5{v.rc}) {v.magenta}Change character{v.rc}.\n"))
    while escape != 1:
        if user_input == "1": #DO sleep if they want to sleep
            health, people, cperson, cperson2 = v.sleep()
        elif user_input == "2": #If the player wants to cross the river right here
            while user_input != "y" and user_input != "n":
                if cworld[1] == 1: #set up vote
                    user_input = str.lower(input(f"({cperson}) - Lets try to cross here.\n({cperson}) - IDK... It looks super deep.\nDo you want to cross? ({v.yellow}y{v.rc}, {v.red}n{v.rc})\n"))
                    wl = 0 #local var
                    if user_input == "n": #If player says no do vote
                        print(f"({cperson2}) - No I don't think we should.\n({cperson2}) - Well then lets take a vote.")#tell player
                        num = 0 #local var
                        for i in people: #for everyone in people
                            num += random.randint(0,1) #1 vote yes or no
                        if num > len(people)/2: #if it is bigger then half the people they win
                            wl = 1 #set win to 1
                            print("Well its decided then we will cross the river!") #Tell player
                        else:
                            wl = 0 #Set win to lose
                            print("Well its decided then we will not go through the river") #Tell player
                        break
                if user_input == "y" or wl == 1 or cworld[1] == 0: #if the player said yes the vote ended on yes or people were asleep
                    if cworld[1] == 1: #if everyone is asleep
                        print("Every one starts to cross the river") #Tell the player
                    while people != []: #while there are still people do this
                        temp = random.randint(0,3) #getting a random number to see if they live or not
                        index2 = 0 #local var
                        if temp == 3 or cperson == f"{v.blue}Sophia{v.rc}": #if the random numb was 3 or the cperson is sophia
                            print(f"({cperson}) {v.green}Survived the crossing and ran into the woods{v.rc}") #tell the player they lived
                            escapedb.append(cperson) #add cperson to the list of escaped people
                            for i in people: #for everyone in people
                                if i == cperson: #find the index value where the cperson is
                                    healthdb.append(health[index2]) #use that index to add to healthdb
                                    health.remove(health[index2]) #and remove itself from health
                                    break
                                index2 += 1 #incroment index2
                            v.people.remove(cperson) #remove cperson from people
                            people = v.people #update the local var for global var
                        else:
                            print(f"({cperson}){v.red} died in the river{v.rc}") #tell the player they died
                            for i in people: #for everyone in people
                                if i == cperson: #find index
                                    health.remove(health[index2]) #remove from health
                                index2 += 1
                            v.people.remove(cperson) #remove
                            people = v.people #update
                        time.sleep(0.5) #Sleep to show that it is updating
                        if people == []: #if the people list is emptey
                            escape = 1 #tell the code to end
                        else:
                            cperson = v.newpers(); cperson2 = v.newpers() #Get new people
                            if cworld[1] == 0: #if everyone is asleep
                                escapedb.append(cperson) #Add the player to the list of people that escapes
                                index2 = 0 #setting a local variable
                                for i in people:
                                    if i == cperson:
                                        healthdb.append(health[index2]) #add there health to the escaped people heath list
                                        health.remove(health[index2]) #remove the health from the health list
                                    index2 += 1
                                people.remove(cperson) #removing cperson from the list of people
                                cperson = v.newpers() #getting a new cperson
                                print(f"{v.yellow}You are now {cperson}{v.rc}") #tell the player who they are
                                break
                if user_input != "y" and user_input != "n": #if there is no yes or no
                    print(v.error) #print error
        elif user_input == "3": #if they wanted to go up the river
            if cworld[1] == 0: #if asleep then just the player escapes
                print(f"{cperson} crosses the river and escapes.") #tell the player
                escapedb.append(cperson) #update the lists
                index2 = 0
                for i in people: #do stuff again
                    if i == cperson: #I SHOULD MAKE A FUCTION
                        healthdb.append(health[index2]) #TRAVIS MAKE FUCTION
                        health.remove(health[index2]) #PlEASE
                        break
                    index2 += 1 #REMEMBER
                people.remove(cperson)
                cperson = v.newpers()
            if cworld[1] == 1: #if awake
                print(f"({cperson}) - lets go look for a better crossing up the river.") #Tell the player
                time.sleep(0.1) #Sleep like they are walking up
                print(f"The group walks up the river and finds a nice calm and shallow area to cross at.\nEveryone goes throught that and runs into the forest!") #Tell the player
                escapedb += people #MAKE ANOUTHER
                people = [] #FUCTION
                healthdb += health #OPTIMISE
                health = [] #PLEASE
                escape = 1
        elif user_input == "4": #if leave
            if cworld[1] == 0: #if asleep
                print(f"{cperson} walks back away from the river.") #Tell player
            if cworld[1] == 1: #if awake
                print(f"The group walks back away from the river.") #Tell player
            break
        elif user_input == "5": #If change player
            cperson = v.perchange() #Do person change
        else: #If none of them were true
            print(v.error) #Print error
        if escape != 1: #if nothing was given
            if cworld[1] == 0: #ask what the player wants to do if they gave a bad input
                user_input = str.lower(input(f"{cperson} can ({v.yellow}1{v.rc}) Go to sleep, ({v.yellow}2{v.rc}) Cross here, ({v.yellow}3{v.rc}) Look for a crossing, ({v.yellow}4{v.rc}) Go back, ({v.yellow}5{v.rc}) {v.magenta}Change character{v.rc}.\n"))
            if cworld[1] == 1:
                user_input = str.lower(input(f"The group can ({v.yellow}1{v.rc}) Go to sleep, ({v.yellow}2{v.rc}) Cross here, ({v.yellow}3{v.rc}) Look for a crossing, ({v.yellow}4{v.rc}) Go back, ({v.yellow}5{v.rc}) {v.magenta}Change character{v.rc}.\n"))
    return cperson,escape,cperson2,people,health,escapedb,healthdb