#Putting some things here that I have a feeling I'll need to do:
#putting some stuff outside the while loop
#Tracks the score
from xml.dom.minidom import ProcessingInstruction

total_mood_stats = {
    "Happy": 0,
    "Sad": 0,
    "Angry": 0
}
#defines the variable prior to while loop
main_menu_user_input = 0
#90% of the code is here
print("Welcome to the Mood Tracker!")
#we don't want this being asked every time
print("Let's get started, shall we? Please enter your name.")
user_name = input()
while main_menu_user_input != 3:
    #Main Menu interface, make this a thing I can call later
    #Helpful little tip I learned, change out the print lines when savin the file
    import os

    os.system('cls' if os.name == 'nt' else 'clear')
    #This bit is just for the debug console since it's not an OS
    #print("\n" * 50)
    print("Main Menu\n1. Log Mood\n2. View Mood Stats\n3. Exit")
    main_menu_user_input = int(input())
    print(main_menu_user_input)

    #Comments make my life easier
    #Option 1
    if main_menu_user_input == 1:
        print("How are you feeling today? Please type the number corresponding to your choice:\n1. Happy\n2. Sad\n3. Angry")
        user_mood = int(input())
        validation_user_mood = [1,2,3]
        while user_mood not in validation_user_mood:
            print("That was an invalid submission. Please try again.")
            user_mood = int(input())
        print("Thank you for your response! This will now go back to the main menu.")
        input()
        if user_mood == 1:
            total_mood_stats["Happy"] += 1
        if user_mood == 2:
            total_mood_stats["Sad"] += 1
        if user_mood == 3:
            total_mood_stats["Angry"] += 1

    #Comments make my life easier
    #Option 2
    if main_menu_user_input == 2:
        print(total_mood_stats)
        input()
print("Thank you for playing! Don't forget to subscribe for daily python challenges!")
