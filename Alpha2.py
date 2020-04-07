#Hello Everyone
from termcolor import colored

#getting the username
username = input('Please choose a user name.')
attempts = 0

#loop to verify username
c = False
while attempts != 3 and c != True:
	usernameA = input("Please reenter username.")
	attempts = +1
	if usernameA == username:
		print("congrats")
		c = True
	else:
		print('incorrect username please try again')

#get player name
name = input('What is your full name friend?')

#make player choose team
team = input(
    'Please pick between the folowing colors. \n Red, Yellow, Pink, or Blue?')

#get user birthday
month = input('What is the numeric value of the month you were born?')
while len(month) > 2:
	month = input('Please reenter the month you were born in a 2 digit format.')
day = input('What Day were you born')
while len(day) > 2:
	day = input('Please renter the day you were born with no more than a 2 digit value.')
year = input('What year were you born?')

#get player age
while len(year) > 4:
	year = input('Please reenter the year you were born in a 4 digit format.')
curYear = input('Please remind me what year is it?')
while len(curYear) > 4:
	curYear = ('Please reenter the current year in a 4 digit format.')
curMonth = input('Oh and the month too?')
age = (int(curYear) - int(year))
age = int(age)
if curMonth <= month:
	age = age
else:
	age = (age - 1)

#dictionary for month conversion
monconv = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

print(
	colored(
    "Hello " + name.title() +
    ", Welcome to world of python programmers. Here many new and old programmers come to make what ever their heart desires.", 'white'
	)
)
input('Press enter to continue')

if team.title() == 'Blue':
	print(
		colored(
	    'I see, you are fond of blue are you not? May I be the first to welcome you to Team Sky. We value freedom above all and love to explore.', "blue"
		)
	)
	input('Press Enter to continue')

elif team.title() == 'Red':
	print(
		colored(
	     'You have chosen well. Welcome to team Magma. Power 		and raw stregth are valued above all.', 'red'
		)
	)
	input('Press Enter to continue')

elif team.title() == 'Yellow':
	print(
		colored(
	    "You chose Yellow. Very, very interesting. I think we will have much to learn from you.", "yellow"
		)
	)
	input('Press Enter to continue')

elif team.title() == 'Pink':
	print(
		colored("Welcome to the team of love.", "pink")
	)
	input('Press Enter to continue')

animal = input('What animal do you relate to the most?')


#make a list of player info for sorting later
def player(a, b, c):
	player_1 = [a]
	player_1.append(b)
	player_1.append(c)
	return (player_1)


player(name, team, animal)

print('Welcome ' + name.title() + ' the ' + team.title() + ' ' +  animal.title() + '!')

if day == 1:
	print("Your were born on the first day of " + monconv.get(int
		(month)))
elif day == 2:
	print("You were born on the Seocnd day of " + monconv.get(int(month)))
elif day == 3:
	print("You were born on the third day of " + monconv.get(int(month)))
else:
	print("You were born " + (monconv.get(int(month))) + ',' + day + "th " + year + '.')

if age >= 75 and age < 100:
	print(
		" Over 75 you are, a master you must be. Hopefully expiernced or making a career change. "
	)
	player_file = open("player.txt", "w")

elif age == 23 and age > 16:
	print(
		'Your only,' + str(age) +  ' you must be new here. \n Let me know if you have any questions.'
	)
	player_file = open("player.txt", "w")
	
elif age >= 24 and age < 75:
	print(
	    'Hopefully you like this language more than the one you are switching from. You know my favorite is binary. I I dont really like english.'
	)
	player_file = open("player.txt", "w")

elif age <= 16 and age > 0:
	print(
		"welp hopefully you understand this more than I do."
	)
	player_file = open("player.txt", "w")

else:
	print('goodluck you are ' + str(age) + ' years old.')

	player_file = open("player.txt", "w")
