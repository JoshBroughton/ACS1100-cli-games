# flashcards.py

# import the json module
import json


# initialize starting score to 0
score = 0
# loads cards from given file path, expects JSON format
def load_cards(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# assign the parsed json data to data
data = load_cards('me-capitals.json')

# initialize total as the length of the cards array
total = len(data["cards"])

# group logic for checking correctness and incrementing score into one function
def ask_question(card):
    global score
    guess = input(card["q"] + " > ")

    if guess.lower() == card["a"].lower():
        score += 1
        return True
    else:
        return False

# function for printing message depending on whether user was correct
def answer_message(is_correct):
    if is_correct:
        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")

# function for pritning end message depending on score
def end_message():
    if score / total < 0.5:
        end_message = "You need more practice!"
    elif score == total:
        end_message = "Perfect score, amazing!"
    else:
        end_message = "Good work!"

    print(f"Thanks for playing! You got {score} out of {total} cards correct! {end_message}")

# iterate over the dictionary containing the cards and ask the question in each card
for i in data["cards"]:
# ask the question, save correctness in Boolean is_correct, iterate score if appropriate    
    is_correct = ask_question(i)
# print the appropriate answer message    
    answer_message(is_correct)
#print the appopriate end message
end_message()
