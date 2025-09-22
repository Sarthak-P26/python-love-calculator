def calculate_love_score(name1,name2):
    word1 = "TRUE"
    word2 = "Love"
    count = 0
    count2 = 0

    for item in name1.upper():
        if item in word1:
            count+=1
        if item in word2:
            count2+= 1