def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    cr_vowel = [i for i in s if i in vowels][::-1]
    concat = ""
    ind = 0
    for i in range(len(s)):
        if s[i] in vowels:
            concat = concat + cr_vowel[ind]
            ind += 1
        else:
            concat += s[i]
    print(concat)

s = "robin"
reverse_vowels(s)

s = "BATgirl"
reverse_vowels(s)

s = "batman"
reverse_vowels(s)


