word1 = input("Введіть перше слово: ").lower()
word2 = input("Введіть друге слово: ").lower()

if len(word1) != len(word2):
    print("Це не анаграми")
else:
    letters1 = {}
    letters2 = {}

    for letter in word1:
        if letter in letters1:
            letters1[letter] += 1
        else:
            letters1[letter] = 1

    for letter in word2:
        if letter in letters2:
            letters2[letter] += 1
        else:
            letters2[letter] = 1

    if letters1 == letters2:
        print("Це анаграми")
    else:
        print("Це не анаграми")