import random

# Psuedo Code

# Ask the user for a sign
def get_users_sign():
	my_prompt = 'What sign do you want to use?\n'
	my_prompt += 'Press "R" for rock\n'
	my_prompt += 'Press "P" for paper\n'
	my_prompt += 'Press "S" for scissors\n'
	my_prompt += 'Press "Q" to quit\n'
	return input(my_prompt + '>>')

# Make sure they used a legal sign
def validate_input(res):
	if res == "R" or res == "P" or res == "S":
		return True
	else:
		print('You did not use a proper letter\n\n')
		return False

# Figure who won or if it is a tie
def determine_winner(res, comp_ai):
	if res == comp_ai:
		return "tie"
	elif (res == "R" and comp_ai == "S") or (res == "S" and comp_ai == "P") or (res == "P" and comp_ai == "R"):
		return "win"
	else:
		return "loss"

# Tell the user what happened
def print_win_screen(result):
	if result == "win":
		print("Good job, you won!")
	elif result == "tie":
		print("Close, but this round is a draw!")
	else:
		print("You lose because your bad at luck!")

def print_choices(res, comp_res):
	print("\n\tYou chose {}, and the computer chose {}".format(res, comp_res))

# Pick a random choice for the computer
def computer_picks_an_answer():
	choices = ["R", "P", "S"]
	return random.choice(choices)


# Program start
user_input = ""

while True:
	user_input = get_users_sign()
	user_input = user_input.upper()
	if user_input == 'Q':
		break
	if validate_input(user_input):
		computers_answer = computer_picks_an_answer()
		game_result = determine_winner(user_input, computers_answer)
		print_win_screen(game_result)
		print_choices(user_input, computers_answer)
		if game_result == "tie":
			pass
		else:
			break
