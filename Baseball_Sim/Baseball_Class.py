import random, sys, pygame, time, math

def main():
	availableNumbers = [number for number in range(1, 100)]
	random.shuffle(availableNumbers)	
	firstNames, lastNames = createPlayerNameLists("male_first.txt", "all_last.txt")
	states, animals = createTeamNameLists("States.txt", "animals.txt")
	print(states)
	#game = Game()
	t1 = Team()
	#t2 = Team()
	print(t1._name)

#The following two functions read text files and randomize names from them
def createTeamNameLists(stateFile, animalFile):
	states = []
	animals = []
	infile = open(stateFile, 'r')
	for line in infile:
		line.strip()
		states.append(line)
	infile.close()
	infile = open(animalFile, 'r')
	for line in infile:
		line.strip()
		animals.append(line)
	infile.close()
	return states, animals	
def createPlayerNameLists(firstFile, lastFile):
	firstNamesList = []
	lastNamesList = []
	infile = open(firstFile, 'r')
	for line in infile:
		line = line.split()
		firstName = line[0]
		firstNamesList.append(firstName.title())
	infile.close()	
	infile = open(lastFile, 'r')
	for line in infile:
		line = line.split(' ')
		lastName = line[0]
		lastNamesList.append(lastName.title())
	infile.close()
	return firstNamesList, lastNamesList
#Experimenting with PyGame graphics
def graphics():
	black = 0, 0, 0
	brown = (160, 97, 46)
	green = (112, 142, 55)
	white = (255, 255, 255)
	screen = pygame.display.set_mode((600,600))
	screen.fill(green)
	pygame.draw.lines(screen, white, False, [(5, 280), (300,575), (595,280)], 5)
	pygame.display.update()
	pygame.quit()
#Prints player information for each team
def displayTeams(team1, team2):
	print('{:^80}'.format("Rosters"))
	print('{:^80}'.format("TEAM 1"))
	for player in team1:
		print(player,'\n')
	print('{:^80}'.format("TEAM 2"))
	for player in team2:
		print(player, '\n')

class Game:
	def __init__(self):
		self._score = (0,0)
		self._inning = (1, True)
		self._balls = 0
		self._strikes = 0
		self._runnersOn = (0)
#5% chance of hit per pitch = .150 avg
#10.7% chance of hit per pitch = .365 avg
class AtBat:
	def __init__(self, index, tBat, tField):
		self._strikes = 0
		self.balls = 0
		self.batter = tBat.index
		self.pitcher = tField._pitcher

class Player:
	def __init__(self):
		self._name = self.createPlayerName(firstNames, lastNames)
		self._number = availableNumbers.pop()
		self._throwing = random.randint(50, 100)
		self._fielding = random.randint(50, 100)
		self._contact = random.randint(50, 100)
		self._power = random.randint(50, 100)
		self._speed = random.randint(50, 100)
	def createPlayerName(self, firstNamesList, lastNamesList):
		playerName = str(firstNamesList[random.randint(0,len(firstNamesList))] + ' ' +
			lastNamesList[random.randint(0, len(lastNamesList))])
		return playerName
	def __str__(self):
		return ("Name: " + str(self._name)
			+ "\nNumber: " + str(self._number)
			+ "\nThrowing: " + str(self._throwing)
			+ "\nFielding: " + str(self._fielding)
			+ "\nContact: " + str(self._contact)
			+ "\nPower: " + str(self._power)
			+ "\nSpeed: " + str(self._speed))
		
class Team:
	def __init__(self):
		self._name = self.createTeamName(states, animals)
		self._roster = []
		self._pitcher = -1
		self._maxThrowing = 0
		for i in range (9):
			p = Player()
			self._roster.append(p)
			if p._throwing > self._maxThrowing:
				self._maxThrowing = p._throwing
				self._pitcher = p 
	def createTeamName(self, states, animals):
		state = states[random.randint(0,len(states))]
		animal = animals[random.randint(0, len(animals))]
		teamName = "The " + str(state) + ' ' + str(animal) + 's'
		teamName = ''.join(teamName.splitlines())
		return teamName
	
	def __str__(self):
		pass

class Fielder:
	def __init__(self):
		self._position = ''

			
			
			
#displayTeams(*createTeams())


main()

