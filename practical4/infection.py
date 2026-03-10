#Pseudocode:
#1. Define the total population size (n = 91).
#2. Define the initial number of infected individuals (starting at 5).
#3. Define the growth rate (40% or 0.4).
#4. Initialize a counter for the current day (Day 1).
#5. Use a 'while' loop that runs as long as the infected count is less than the total population.
#6. Inside the loop:
#    a. Increment the day counter.
#    b. Update the number of infected students based on the growth rate.
#    c. Print the status for the current day.
#7. After the loop, print the total number of days taken to infect everyone.

#Initialize starting variables
total_students = 91
infected = 5
growth_rate = 0.4
day = 1

#Print initial status for Day 1
print("Day", day, ": Infected =", infected)

#Loop until all students are infected
while infected < total_students:
    day = day + 1
    infected = infected + ((infected * growth_rate))
    if infected > total_students:
        infected = total_students
    #print the status for the current day
    print("Day", day, ": Infected =", int(infected))

#report the total number of days taken to infect everyone
print("It takes", day, "days to infect all students in IBI class.")