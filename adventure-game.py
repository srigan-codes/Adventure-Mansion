# Define the list of all the rooms
room_list = []

# Define the list of each room and append it to room_list
room = ["You are in bedroom 2.\nThere is a passage to the north and east.", 3, 1, None, None]
room_list.append(room)
room = ["You are in the south hall.\nThere is a passage to the north, east, and south.", 4, 2, 0, None]
room_list.append(room)
room = ["You are in the dining Room.\nThere is a passage to the north and south.", 5, None, 1, None]
room_list.append(room)
room = ["You are in bedroom 1.\nThere is a passage to the east and south.", None, 4, 0, None]
room_list.append(room)
room = ["You are in the north hall.\nThere is a passage in all directions.", 6, 5, 1, 3]
room_list.append(room)
room = ["You are in the kitchen.\nThere is a passage to the north, south, and west.", 0, None, 2, 4]
room_list.append(room)
room = ["You are on the balcony.\nThere is a passage to the south.", None, None, 4, None]
room_list.append(room)

# Initialize the current room to the first room
current_room = 0

# Define done as False
done = False

print("Welcome to THE MANSION")

# While done is False, the game will continue
while not done:
    # Let the user know where they are and ask for a direction
    print("\n" + room_list[current_room][0])
    direction = input("What direction would you like to go in, enter a letter (n,s,e,w enter Q to quit)? ").lower()

    # Depending on the direction the user inputs, update the current room or print an error
    if direction == "north" or direction == "n":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("\nYou can't go that way")
        else:
            current_room = next_room
    elif direction == "east" or direction == "e":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("\nYou can't go that way")
        else:
            current_room = next_room
    elif direction == "south" or direction == "s":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("\nYou can't go that way")
        else:
            current_room = next_room
    elif direction == "west" or direction == "w":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("\nYou can't go that way")
        else:
            current_room = next_room
    elif direction == "quit" or direction == "q":
        print("\nThank you for playing")
        done = True
    else:
        print("\nInvalid input. Try again.")