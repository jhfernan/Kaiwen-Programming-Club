import random

# Psuedo Code

# Ask the user for a sign
def get_users_sign():
	my_prompt = 'What sign do you want to use?\n'
	my_prompt += 'Press "R" for rock\n'
	my_prompt += 'Press "P" for paper\n'
	my_prompt += 'Press "S" for scissors\n'
	return input(my_prompt + '>>')

# Make sure they used a legal sign
def validate_input(response):
	if response == "R" or response == "P" or response == "S":
		return True
	else:
		print('You did not use a proper letter')
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

# Pick a random choice for the computer
def computer_picks_an_answer():
	choices = ["R", "P", "S"]
	return random.choice(choices)
