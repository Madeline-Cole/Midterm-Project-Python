print(
    "Full Name: Madeline Cole \nEmail: Mec399@miami.edu \nCourse: Python Programming For Everyone \nMajor: Biochemistry & Molecular Science\n")
# displays my full name, email, course, major in the first 4 lines of the output

print("Enter The Starting Number of Organisms:")
organisms = int(input())
# asks the user to enter the starting number of organisms and assigns the input to the integer "organism"

while organisms <= 0:
    print("Please Enter a Positive Number For The Starting Number of Organisms:")
    organisms = int(input())
    # checks to see if the number is negative and then asks for a new input

print("Enter The Average Daily Population Increase (as a percentage, for example 30 = 30%):")
average = int(input())
# asks the user to enter the average daily population increase and assigns the input to the integer "average"

while average <= 0 or average > 100:
    print("Please Enter a Positive Number Within 1-100 For The Average Daily Population Increase:")
    average = int(input())
    # checks to see if both instances occur then asks for a valid input

increase = (average / 100) + 1
# converts the whole number into a percentage to be used in the loop

print("Enter The Number of Days The Organisms Will Be Left To Multiply:")
days = int(input())
# asks the user the number of days the organisms will be left to multiply and assigns the input to the integer "days".
while days <= 0 or days > 30:
    print("Please Enter a Positive Number No Greater Than 30:")
    days = int(input())
    # checks to see if both instances occur then asks for a valid input
numbers = 1
# this variable is for the number of days that go under the title "Day Approximate"

print("\nDay Approximate        Population")
# prints the heading for the table of information

while days > 0:
    print(numbers, ".                   ", organisms)
    # prints out the information everytime the loop starts
    organisms = organisms * increase
    # increases the population by the given average increase of population
    days -= 1
    # makes the loop stop when it has given the information for the number of days the user inputs
    numbers += 1
    # increases the numbers of days on the left by one to indicate which days are which


#for eachDay in range (days):
   # print(eachDay+1, ".                   ", organisms)
    # prints out the information everytime the loop starts
    #organisms = organisms * increase


# !!! Trashed Code !!!

# days_approximate = 1
# count = days
# while(count != days_approximate):
# print(days_approximate,".", organisms)
# days_approximate += 1
# days -= 1
# organisms = organisms * increase

# while(average <= 0):
# print("Please Enter a Positive Number For The Average Daily Population Increase:")
# average = int(input())
# checks to see if the number is negative and then asks for a valid input
# while(average > 100):
# print("Please Enter a Number Within 1-100 For The Average Daily Population Increase:")
# average = int(input())
# checks to see if the number is no greater than 100 and then asks for a valid input




