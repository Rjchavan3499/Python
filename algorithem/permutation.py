def permute(s, sen):
    if (len(s) == 0):
        print(sen, end=" ")
        return

    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, sen + ch)


sen = ""
s = input("Enter the string : ")
print("All possible strings are : ")
permute(s, sen)

