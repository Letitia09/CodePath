def merge_alternately(word1, word2):
    def summ(length):
        sum1 = ""
        for i in range(length):
            sum1 = sum1 + word1[i] + word2[i]
        return sum1
    if len(word1)>len(word2):
        print(summ(len(word2)) + word1[len(word2):])
    else:
        print(summ(len(word1)) + word2[len(word1):])
        
word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)
