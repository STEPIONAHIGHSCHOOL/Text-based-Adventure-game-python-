
# STEP Engineering Summer Camp Final Project
<img width="690" height="500" alt="image" src="https://github.com/user-attachments/assets/5706f08a-892a-4de3-845b-8236588bc4a0" />
Copy and paste

Class 1: 
```python
def intro():
    print("winterwonderland")
    print("welcome to winterwonderland")
    print("You have spawned into the land of winter")
    print("ballet or mysterioushouse")
    choice= input("which one do you choose?(ballet/mysteriousehouse:)").lower()
    if choice == "ballet":
        ballet_room()
    elif choice == "mysterioushouse":
        mysterious_house()
    else: 
        print("restart")
        intro()
    def mysterious_house(): 
        print("you see elf onf the shelf")
        print("would you like to interact with the elf")
    user = input("Talk, Yes or No")
    if user == "Yes":
        print("Do you want a jolly cane?")
        print("Here, you can use this jolly cane as a key to the mysterious house")
        print("You run to the ballet with the jolly cane")
        print("You enter the ballet and it is very dark")
        print("You see a round figure arriving out of the shadows with a yellow glow")
    elif user == "No":
        print("Elf now considers you as an opp and is chasing you down")
    else: 
        print("restart")
intro()
```
classmate from class 1: 
```python

def intro():
    print("winterwonderland")
    print("welcome to winterwonderland")
    print("go to the theater")
    choice = input("Which one do you choose?)
    if choice == "ballet":
        ballet_room()
    elif choice == "mall":
        mall()
    else:
        print("restart")
        intro()
def ballet_room():
    print("You sit down in your seat")
```
Class 2: 
```python
def houseoftheclowns():
    print("Welcome to the house of the clowns")
    print("Would you like to be a Scary or Happy clown") 
    choice = input("Which do clown do you want?")
    if choice == "scary":
        scary()
    elif choice == "happy":
        happy()
    else:
        print("That is not an option try again.")
        houseoftheclowns()
def scary():
    print("Now you're a SCARY clown")
    scaryChoice = input("Do you want to scare people or hide in the sewers? (scare or sewer)")
    if scaryChoice == "scare":
        scarePeople()
    elif scaryChoice == "sewer":
        goSewer()
    else:
        print("That is not an option try again.")
        scary()
scary()

def happy():
    print("Now you're a HAPPY clown")
    happyChoice == input("Do you want to drive a car or make balloons ('car' or 'balloons')?")
    if happyChoice == "car":
        driveCar()
    elif happyChoice == "balloons":
        makeBalloons()
    else:
        print("That is not an option try again.")
        happy()
happy()
def scarePeople():
    print("You are a SCARY clown")
    print("This is too scary I'm running away!")
    scarePeople()
def goSewer():
    print("The sewer is making weird noises")
    goSewer()
```
