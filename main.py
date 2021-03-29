

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
	if response == "R" || response == "P" || response == "S":
		return true
	else:
		print('You did not use a proper letter')
		return false


# Figure who won or if it is a tie

# Tell the user what happened
