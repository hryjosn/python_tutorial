letters = "cdefghijlmnoqstuvxz"
def reverseHash(hash):
    print(hash)
def hash(str):
    h = 7
    for i in str:
        print('i:',i)
        h = h * 23 + letters.index(i);
        print(h)
        print(letters.index(i))
    return h

print(hash("ju"))
# print(reverseHash(6933552791181934))