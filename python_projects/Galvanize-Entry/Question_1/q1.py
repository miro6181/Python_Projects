"""Technical Exercise Question 1 written in Atom
Author: Michael Rogers


DIRECIONS TO TEST THE CODE:

AT THE BOTTOM OF THIS FILE THERE IS AN INSTANTIATION AND TEST OF THE CODE.
YOU CAN EITHER REPLACE THE 'test.txt' IN THE INSTANTIATION WITH YOUR OWN TEST
FILE OR CREATE A FILE NAMED 'test.txt'.
THE TEST FILE I USED HAS THE FOLLOWING:

This is a file in the test file.
It has 40 words, 2 sentences, and 28 unique words to test the technical exercise.
Third line
Fourth line
Fifth line
Sixth line
Seventh line
Eighth line
Ninth line
Tenth line
etc.

IMPORTANT: BOTH THE 'q1.py' FILE AND THE TEST FILE MUST BE IN THE SAME DIRECTORY
FOR THE CODE TO EXECUTE PROPERLY. OR YOU MUST PUT THE FILE PATH IN THE
INSTANTIATION. """

# Create a text content analyzer. This is a tool used by writers to find statistics such as word and sentence count on essays or articles they are writing.
# Write a Python program that analyzes input from a file and compiles statistics on it.
# The program should output:
# 1. The total word count
# 2. The count of unique words
# 3. The number of sentences
# Example output:
#
# Total word count: 468
# Unique words: 223
# Sentences: 38
# Brownie points will be awarded for the following extras:
# 1. The ability to calculate the average sentence length in words
# 2. The ability to find often used phrases (a phrase of 3 or more words used over 3 times)
# 3. A list of words used, in order of descending frequency
# 4. The ability to accept input from STDIN, or from a file specified on the command line.
# This question should be written in Python.

class TextAnalyzer:
    def __init__(self, filename):
        self.filename = filename
    # Returns the the total word count.
    def words_ct(self):
        word_ct = 0
        with open(self.filename) as in_file:
            for line in in_file:
                word_ct += len(line.split())
        return word_ct
    # Returns the the total number of sentences.
    def sentences_ct(self):
        sentence_ct = 0
        with open(self.filename) as in_file:
            for line in in_file:
                sentence_ct += line.count('.')
        return sentence_ct
    # Returns the total number of unique words.
    def unique_ct(self):
        with open(self.filename) as in_file:
            unique_words = set(in_file.read().split())
        return len(unique_words)
    # Returns the the average length of the sentences.
    def avg_length(self):
        word_counts = []
        with open(self.filename) as in_file:
            text = in_file.read()
            sentences = text.split('.')
            for sentence in sentences:
                words = sentence.split()
                word_counts.append(len(words))
            average_word_count = sum(word_counts)/self.sentences_ct()
        return average_word_count

if __name__ == '__main__':
    TextAnalyzer(__name__)



# This is the instantiation and test.

text = TextAnalyzer('test.txt')

words_ct = text.words_ct()
sentences_ct = text.sentences_ct()
unique_ct = text.unique_ct()
avg_length = text.avg_length()

print('Total word count: ' + str(words_ct))
print('Sentences: ' + str(sentences_ct))
print('Unique words: ' + str(unique_ct))
print('Average sentence length: ' + str(avg_length))
