# Take a sentence from user and count its words
Sentence = input("Please Enter a sentence:  ")  # take sentence from user
word_count = Sentence.count( ' ' ) + 1          # count spaces and 1 beacuse index starts with 0
print ("Total Number of Words in Given Sentence are:  " , word_count)  # print statement