import random

def generatePassword():
    uppercaseCharOne = chr(random.randint(65, 90))
    uppercaseCharTwo = chr(random.randint(65, 90))
    lowerCaseCharOne = chr(random.randint(97, 122))
    lowerCaseCharTwo = chr(random.randint(97, 122))
    digitOne = chr(random.randint(48, 57))
    digitTwo = chr(random.randint(48, 57))
    punctuationSignOne = chr(random.randint(33, 152))
    punctuationSignTwo = chr(random.randint(33, 152))

    password = uppercaseCharOne + uppercaseCharTwo + lowerCaseCharOne + lowerCaseCharTwo + digitOne + digitTwo + punctuationSignOne + punctuationSignTwo

    l = list(password)
    ls = random.shuffle(l)
    print(ls)
    result = ''.join(l)
    print(result)

generatePassword()