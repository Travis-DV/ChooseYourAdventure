# -----------------------------------------------------------
#
#    Project:      Ricoil Sim v2
#    Author:       Travis Findley
#    Created:      27/2/2022
#    Description:  Cool Ricoil Sim, second try first one big bad
#
# -----------------------------------------------------------

#Libs
import random
import time

#Functions
def newpers():
    global people, health
    random.shuffle(people)
    while True:
        temp = random.randint(1,len(people))-1
        if health[temp] > 0:
            cperson = people[temp]
            break
        else:
            print(f"({people[temp]})\033[1;31m was at 0 health, and has now died.\033[1;0m")
            health.remove(health[temp])
            people.remove(people[temp])
    return cperson, health, people

def opendoor():
    global health, cperson, cperson2, cworld, people, newpers, cperson2c; index2 = 0
    print(f"{cperson} trys to open the door")
    if cperson != "\033[1;36mElijah\033[1;0m":
        print(f"{cperson}\033[1;31m was crushed by the door and has now died\033[1;0m")
        people.remove(cperson)
        for i in people:
            if i == cperson:
                health.remove(health[index2])
                break
            index2 += 1
        cperson, health, people = newpers()
        cperson2, health, people = cperson2c()
        print(f"\033[1;33mYou are now {cperson}\033[1;0m")
    else:
        print(f"it starts to fall and they manage to get out of the way.")
    if cworld[1] == 0:
        print("In all the noise everyone else wakes up.")
        cworld[1] = 1
    cworld[0] = 1
    return cworld, cperson, health, people, cperson2

def renheathc():
    global people, health, cperson2, cperson2c
    temp = random.randint(0,2)
    index2 = 0; died = 0
    for i in people:
        if i == cperson2:
            if health[index2]-temp > 0:
                health[index2] -= temp
                break
            else:
                died = 1
                cperson2, health, people = cperson2c()
                health.remove(health[index2])
                people.remove(people[index2])
            break
        index2 += 1
    return health, temp, cperson2, people, died

def perchange():
    global people, health, newpers, error
    word = ""
    index2 = 1
    for i in people:
        word += f"({index2}) {i}"
        if index2 < len(people):
            word += ", "
        index2 += 1
    while True:
        user_input = str.lower(input(f"Who do you want? {word}\n"))
        if user_input.isnumeric():
            user_input = int(user_input)-1
            break
        else:
            print(error)
    cperson = people[user_input]
    print(f"\033[1;33myou are now {cperson}\033[1;0m")
    return cperson

def cperson2c():
    global newpers, cperson, cperson2, health, people
    while cperson2 == "" or cperson2 == cperson:
        cperson2, health, people = newpers()
    return cperson2, health, people

#Vars
people = ['\033[1;34mSophia\033[1;0m', '\033[1;35mLiam\033[1;0m', '\033[1;32mOlivia\033[1;0m', '\033[1;36mElijah\033[1;0m', '\033[1;36mOliver\033[1;0m']
"""
Sophia = small bad but good swim flex
Liam = fat
Olivia = smart
Elijah = small but strok
Oliver = big but strok
"""
health = [random.randint(3,5), random.randint(3,5), random.randint(3,5), random.randint(3,5), random.randint(3,5)]
escapedp = []
healthep = []
cperson, health, people = newpers()
error = "\033[1;31mError, try inputing again\033[1;0m"
cworld = [0, 0, 0]
cperson2 = ""
counter = 0
escape = 0
wl = 0

#User Code
while True:
    while people != []:
        print(f"*SKERRRRRRRRT*, *THUD THUD THUD* (car doors closing) \033[1;31m*bang*\033[1;0m (knocked out)")
        time.sleep(1)
        while True:
            user_input = str.lower(input(f"{cperson} wakes up in the dark, and looks around realizing that they are in a barn.\n{cperson} hears gunts and growns coming from other people.\n{cperson} realizes that they are with {len(people)-1} other people.\n{cperson} sees a door, and can \n (\033[1;33m1\033[1;0m) try to leave through that door, \n (\033[1;33m2\033[1;0m) wait for everyone to wake up,\n (\033[1;33m3\033[1;0m) Look around.\n  "))
            if user_input == "1":
                cworld, cperson, health, people, cperson2 = opendoor()
                break
            elif user_input == "2":
                time.sleep(random.randint(10,45)/10)
                while user_input != "y" or user_input != "n":
                    if cworld[1] == 0:
                        print(f"{cperson} waits for all {len(people)-1} to wake up.")
                        cworld[1] = 1
                        if cworld[0] == 0:
                            user_input = str.lower(input(f"Does {cperson} want to open the door? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
                    if user_input == "y":
                        cworld, cperson, health, people, cperson2 = opendoor()
                        break
                    elif user_input == "n":
                        break
                    else:
                        print(error)
                break
            elif user_input == "3":
                user_input = str.lower(input(f"{cperson} looks around and sees a door and a hole in the wall, they can\n (\033[1;33m1\033[1;0m) try to leave through the door, \n (\033[1;33m2\033[1;0m) wait for everyone to wake up,\n (\033[1;33m3\033[1;0m) Go through the hole in the ground.\n  "))
                while True:
                    if user_input == "1" or user_input == "2" or user_input == "3":
                        break
                    else:
                        print(error)
                        user_input = str.lower(input(f"{cperson} can\n (\033[1;33m1\033[1;0m) try to leave through the door, \n (\033[1;33m2\033[1;0m) wait for everyone to wake up,\n (\033[1;33m3\033[1;0m) Go through the hole in the ground.\n  "))
                if user_input == "1":
                    cworld, cperson, health, people, cperson2 = opendoor()
                elif user_input == "2":
                    time.sleep(random.randint(10,45)/10)
                    while user_input != "y" or user_input != "n":
                        if cworld[1] == 0:
                            print(f"{cperson} waits for all {len(people)-1} to wake up.")
                            cworld[1] = 1
                            if cworld[0] == 0:
                                user_input = str.lower(input(f"Does {cperson} want to open the door? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
                        if user_input == "y":
                            cworld, cperson, health, people, cperson2 = opendoor()
                            break
                        elif user_input == "n":
                            break
                        else:
                            print(error)
                    break
                elif user_input == "3":
                    print(f"{cperson} leaves through the hole in the wall")
                    cworld[2] = 1
                    break
            else:
                print(error)
        if cworld[2] == 0:
            cperson, health, people = newpers()
            cperson2, health, people = cperson2c()
            if cworld[0] == 1:
                print(f"({cperson2}) - welp we don't have a door anymore...")
            print(f"({cperson2}) - I see a hole in the floor!")
            if cworld[1] == 1:
                cperson2, health, people = cperson2c()
                health, temp, cperson2, people, died = renheathc()
                print(f"All {len(people)-1} people leave through the hole.")
                if died == 0:
                    print(f"\033[1;31mAHHHHHHHHHHHH {cperson2} screams!! Getting cought on a nail. (They lost {temp} heart(s))\033[1;0m")
                if died == 1:
                    print(f"{cperson2} \033[1;31mlost {temp} heart(s) getting cought on a nail, and has now died.\033[1;0m")
                user_input = str.lower(input(f"The group escapes and when they make it outside they can go (\033[1;33m1\033[1;0m) \033[1;35mLeft\033[1;0m, (\033[1;33m2\033[1;0m) \033[1;34mRight\033[1;0m, (\033[1;33m3\033[1;0m) \033[1;32mCenter\033[1;0m, (\033[1;33m4\033[1;0m) \033[1;36m\033[1;36mChange character\033[1;0m\033[1;0m\n"))
        elif cworld[1] == 0:
            user_input = str.lower(input(f"{cperson} escapes and when they make it outside they can go (\033[1;33m1\033[1;0m) \033[1;35mLeft\033[1;0m, (\033[1;33m2\033[1;0m) \033[1;34mRight\033[1;0m, (\033[1;33m3\033[1;0m) \033[1;32mCenter\033[1;0m, (\033[1;33m4\033[1;0m) \033[1;36m\033[1;36mChange character\033[1;0m\033[1;0m\n"))
        while escape != 1:
            if user_input == "2":
                user_input = str.lower(input(f"{cperson} walks up to a river that seems to be deep and is moving super fast.\n{cperson} can (\033[1;33m1\033[1;0m) Go to sleep, (\033[1;33m2\033[1;0m) Cross here, (\033[1;33m3\033[1;0m) Look for a crossing, (\033[1;33m4\033[1;0m) Go back, (\033[1;33m5\033[1;0m) \033[1;36mChange character\033[1;0m.\n"))
                while escape != 1:
                    if user_input == "1":
                        while user_input != "y" and user_input != "n":
                            user_input = str.lower(input(f"({cperson2}) - Lets just sleep, its hard to see in the dark. We will probably be able to get out faster during the day.\n({cperson}) - Couldn't whoever took us here find us?\nDo you want to sleep? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
                            if user_input == "n":
                                print(f"({cperson}) - No I don't think we should!\n({cperson2}) - Well then lets took a vote!")
                                num = 0
                                wl = 0
                                for i in people:
                                    num += random.randint(0,1)
                                if num > len(people)/2:
                                    wl = 0
                                    print("Well its decided then we will escape tomarrow morning!\nThe next Morning")
                                    break
                                else:
                                    wl = 1
                                    print("Well its decided then we will escape tonight!")
                            if user_input == "y" or wl == 1:
                                print("Every one goes to sleep")
                                cperson2, health, people = newpers()
                                health, temp, cperson2, people, died = renheathc()
                                time.sleep(0.2)
                                if died == 0:
                                    print(f"({cperson2}) - \033[1;31mAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH (They lost {temp} health)\033[1;0m")
                                    died = -1
                                elif died == 1:
                                    print(f"{cperson2} \033[1;31mlost {temp} heart(s) and has now died.\033[1;0m")
                                    cperson2, health, people = newpers()
                                    died = -1
                                break
                            if user_input != "y" and user_input != "n":
                                print(error)
                    elif user_input == "2":
                        while user_input != "y" and user_input != "n":
                            user_input = str.lower(input(f"({cperson2}) -  Lets try to cross here.\n({cperson}) - IDK... It looks super deep.\nDo you want to cross? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
                            wl = 0
                            if user_input == "n":
                                print(f"({cperson}) - No I don't think we should.\n({cperson2}) - Well then lets take a vote.")
                                num = 0
                                for i in people:
                                    num += random.randint(0,1)
                                if num > len(people)/2:
                                    wl = 1
                                    print("Well its decided then we will not go through the river")
                                else:
                                    wl = 0
                                    print("Well its decided then we will cross the river!")
                                break
                            if user_input == "y" or wl == 1:
                                print("Every one starts to cross the river")
                                while people != []:
                                    temp = random.randint(0,3)
                                    index2 = 0
                                    if temp == 3 or cperson == "\033[1;34mSophia\033[1;0m":
                                        print(f" \033[1;32m({cperson}) Survived the crossing and ran into the woods\033[1;0m")
                                        escape = 1
                                        escapedp.append(cperson)
                                        for i in people:
                                            if i == cperson:
                                                healthep.append(health[index2])
                                                health.remove(health[index2])
                                            index2 += 1
                                        people.remove(cperson)
                                    else:
                                        print(f"({cperson})\033[1;31m died in the river\033[1;0m")
                                        for i in people:
                                            if i == cperson:
                                                health.remove(health[index2])
                                            index2 += 1
                                        people.remove(cperson)
                                    if people != []:
                                        cperson, health, people = newpers()
                                    else:
                                        escape = 1
                                        break
                                escapedp += people
                            if user_input != "y" and user_input != "n":
                                print(error)
                    elif user_input == "3":
                        print(f"({cperson}) - lets go look for a better crossing up the river.")
                        time.sleep(0.1)
                        print(f"The group walks up the river and finds a nice calm and shallow area to cross at.\nEveryone goes throught that and runs into the forest!")
                        escapedp += people
                        people = []
                        healthep += health
                        health = []
                        escape = 1
                    elif user_input == "4":
                        print(f"{cperson} walk back away from the river.")
                        break
                    elif user_input == "5":
                        cperson = perchange()
                    else:
                        print(error)
                    if escape != 1:
                        user_input = str.lower(input(f"{cperson} can (\033[1;33m1\033[1;0m) Go to sleep, (\033[1;33m2\033[1;0m) Cross here, (\033[1;33m3\033[1;0m) Look for a crossing, (\033[1;33m4\033[1;0m) Go back, (\033[1;33m5\033[1;0m) \033[1;36mChange character\033[1;0m.\n"))
            elif user_input == "3":
                user_input = str.lower(input(f"{cperson} walks strate and into a corn field, they can (\033[1;33m1\033[1;0m) Keep going, (\033[1;33m2\033[1;0m) Go to sleep, or (\033[1;33m3\033[1;0m) Turn back, (\033[1;33m4\033[1;0m) \033[1;36mChange character\033[1;0m\n"))
                while True:
                    if user_input == "1":
                        if counter >= 2:
                            if cworld[1] == 0:
                                print(f"{cperson} escapes to the other side of the field into a train yard")
                                escapedp.append(cperson)
                                index2 = 0
                                for i in people:
                                    if i == cperson:
                                        healthep.append(health[index2])
                                        health.remove(health[index2])
                                    index2 += 1
                                people.remove(cperson)
                                while cperson == "" or cperson == cperson2:
                                    cperson, health, people = newpers()
                                print(f"\033[1;33mYou are now {cperson}\033[1;0m")
                                break
                            if cworld[1] == 1:
                                print("The whole group escaped into the train yard")
                                escapedp += people
                                people = []
                                healthep += health
                                health = []
                                escape = 1
                                break
                        else:
                            counter += 1
                            print(f"{cperson} wanders farther into the field")
                    elif user_input == "2":
                        counter = 0
                        wl = 0
                        while True:
                            user_input = str.lower(input(f"({cperson2}) - Lets just sleep, its hard to see in the dark. We will probably be able to get out faster during the day.\n({cperson}) - Couldn't whoever took us here find us?\nDo you want to sleep? (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
                            if user_input == "n":
                                print(f"({cperson}) - No I don't think we should!\n({cperson2}) - Well then lets take a vote!")
                                num = 0
                                for i in people:
                                    num += random.randint(0,1)
                                if num > len(people)/2:
                                    wl = 0
                                    print("Well its decided then we will escape tomarrow morning!\nThe next Morning")
                                else:
                                    wl = 1
                                    print("Well its decided then we will escape tonight!")
                            if user_input == "y" or wl == 1:
                                print("Every one goes to sleep")
                                cperson2, health, people = newpers()
                                health, temp, cperson2, people, died = renheathc()
                                time.sleep(0.2)
                                if died == 0:
                                    print(f"({cperson2}) - \033[1;31mAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH (They lost {temp} health)\033[1;0m")
                                    died = -1
                                elif died == 1:
                                    print(f"{cperson2} \033[1;31mlost {temp} heart(s) and has now died.\033[1;0m")
                                    cperson2, health, people = newpers()
                                    died = -1
                                break
                            else:
                                print(error)
                    elif user_input == "3":
                        print(f"{cperson} walk back out of the field.\n")
                        counter = 0
                        break
                    elif user_input == "4":
                        cperson = perchange()
                    else:
                        print(error)
                    user_input = str.lower(input(f"{cperson} can (\033[1;33m1\033[1;0m) Keep going, (\033[1;33m2\033[1;0m) Go to sleep, or (\033[1;33m3\033[1;0m) Turn back, (\033[1;33m4\033[1;0m) \033[1;36mChange character\033[1;0m\n"))
            elif user_input == "4":
                cperson = perchange()
            else:
                print(error)
            if escape != 1:
                if cworld[1] == 0:
                    user_input = str.lower(input(f"({cperson}) - can go (\033[1;33m1\033[1;0m) \033[1;35mLeft\033[1;0m, (\033[1;33m2\033[1;0m) \033[1;34mRight\033[1;0m, (\033[1;33m3\033[1;0m) \033[1;32mCenter\033[1;0m, (\033[1;33m4\033[1;0m) \033[1;36m\033[1;36mChange character\033[1;0m\033[1;0m\n"))
                elif cworld[1] == 1:
                    user_input = str.lower(input(f"The group - can go (\033[1;33m1\033[1;0m) \033[1;35mLeft\033[1;0m, (\033[1;33m2\033[1;0m) \033[1;34mRight\033[1;0m, (\033[1;33m3\033[1;0m) \033[1;32mCenter\033[1;0m, (\033[1;33m4\033[1;0m) \033[1;36m\033[1;36mChange character\033[1;0m\033[1;0m\n"))
    word = ""
    index2 = 0
    hp1 = 0; hp2 = 10
    if escapedp == []:
        print("You lost, everyone \033[1;31mdied.\033[1;0m")
    else:
        for i in escapedp:
            word += i
            if index2 < len(escapedp)-1:
                word += ", "
            index2 += 1
        index2 = 0
        for i in healthep:
            hp1 = i
            if hp1 < hp2:
                temp = index2
                hp2 = hp1
            index2 += 1
        print(f"\033[1;32mGOOD JOB! You had {len(escapedp)} survivers!\033[1;0m\nThey were {word}.\nThe person with the least health was {escapedp[temp]} they had {healthep[temp]} heart(s) left.\033[1;0m")
    user_input = str.lower(input("Do you want to play again (\033[1;33my\033[1;0m, \033[1;31mn\033[1;0m)\n"))
    if user_input == "n":
        break
    elif user_input == "y":
        people = ['\033[1;34mSophia\033[1;0m', '\033[1;35mLiam\033[1;0m', '\033[1;32mOlivia\033[1;0m', '\033[1;36mElijah\033[1;0m', '\033[1;36mOliver\033[1;0m']
        health = [random.randint(3,5), random.randint(3,5), random.randint(3,5), random.randint(3,5), random.randint(3,5)]
        escapedp = []
        healthep = []
        cperson, health, people = newpers()
        error = "\033[1;31mError, try inputing again\033[1;0m"
        cworld = [0, 0, 0]
        cperson2 = ""
        counter = 0
        escape = 0
        wl = 0