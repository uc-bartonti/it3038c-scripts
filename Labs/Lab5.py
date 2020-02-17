def WordCount():
    vowels = ['a','e','i','o','u']
    vowelCount = 0
    consonantCount = 0
    letterCount = 0
    print('Enter a word here.')
    word = input()
    word = word.lower()
    print(word)
    for letter in word:
        if letter in vowels:
            vowelCount = vowelCount + 1
        else:
            consonantCount = consonantCount + 1
    for letter in word:
        letterCount = letterCount + 1
    print('your word contains %d letters' % letterCount)
    print('your word vowel count is %d' % vowelCount)
    print('your word consonant count is %d' % consonantCount)
WordCount()
