vowels = 'aeiou'
#
# def pig_latin(s):
#     sentence = []
#     for word in s.split(' '): #splits sentence into array of words
#         for counter, letter in enumerate(vowels): #compares first letter each word
#             if word[0].lower() == letter: #if first letter is = to vowel
#                 word = word + 'ay'
#                 # sentence.append(word)
#                 print(word)
#             else:
#                 word = word + word[0] + 'ay'
#                 # split_word = [a for a in word]
#                 # split_word.pop(0)
#                 # "".join(split_word)
#                 # # sentence.append(split_word)
#                 # print(split_word)
#                 print(word)
#
# pig_latin('this is a sample sentence')

def translator():
    print("Type a word and translate it to piglatin!")
    s = input("Translate: ")
    if(s[0] in vowels):
        s = s + 'ay'
        print(s)
    else:
        s = s + s[0] + 'ay'
        arrayed_s = [letter for letter in s]
        arrayed_s.pop(0)
        s = "".join(arrayed_s)
        print(s)


translator()
