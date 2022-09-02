# Import random method from randint module
from random import randint

# Define the possible roles
roles = ["Bear", "Ninja", "Cowboy"]
score = 0
# returns true iff parameter user_input is a valid role (belongs to roles array)
def valid_role(user_input):
    is_role = False
    for role in roles:
        if user_input == role:
            is_role = True
    
    return is_role

# determine the initial computer role
computer_role = roles[randint(0, 2)]
# initialize the game loop control Boolean
is_playing = True

# continue playing the game until is_palyer is set to false
while is_playing:
    player_role = input("Bear, Ninja, or Cowboy? > ")
    #prompt the user for input until they enter a valid role
    while not valid_role(player_role):
        player_role = input("Bear, Ninja, or Cowboy? > ")

    # execute the conditional game logic
    if computer_role == player_role:
        print("DRAW")
    elif computer_role == "Cowboy":
        if player_role == "Bear":
            print(f"You lose! {player_role} is shot by {computer_role}")
        else:
            print(f"You win! {player_role} defeats {computer_role}")
    elif computer_role == "Bear":
        if player_role == "Cowboy":
            print(f"You win! {player_role} shoots {computer_role}")
        else:
            print(f"You lose! {player_role} is eaten by {computer_role}")
    elif computer_role == "Ninja":
        if player_role == "Cowboy":
            print(f"You lose! {player_role} is defated by {computer_role}")
        else:
            print(f"You win! {player_role} eats {computer_role}")

    #prompt to play again, play again unless player enters exactly "no"
    play_again = input("Would you like to play again? (yes/no) > ")

    if play_again == "no":
        is_playing = False
    else:
        computer_role = roles[randint(0, 2)]

