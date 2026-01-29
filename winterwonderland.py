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
