from q1 import TextAnalyzer

text = TextAnalyzer('test.txt')

words_ct = text.words_ct()
sentences_ct = text.sentences_ct()
unique_ct = text.unique_ct()
avg_length = text.avg_length()

print('Total word count: ' + str(words_ct))
print('Sentences: ' + str(sentences_ct))
print('Unique words: ' + str(unique_ct))
print('Average sentence length: ' + str(avg_length))
