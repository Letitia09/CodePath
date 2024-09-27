def is_acronym(words, s):
    acr = ""
    for i in range(len(words)):
        acr += words[i][0]
    if acr == s:
        print(True)
    else:
        print(False)
words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)
