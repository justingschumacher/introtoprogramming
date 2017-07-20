 # IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

# Importing random to allow for the easy random selection from a sample
import random

# Predefined tests section
test1 = "The __1__, __2__"
test2 = "The __3__, __4__"
test3 = "The __5__, __6__"
test4 = "The __7__, __8__"
test5 = "The __9__, __10__"

# Predefined answers dictionary. I decided on dictionary to exercise that knowledge, and because it seemed appropriate.
test1answers = {1: 'a', 2: 'b'}
test2answers = {3: 'c', 4: 'd'}
test3answers = {5: 'e', 6: 'f'}
test4answers = {7: 'g', 8: 'h'}
test5answers = {9: 'i', 10: 'j'}

# Lists and variables for defining, selecting and managing number of games
tests = [test1, test2, test3, test4, test5]
testsSelected = []
testsCompleted = []
number_of_games = None


# This will get the information to start the game
def setup_game():
    answertest = False #First, get the number of games to play from a random pool of games, and validate input
    while answertest is False:
        number_of_games = 3  # raw_input("How many games do you want to play? Choose 1-3, or q to quit: " )
        try:
            if number_of_games.startswith("Q") or number_of_games.startswith("q"):
                print("Bye!")
                break
        except:
            if isinstance(number_of_games, str): #int(number_of_games):
                print("Choose 1-3, or q to quit")
                setup_game()
            else:
                answertest = True
                testsSelected = random.sample(tests, number_of_games)
                return testsSelected


userinput = "a"  # raw_input("What is the answer to blank " + iterator + "?")
testanswer = test1answers
#print(word_in_list(userinput, testanswer))

# This will find the word in the answers dictionary and provide feedback
def word_in_list(response, testanswer):
    pass

def fill_in_the_blanks(questions, answers):
    pass


def start_test(tests, testanswer):
    currenttest = []
    currenttest = tests[0]
    testquestions = [int(s) for s in tests[0] if s.isdigit()]
    print(testquestions)
    iterator = 1 #raw_input("What is the answer to blank " + testquestions[0] + "?"
    response = 1
    for k, v in testanswer.items():
        if k is iterator:
            if response is v:
                print("correct!")
            else:
                print("incorrect")
    print(currenttest)
    print(tests)

# Select the test, ask for answer, while answer is false retry. When all questions are correct list.remove(test)

start_test(setup_game(), testanswer)