#OTHER FLIES TO COPY
#I DID NOT GET TO CODE THE "left" PATH< BECAUSE I RAN OUT OF TIME

# -----------------------------------------------------------
#
#    Project:      Choose your own adventure
#    Author:       Travis Findley
#    Created:      27/2/2022
#    Description:  A choose your own adventure
#
# -----------------------------------------------------------

#Libs
import random
import time
import right
import vars as v
import center

#User Code

while True:
    while v.people != []: #While there are still people to play as
        print(f"*SKERRRRRRRRT*, *THUD THUD THUD* (car doors closing) {v.red}*bang*{v.rc} (knocked out)") #Start the "story"
        time.sleep(1) #make player wait
        while True:
            #Give rest of story
            user_input = str.lower(input(f"{v.cperson} wakes up in the dark, and looks around realizing that they are in a barn.\n{v.cperson} hears gunts and growns coming from other people.\n{v.cperson} realizes that they are with {len(v.people)-1} other people.\n{v.cperson} sees a door, and can \n ({v.yellow}1{v.rc}) try to leave through that door, \n ({v.yellow}2{v.rc}) wait for everyone to wake up,\n ({v.yellow}3{v.rc}) Look around.\n  "))
            if user_input == "1": #If they want to open the door
                v.cworld, v.cperson, v.health, v.people, v.cperson2 = v.opendoor() #open the door
                break
            elif user_input == "2": #If the player wanted to wait
                time.sleep(random.randint(10,45)/10) #Make them wait
                while user_input != "y" or user_input != "n": #Start loop to make sure the player what I want them to do
                    if v.cworld[1] == 0: #If asleep
                        print(f"{v.cperson} waits for all {len(v.people)-1} to wake up.") #wake everyone up
                        if v.cworld[0] == 0: #Ask if want to open door if not already done
                            user_input = str.lower(input(f"Does {v.cperson} want to open the door? ({v.yellow}y{v.rc}, {v.red}n{v.rc})\n"))
                    if user_input == "y": #if yess
                        v.cworld, v.cperson, v.health, v.people, cperson2 = v.opendoor() #open door
                        v.cworld[1] = 1 #Store that it has been opened
                        break
                    elif user_input == "n": #If not
                        v.cworld[1] = 0 #Dont open the door
                        break
                    else:
                        print(v.error)
                break
            elif user_input == "3": #If they wanted to look around
                #Find out what they want to do
                user_input = str.lower(input(f"{v.cperson} looks around and sees a door and a hole in the wall, they can\n ({v.yellow}1{v.rc}) try to leave through the door, \n ({v.yellow}2{v.rc}) wait for everyone to wake up,\n ({v.yellow}3{v.rc}) Go through the hole in the ground.\n  "))
                while True: #make sure they put a valed input
                    if user_input == "1" or user_input == "2" or user_input == "3":
                        break
                    else: #If not show error and get a new one
                        print(v.error)
                        user_input = str.lower(input(f"{v.cperson} can\n ({v.yellow}1{v.rc}) try to leave through the door, \n ({v.yellow}2{v.rc}) wait for everyone to wake up,\n ({v.yellow}3{v.rc}) Go through the hole in the ground.\n  "))
                if user_input == "1": #if they want to open door then do that
                    v.cworld, v.cperson, v.health, v.people, v.cperson2 = v.opendoor()
                elif user_input == "2": #If they want to wait for everyone to wake up do that
                    time.sleep(random.randint(10,45)/10)
                    while user_input != "y" or user_input != "n":
                        if v.cworld[1] == 0:
                            print(f"{v.cperson} waits for all {len(v.people)-1} to wake up.")
                            v.cworld[1] = 1
                            if v.cworld[0] == 0:
                                user_input = str.lower(input(f"Does {v.cperson} want to open the door? ({v.yellow}y{v.rc}, {v.red}n{v.rc})\n"))
                        if user_input == "y":
                            v.cworld, v.cperson, v.health, v.people, v.cperson2 = v.opendoor()
                            break
                        elif user_input == "n":
                            break
                        else:
                            print(v.error)
                    break
                elif user_input == "3": #If they want to leave the the hole in the wall then tell the computer and player that
                    print(f"{v.cperson} leaves through the hole in the wall")
                    v.cworld[2] = 1
                    break
            else:
                print(v.error)
        if v.cworld[2] == 0: #If the player did not go through the hole in the floor alown
            v.cperson2 = v.newpers() #Get a new second person
            if v.cworld[0] == 1: #If door was done
                print(f"({v.cperson2}) - welp we don't have a door anymore...") #Remind player
            print(f"({v.cperson2}) - I see a hole in the floor!") #Tell player how people are going to escape
            if v.cworld[1] == 1: #If awake
                v.cperson2 = v.newpers() #Get a new cperson2
                v.health, temp, v.cperson2, v.people, died = v.renheathc() #Remove a random amount of health
                print(f"All {len(v.people)} people leave through the hole.") #Tell the player they left
                if died == 0: #If they did not die
                    print(f"{v.red}AHHHHHHHHHHHH {v.cperson2} screams!! Getting cought on a nail. (They lost {temp} heart(s)){v.rc}") #Tell the player how much they hurt
                if died == 1: #If they did die
                    print(f"{v.cperson2} {v.red}lost {temp} heart(s) getting cought on a nail, and has now died.{v.rc}") #Tell the player how much health was lost and that they died
        if v.cworld[1] == 1: #If awake or asleep get user input for what way they want to go
            user_input = str.lower(input(f"The group escapes and when they make it outside they can go ({v.yellow}1{v.rc}) {v.magenta}Left{v.rc}, ({v.yellow}2{v.rc}) {v.blue}Right{v.rc}, ({v.yellow}3{v.rc}) {v.green}Center{v.rc}, ({v.yellow}4{v.rc}) {v.magenta}{v.magenta}Change character{v.rc}{v.rc}\n"))
        elif v.cworld[1] == 0:
            user_input = str.lower(input(f"{v.cperson} escapes and when they make it outside they can go ({v.yellow}1{v.rc}) {v.magenta}Left{v.rc}, ({v.yellow}2{v.rc}) {v.blue}Right{v.rc}, ({v.yellow}3{v.rc}) {v.green}Center{v.rc}, ({v.yellow}4{v.rc}) {v.magenta}{v.magenta}Change character{v.rc}{v.rc}\n"))
        while v.escape != 1: #While they have not escaped
            if user_input == "2": #If they want to go right
                #Call the fuction in the right file
                v.cperson, v.escape, v.cperson2, v.people, v.health, v.escapedb, v.healthdb = right.rright(v.people, v.health, v.escapedb, v.healthdb, v.cperson, v.cworld, v.cperson2)
            elif user_input == "3": #If they want to go center
                #Call the center fuction in the center file
                v.cperson, v.escape, v.cperson2, v.people, v.health, v.escapedb, v.healthdb = center.ccenter(v.people, v.health, v.escapedb, v.healthdb, v.cperson, v.cworld, v.cperson2)
            elif user_input == "4": #if they wanted to change there person
                v.cperson = v.perchange() #Do that
            else:
                print(v.error)
            if v.escape != 1: #If they did not escape
                if v.cworld[1] == 0: #and there was a bad input get a new one based on awake or not
                    user_input = str.lower(input(f"({v.cperson}) - can go ({v.yellow}1{v.rc}) {v.magenta}Left{v.rc}, ({v.yellow}2{v.rc}) {v.blue}Right{v.rc}, ({v.yellow}3{v.rc}) {v.green}Center{v.rc}, ({v.yellow}4{v.rc}) {v.magenta}{v.magenta}Change character{v.rc}{v.rc}\n"))
                elif v.cworld[1] == 1:
                    user_input = str.lower(input(f"The group - can go ({v.yellow}1{v.rc}) {v.magenta}Left{v.rc}, ({v.yellow}2{v.rc}) {v.blue}Right{v.rc}, ({v.yellow}3{v.rc}) {v.green}Center{v.rc}, ({v.yellow}4{v.rc}) {v.magenta}{v.magenta}Change character{v.rc}{v.rc}\n"))
    word = ""; index2 = 0; hp = [0,0] #set vars needed here
    if v.escapedb == []: #If everyone is dead then tell the player they lost
        print(f"You lost, everyone {v.red}died.{v.rc}")
    else:
        for i in v.escapedb: #Make a string that has everyone that escaped
            word += i #adding name here
            if index2 < len(v.escapedb)-1: #If it is not the second to last person
                word += ", " #Add a , to make readable
            index2 += 1
        index2 = 0
        for i in v.healthdb: #For everything in healthdb
            hp[0] = i #Set it to the first part of health
            if hp[0] < hp[1]: #Check if greater
                temp = index2 #Set an index for futer use
                hp[1] = hp[0] #Set the second hp value to the larges version
            index2 += 1
        #Tell the player they won who had the most health how many people escaped etc.
        print(f"{v.green}GOOD JOB! You had {len(v.escapedb)} survivers!{v.rc}\nThey were {word}.\nThe person with the least health was {v.escapedb[temp]} they had {v.healthdb[temp]} heart(s) left.{v.rc}")
    #Ask if they want to play again
    user_input = str.lower(input(f"Do you want to play again ({v.yellow}y{v.rc}, {v.red}n{v.rc})\n"))
    if user_input == "n": #if not kill the code
        break
    elif user_input == "y": #if yes
        #Reset all the variables and start over
        v.people = [f'{v.blue}Sophia{v.rc}', f'{v.magenta}Liam{v.rc}', f'{v.green}Olivia{v.rc}', f'{v.magenta}Elijah{v.rc}', f'{v.magenta}Oliver{v.rc}']
        v.health = [random.randint(3,5), random.randint(3,5), random.randint(3,5), random.randint(3,5), random.randint(3,5)]
        v.escapedb = []
        v.healthdb = []
        v.cperson = v.newpers()
        v.cperson2 = v.newpers()
        v.cworld = [0, 0, 0]
        v.escape = 0