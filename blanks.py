import numpy
import scipy
import matplotlib


# Predefined tests section
test1 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
test2 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
test3 = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# Predefined answers dictionary. I decided on dictionary to exercise that knowledge, and because it seemed appropriate.
testanswers = ["function", "values", "none", "list"]

def setup_game():
    number_of_games = None
    while number_of_games == None:
        try:
            number_of_games = "easy" #input("What difficulty? Type easy, medium or hard. q to quit: ").lower()
            while number_of_games not in ["easy", "medium", "hard", "q"]:
                number_of_games = number_of_games = \
                    input("What difficulty? Type easy, medium or hard. q to quit: ").lower()
        except:
            print("Unexpected input, press q to quit or type easy, medium, or hard.")
    if number_of_games == "q":
        print("Bye!")
        exit(0)
    elif number_of_games == "easy":
        tests = [test1]
        return tests
    elif number_of_games == "medium":
        tests = [test1, test2]
        return tests
    elif number_of_games == "hard":
        tests = [test1, test2, test3]
        return tests
    else:
        print("I don't know what to do!")

def word_replace(word, answer_list):
    for answer in answer_list:
        if answer in word:
            return answer
    return None

def get_answer(blank_number):
    print("What is your answer for ", blank_number, "?")
    try:
        useranswer = input("")
        int(useranswer)
    except:
        print("Huh")

def get_tests():


def start_test():
    tests = setup_game()
    test_current = tests.pop()
    print(test_current)
    answer1 = get_answer(1)
    seperate_string = test_current.split()
    for word in seperate_string:
        replacement = word_replace(answer1, testanswers)
        if replacement != None:
            u





start_test()


# # Checks if a word in parts_of_speech is a substring of the word passed in.
# def word_in_pos(word, parts_of_speech):
#     for pos in parts_of_speech:
#         if pos in word:
#             return pos
#     return None
#
#
# # Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# # which appear in parts_of_speech with their own words.
# def play_game(ml_string, parts_of_speech):
#     replaced = []
#     ml_string = ml_string.split()
#     for word in ml_string:
#         replacement = word_in_pos(word, parts_of_speech)
#         if replacement != None:
#             user_input = raw_input("Type in a: " + replacement + " ")
#             word = word.replace(replacement, user_input)
#             replaced.append(word)
#         else:
#             replaced.append(word)
#     replaced = " ".join(replaced)
#     return replaced
#
#
# print
# play_game(test_string1, parts_of_speech1)
