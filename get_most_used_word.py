"""
This function will take a string, "teststring", and will use a list, "punctuation" and return the most
used word in the string. It does so while using the least modules possible. There are more
effecient ways using the string library. This also includes a simple unittest at the end, to
to validate the output.
"""

teststring = "A blue shirt cost is twenty-four dollars but a white shirt is only twenty so I bought the white shirt."
punctuation = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""] # I would use the string library instead

def most_used_word(string):
    wordcount = {}
    translation_table = dict.fromkeys(map(ord, punctuation), None)
    nopunct_string = teststring.translate(translation_table) # Pulling known punctuation from string
    for word in nopunct_string.lower().split(): # Normalize text with lower, and split into a list
        if word not in wordcount: # Add list words as keys to a dictionary, and increment values
            wordcount[word] = 1
        else:
            wordcount[word] = wordcount[word] + 1
    sortlist = list([(v, k) for k, v in wordcount.items()]) # Convert to list to create a histogram/maintain order
    biggest = (0, 0) # Create tuple to hold largest word count item in
    for i in sortlist: # Iterate through tuples and update biggest variable with biggest count found
        if i[0] > biggest[0]:
            biggest = i
    return biggest[1] # Return only the word that has the largest count per the instructions

most_used_word(teststring) # Run the function



import unittest

class TestResultingWord(unittest.TestCase):
    """ Test for resulting expected word from string 'shirt'. """
    def test_word_result(self):
        result = most_used_word(self)
        self.assertEqual(result, 'shirt')

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
