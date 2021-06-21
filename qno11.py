# words = "navgurukul is great"
# counter = 0
# while counter < len(words):
#     print (words[counter]) 
#     counter+=1


def break_into_words(sentence):
    a=[]
    b=""
    for i in sentence:
        if i==" ":
            a.append(b)
            b=" "
        else:
            b+=i
    if b :
        a.append(b)
    print(a)

break_into_words("NavGurukul is an alternative to higher education reducing the barriers of current formal education system")
