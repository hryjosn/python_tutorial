letters = "cdefghijlmnoqstuvxz"


def unHash(hashedNum):
    result = ""
    while hashedNum > 7:
        result +=letters[hashedNum % 23]
        hashedNum = int((hashedNum - hashedNum % 23) / 23)
    print(result[::-1])

def hash(str):
    h = 7
    for i in str:
        h = h * 23 + letters.index(i)
    return h


print(hash("ilovecoding"))
print(unHash(6933552791181934))
