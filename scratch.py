test1 = "1Abc __1__ defg __2__ hijk __3__ lmno __4__"
test2 = "2Abc __1__ defg __2__ hijk __3__ lmno __4__"
test3 = "3Abc __1__ defg __2__ hijk __3__ lmno __4__"

answers = ["function", "variable", "class", "object"]

difficulty = ""

tests = []

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

def pick_tests(difficulty):
    tests = []
    if difficulty == "easy":
        tests = [test1]
    elif difficulty == "medium":
        tests = [test1, test2]
    elif difficulty == "hard":
        tests = [test1, test2, test3]
    return tests



print(pick_tests(get_difficulty()))
