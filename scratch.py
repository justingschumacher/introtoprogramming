test1 = "1Abc __1__ defg __2__ hijk __3__ lmno __4__"
test2 = "2Abc __1__ defg __2__ hijk __3__ lmno __4__"
test3 = "3Abc __1__ defg __2__ hijk __3__ lmno __4__"

answerlist = ["function", "variable", "class", "object"]


def get_answer():
    user_answer = input("What is your answer? ")
    return user_answer


def get_difficulty():
    difficulty_choices = ["easy", "medium", "hard"]
    difficulty = input("Easy, Medium or Hard? ")
    difficulty = difficulty.lower()
    while difficulty not in difficulty_choices:
        try:
            print("Invalid input, try again.")
            difficulty = input("Easy, Medium or Hard? ")
            difficulty = difficulty.lower()
            if difficulty in ["easy", "medium", "hard"]:
                return difficulty
        except:
            print("Not an expected input, goodbye")
            break
    return difficulty


def pick_tests(difficulty):
    if difficulty == "easy":
        tests = [test1]
        return tests
    elif difficulty == "medium":
        tests = [test1, test2]
        return list(map(lambda x: x, tests))
    elif difficulty == "hard":
        tests = [test1, test2, test3]
        return list(map(lambda x: x, tests))


def test(test):
    replaced = []
    blank = "__1__"
    current_test = test.pop()
    current_test = current_test.split()
    for word in current_test:
        answer = get_answer()
        replacement = replace_word(answer, answerlist)
        if replacement != None:
            answer = get_answer()
            word = word.replace(replacement, answer)
            replaced.append(word)
        else:
            replaced.append(word)
        # if i.startswith(blank):
        #     print(blank, "  ", current_test)
        #     blank = replace_word(get_answer(), answerlist)
        #     print(blank, "  ", current_test)


def replace_word(user_answer, answerlist):
    for ans_list in answerlist:
        if ans_list in user_answer:
            return ans_list
    return None


print(test(pick_tests(get_difficulty())))


# ## A list of replacement words to be passed in to the play game function.
# parts_of_speech1  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN", "NAME", "VERB", "OCCUPATION", "ADJECTIVE"]
#
# # The following are some test strings to pass in to the play_game function.
# test_string1 = "Hi, my name is NAME and I really like to VERB PLURALNOUN. I'm also a OCCUPATION at PLACE."
# test_string2 = """PERSON! What is PERSON going to do with all these ADJECTIVE PLURALNOUN? Only a registered
# OCCUPATION could VERB them."""
# test_string3 = "What a ADJECTIVE day! I can VERB the day off from being a OCCUPATION and go VERB at PLACE."
#
# # Checks if a word in parts_of_speech is a substring of the word passed in.
# def word_in_pos(word, parts_of_speech):
#     for pos in parts_of_speech:
#         if pos in word:
#             return pos
#     return None
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
# print play_game(test_string1, parts_of_speech1)