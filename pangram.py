def is_pangram(sentence):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in sentence.lower():
            return False
    return True

# test = "qwertyuiolkjhgfdsazxcvvbnm"
# def panderin(test):
#     for i in "qwertyuiopasdfghjklzxcvbnm":
#         if i not in sentence:
#             print(i)
#             return False
#     return True
