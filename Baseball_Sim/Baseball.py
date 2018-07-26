#python Baseball Team
from random import *
f = '{0:<20}{1:^15}{2:>20}'
positions = ['Pitcher', 'Catcher', 'First Base', 'Second Base', 'Shortstop', 'Third Base',
	'Left Field', 'Center Field', 'Right Field', 'DH']
chrisPicks = ["Pedro Martinez", "Roger Clemens", "Yogi Berra", "Johnny Bench",
	"Lou Gehrig", "Albert Pujols", "Robinson Cano", "Rogers Hornsby", "Honus Wagner",
	"Ernie Banks", "Alex Rodriguez", "George Brett", "Ted Williams", "Barry Bonds", 
	"Willie Mays", "Ken Griffey Jr", "Hank Aaron", "Tony Gwynn", "David Ortiz"]
cP = chrisPicks[randint(0, 1)]
cC = chrisPicks[randint(2, 3)]
c1 = chrisPicks[randint(4, 5)]
c2 = chrisPicks[randint(6, 7)]
cSS = chrisPicks[randint(8, 9)]
c3 = chrisPicks[randint(10, 11)]
cLF = chrisPicks[randint(12, 13)]
cCF = chrisPicks[randint(14, 15)]
cRF = chrisPicks[randint(16, 17)]
cDH = chrisPicks[-1]
chrisTeam = [cP, cC, c1, c2, cSS, c3, cLF, cCF, cRF, cDH]

spencerPicks =["Sandy Koufax", "Rollie Fingers", "Yadier Molina", "Mike Piazza", 
	"Harmon Killebrew", "Frank Thomas", "Rod Carew", "Jackie Robinson", "Ozzie Smith",
	"Cal Ripken Jr", "Paul Molitor", "Mike Schmidt", "Goose Goslin", "Willie Stargell",
	"Kirby Puckett", "Mickey Mantle", "Babe Ruth", "Reggie Jackson", "Mike Trout"] 
sP = spencerPicks[randint(0, 1)]
sC = spencerPicks[randint(2, 3)]
s1 = spencerPicks[randint(4, 5)]
s2 = spencerPicks[randint(6, 7)]
sSS = spencerPicks[randint(8, 9)]
s3 = spencerPicks[randint(10, 11)]
sLF = spencerPicks[randint(12, 13)]
sCF = spencerPicks[randint(14, 15)]
sRF = spencerPicks[randint(16, 17)]
sDH = spencerPicks[-1]
spencerTeam = [sP, sC, s1, s2, sSS, s3, sLF, sCF, sRF, sDH]
print('{:^55}'.format("TEAMS"))
print('{0:<20}{1:>35}'.format("Chris's Team", "Spencer's Team"))
print('~' * 55)
for i in range(len(positions)):
	print(f.format(chrisTeam[i], positions[i], spencerTeam[i]))
stop = input("")