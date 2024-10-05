def are_equivalent(word1, word2):
    word1 = "".join(word1)
    word2 = "".join(word2)
    if word1 == word2:
        print(True)
    else:
        print(False)
word1 = ["bat", "man"]
word2 = ["b", "atman"]
are_equivalent(word1, word2)

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
are_equivalent(word1, word2)

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
are_equivalent(word1, word2)
