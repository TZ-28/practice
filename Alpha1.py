
name = input('What is your full name friend?')

team = input('Please pick between the folowing colors. \n 		Red, Yellow, Pink, or Blue?')

month = input('What is the numeric value of the month you were born?')
day = input('What Day were you born')
year = input('What year were you born?')
curYear= input('Please remind me what year is it?')
curMonth = input('Oh and the month too?')
age = (int(curYear) - int(year))
age = int(age)
if curMonth <= month:
	age = age
else: 
	age = (age - 1)

monconv = {
	1 : "January",
	2 : "February",
	3 : "March",
	4 : "April",
	5 : "May",
	6 : "June",
  7 : "July",
	8 : "August",
	9 : "September",
	10 : "October",
  11 : "November",
	12 : "December",

}

print("Hello " + name.title()  + ", Welcome to world of python programmers. Here many new and old programmers come to make what ever their heart desires.")

if team.title() == 'Blue':
	print('Welcome to team Sky. We value freedom above all and love to explore.')

elif team.title() == 'Red':
	print('You have chosen well. Welcome to team Magma. Power and raw stregth are valued above all.')

elif team.title() == 'Yellow':
	print("You chose Yellow. Very, very interesting. I think we will have much to learn from you.")

elif team.title() == 'Pink':
	print("Welcome to the team of love.")

animal = input('What animal do you relate to the most?')

def player(a, b, c):
	player_1 = [a]
	player_1.append(b)
	player_1.append(c)
	return(player_1)

player(name, team, animal)


print('Welcome ' + name.title() + ' the ' + team.title() + ' ' + animal.title() + '!')

if day == 1:
	print("Your were born on the first day of " + monconv.get(int(month)))
elif day == 2:
	print("You were born on the Seocnd day of " + monconv.get(int(month)))
elif day == 3:
	print("You were born on the third day of " + monconv.get(int(month)))
else:
	print("You were born " + (monconv.get(int(month))) + day + "th " + year + '.')

if age >= 50 and age < 100:
	print(" You are hopefully expiernced or making a career change. ")
elif age == 23 and age > 16:
	print('You must be new here. \n Let me know if you have any questions.')
elif age >= 24 and age < 50:
	print('Hopefully you like this language more than the one you are switching from. You know my favorite is binary. I I dont really like english.')
elif age <= 16 and age > 0:
	print("welp hopefully you understand this more than I do.")
else:
	print('goodluck you are ' + str(age) + ' years old.')
