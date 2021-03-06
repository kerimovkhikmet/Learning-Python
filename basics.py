import random


def addstr(str):
    return '"Hello, ' + str + '!"'


# userStr = input("Enter some string: ")
userStr = "world"
print(addstr(userStr), "\n")


def sum(numList):
    sum = 0
    for num in range(len(numList)):
        sum += numList[num]
    return sum


def multiply(numList):
    prod = 1
    for num in range(len(numList)):
        prod *= numList[num]
    return prod

# def userInput():
#     userNum = []
#     num = int(input("Enter number of elements : "))
#     for i in range(0, num):
#         elem = int(input())
#         userNum.append(elem)
#     return userNum

# userNum = userInput()


userNum = [1, 5, 3, 4]


print(sum(userNum), "\n")
print(multiply(userNum), "\n")


def revStr(str):
    stringlength = len(str)
    slicedString = str[stringlength::-1]
    return slicedString


print(revStr(userStr), "\n")


def isPalindrome(str):
    for i in range(0, len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


userPal = "devopspoved"
res = isPalindrome(userPal)

if (res):
    print("True\n")
else:
    print("False\n")


def histogram(numList):
    chart = ""
    for i in range(len(numList)):
        chart += numList[i] * "*" + "\n"
    return chart


print(histogram(userNum), "\n")


def caesarCipher(str, key):
    result = ""
    for i in range(len(userStr)):
        char = userStr[i]
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result


# userStr = input("Enter some string to cipher: ")
# userKey = input("Enter key to shift: ")
userStr = "vwxyz"
userKey = 5

print("Text  : " + userStr)
print("Shift : " + str(userKey))
print("Cipher: " + caesarCipher(userStr, userKey) + "\n")


def diagonalReverse(arr):
    new_arr = []
    rows = len(arr)
    cols = len(arr[0])
    new_arr = [[None for i in range(rows)] for j in range(cols)]
    for i in range(rows):
        for j in range(cols):
            new_arr[j][i] = arr[i][j]
    return new_arr


userArr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonalReverse(userArr), "\n")


def game(num1, num2):
    value = random.randint(int(num1), int(num2))
    userNum = int(input("Enter number to guess: "))
    while userNum != value:
        if userNum < value:
            print("Your guess is low!")
            userNum = int(input("Enter another number to guess: "))
        elif userNum > value:
            print("Your guess is high!")
            userNum = int(input("Enter another number to guess: "))
        else:
            print("You guess is right, congratulations!")
            # why doesn't prints on screen?
            break
    return value


# num1 = input("Enter start number: ")
# num2 = input("Enter finish number: ")
# print(game(num1, num2))
# print("\n")


def bracketsCheck(str):
    pairs = {"[": "]"}
    stack = []
    for ch in str:
        if ch in "[":
            stack.append(ch)
        elif stack and ch == pairs[stack[-1]]:
            stack.pop()
        else:
            return "Not OK"
    return "OK"


test_cases = ("[[[]]]", "[[[]]]]", "[[[[[[]]]]]]]]", "[[]]", "[]][[]")
for str in test_cases:
    print(str, bracketsCheck(str))
print("\n")


def charFreq(str):
    all_freq = {}
    for i in str:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq


print(charFreq("abbabcbdbabdbdbabababcbcbabc"), "\n")


def decToBin(num):
    if num > 1:
        decToBin(num // 2)
    print(num % 2, end=" ")


decToBin(23)
print("\n")
