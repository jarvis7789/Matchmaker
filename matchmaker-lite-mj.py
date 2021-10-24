# Michael Jarvis - Matchmaker Lite

# Constants

INTRO = '''

Matchmaker 2021

In the following program, you will be asked to answer a series of 5 questions
to see if you are a suitable mate. Read the question and rate how you feel by
answering with a number 1 - 5, with 5 being Strongly Agree.

'''
PERCENT = '''

            Are You Wifey Material?
'''

QUESTION = [
    'I enjoy sports',
    'Cheese is the best',
    'Wisconsin is the best state',
    'Steak is the best food',
    'I dont like 80s music'
]

DESIRED_ANSWER = [
    5,
    2,
    4,
    5,
    1
]
WEIGHTS = [
    2,
    1,
    2,
    2,
    3
]

def getAValidNumberBetween1And5():
    #UserResponse2String = str(input(("Enter a number between 1 and 5.\n")))
    #print("You entered: " + UserResponse2String)
    userResponse = str(input(QUESTION[i]))
    if not userResponse.isnumeric():
        print("This is not a number.\n")
        return -1
    else:
        #print("This is a vallid number.")
        UserResponse2Int = int(userResponse)
        if (UserResponse2Int >= 1) and (UserResponse2Int <= 5):
            #print('Your Compatibility is')
            questionCompatibility = 5 - abs(int(userResponse) - DESIRED_ANSWER[i])
            weightedScore = str(questionCompatibility * WEIGHTS[i])
            weighted.append(weightedScore)
            compatibility.append(questionCompatibility * WEIGHTS[i])
            print('Question %d compatibility: %d\n' % (i+1, questionCompatibility) )
            print('Weighted Score = ' + weightedScore )
            print('')
            return UserResponse2Int
        else:
            print("our number is not between 1 and 5")
            return -1
    response.append(userResponse)

MAX_SCORE = 10 * len(QUESTION)
print(INTRO)

# loop questions
response = []
compatibility = []
weighted = []

for i in range(len(QUESTION)):
    #userResponse = str(input(QUESTION[i]))
    number = -1 #user has not yet entered a valid number
    while(number == -1):
        number = getAValidNumberBetween1And5()
        if (number == -1):
            print("Please try again")
    #print("\nYour Compatibility Score is... " + str(compatibility))
    #print(number)
#response.append(userResponse)

#questionCompatibility = 5 - abs(int(userResponse) - DESIRED_ANSWER[i])
#compatibility.append(questionCompatibility)
#print('\nQuestion %d compatibility: %d\n' % (i+1, compatibility) )

totalCompatibility = 0
for c in compatibility:
    totalCompatibility += c

totalCompatibility *= 100 / MAX_SCORE

totalWeighted = int(weighted[0]) + int(weighted[1]) + int(weighted[2]) + int(weighted[3]) + int(weighted[4])
print('Total Weighted Score = ' + str(totalWeighted))
print(PERCENT)
print('Percent Compatible = %d' %(totalCompatibility))
if totalCompatibility <= 59:
    print("")
    print("Better Luck Next Time")
if totalCompatibility > 59 and totalCompatibility <= 79:
    print("")
    print("You're Almost there...")
if totalCompatibility > 79:
    print("")
    print("How You Doin?")



#userResponse1= int(input(QUESTION[0]))
#compatability1= 5 - abs(userResponse1 - DESIRED_ANSWER[0])
#print("")
#print("Question 1 compatability = " + str(compatability1))
#print("")

#userResponse2= int(input(QUESTION[1]))
#compatability2= 5 - abs(userResponse2 - DESIRED_ANSWER[1])
#print("")
#print("Question 2 compatibility = " + str(compatability2))
#print("")

#userResponse3= int(input(QUESTION[2]))
#compatability3= 5 - abs(userResponse3 - DESIRED_ANSWER[2])
#print("")
#print("Question 3 compatibility = " + str(compatability3))
#print("")

#userResponse4= int(input(QUESTION[3]))
#compatability4= 5 - abs(userResponse4 - DESIRED_ANSWER[3])
#print("")
#print("Question 4 compatibility = " + str(compatability4))
#print("")

#userResponse5= int(input(QUESTION[4]))
#compatability5= 5 - abs(userResponse5 - DESIRED_ANSWER[4])
#print("")
#print("Question 5 compatibility = " + str(compatability5))
#print("")

#TotalCompatibility= ((compatability1 + compatability2 + compatability3 + compatability4 + compatability5) / MAX_SCORE) * 100
#print("Are you wifey material... " + str(TotalCompatibility))
#if TotalCompatibility <= 59:
 #   print("")
  #  print("Better Luck Next Time")
#if TotalCompatibility > 59 and TotalCompatibility <= 79:
 #   print("")
 #   print("You're Almost there...")
#if TotalCompatibility > 79:
 #   print("")
  #  print("How You Doin?")
