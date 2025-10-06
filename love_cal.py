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

    for item in name2.upper():
        if item in word1:
            count+= 1
        if item in word2:
            count2+= 1

    love_score = str(count) + str(count2)
    print(love_score)

print("Welcome to love Calculator....")
print("Let's calculate your score 💖")

name1 = input("Enter your first name: ")
name2 = input("Enter your partner's name: ")

calculate_love_score(name1, name2)