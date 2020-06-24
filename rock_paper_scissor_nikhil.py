# RPC .v3
import random

# Varialbles
choices = ("Rock",  "Paper", "Scissor")
comp_score = 0
human_score = 0

winner_mes = "# !!! You got 1 point !!!"
loser_mes = "# !!! Opponent got 1 point !!!"
tie_mes =  "# !!! Tie !!!"

run = True  # Controls the main loop
Quit = False

# Checks if any of the player has got winning points
def winning(winning_pts):
	global run

	if comp_score == winning_pts: # Checks if the computer has won
		print("### Opponent won the game")
		run = False

	elif human_score == winning_pts: # checks if the player has won
		print("### YOU won the game !")
		run = False

# Ask the player to play again ,if game is over
def replay():
	global run
	# Runs if the main loop is false and not exited
	if not(run) and not(Quit):

		ask_replay = input('### Do you want to play again (|y|or|N|): ')

		if ask_replay == 'y':
			run = True


# ||| Main function |||Gets the input and checks it with some conditions
def process():
	global run
	global Quit
	global comp_score
	global human_score

	print("!!! Welcome to The 'RPC' !!!")
	# It get the input for winning points
	winning_pts = int(input("### What do you want the winning point to be (Enter a number) : "))

	# Prints the scores of both the players
	print("### Opponent Score : " + str(comp_score))
	print("### Your Score : " + str(human_score))

	while(run): # The main loop of the game
		computer = random.choice(choices)  # Helps the make random choices
		print(computer)
		print("### Please enter ['Rock' , 'Paper' or 'Scissor']   ['EXIT' to quit]")  # Tell the player what to enter
		human = input("# Please Enter : ")

		# Checks for who got the point
		if computer ==  human:
			print(tie_mes)

		elif computer == "Rock" and human == "Paper":
			print(winner_mes)
			human_score += 1
		
		elif computer == "Rock" and human == "Scissor":
			print(loser_mes)
			comp_score += 1

		elif computer == "Paper" and human == "Rock":
			print(loser_mes)
			comp_score += 1

		elif computer == "Paper" and human == "Scissor":
			print(winner_mes)
			human_score += 1

		elif computer == "Scissor" and human == "Rock":
			print(winner_mes)
			human_score += 1

		elif computer == "Scissor" and human == "Paper":
			print(loser_mes)
			comp_score += 1

		elif human == "EXIT": # if input is 'Exit' it stops the whole program
			Quit = True
			run = False
			print("!!! Come Back Soon !!!")
			print("### EXITED")
			break

		else:
			print("### OOPS, your input must be |Rock| or |Paper| or |Scissor|")  # Tells what to enter, in the case of unmatched input

		# Prints the present input
		print("# Opponent Score : " + str(comp_score))
		print("# Your Score : "+ str(human_score))

		# Refreshes the input
		human = ""
		computer = ""

		# checks if somebody as won
		winning(winning_pts)

	# refreshes the scores
	human_score = 0
	comp_score = 0

	# if the game is over, it ask the player to play again
	replay()

# Runs the process function if run is true (if player wants to)
while(run):
	process()