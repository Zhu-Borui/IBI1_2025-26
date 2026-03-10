# What does this piece of code do?
# Answer: the code draws 11 random numbers between 1 and 9, sums them up, and prints the total.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:
	#It means progress = progress + 1
	#It indicates that the loop will run 11 times, as progress starts at 0 and increments by 1 until it reaches 10.
	progress+=1
	#draw a random number between 1 and 10, and add it to total_rand.
	#however, 10 is not included, so the random number will be between 1 and 9.
	n = randint(1,10)
	total_rand+=n
#After the loop, total_rand will contain the sum of 11 random numbers drawn between 1 and 9.
print(total_rand)

