test1 = "1Abc __1__ defg __2__ hijk __3__ lmno __4__"
test2 = "2Abc __1__ defg __2__ hijk __3__ lmno __4__"
test3 = "3Abc __1__ defg __2__ hijk __3__ lmno __4__"

answerlist = ["function", "variable", "class", "object"]

difficulty = ""


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
    tests = []
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
    blank = "__1__"
    current_test = test.pop()
    sentence = str(current_test)
    for word in sentence.split():
        if word.startswith(blank):
            print(current_test, word)
            answer = get_answer()
            blank = replace_word(answer, answerlist)
            print(current_test)


def replace_word(user_answer, answerlist):
    for ans_list in answerlist:
        if ans_list in user_answer:
            return ans_list
    return None

print(test(pick_tests(get_difficulty())))
