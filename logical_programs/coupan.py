import random
import string

CODE_COUNT = int(input("how many times you want to generate the numbers"))

CODE_LEN  = int(input("enter the length"))


def strall():
    return (string.ascii_letters + string.digits)


def codeGen():
    CodeSet = set()

    while len(CodeSet) < CODE_COUNT:
        code = ''.join([random.choice(strall()) for i in range(CODE_LEN)])

        CodeSet.add(code)

    return CodeSet


if __name__ == '__main__':
    print(codeGen())