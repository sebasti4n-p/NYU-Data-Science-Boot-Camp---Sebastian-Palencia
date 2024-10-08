def count_vowels(word):
    vowel_count = 0
    the_vowels = ['a','e','i','o','u']
    for letter in word:
        if letter in the_vowels:
            vowel_count += 1
    return vowel_count

print(count_vowels('aerial'))