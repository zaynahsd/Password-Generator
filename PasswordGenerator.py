import random
import string

x = int(input("How many characters do you want your password to be?: "))

a = int(input("Which attributes do you want? Enter the number corresponding to your choice. \n1 Only Uppercase characters \n2 Only Lowercase characters \n3 Only Digits \n4 Only Punctuation \n5 Uppercase + Lowercase \n6 Uppercase + Digits \n7 Uppercase + Symbols \n8 Uppercase + Lowercase + Digits \n9 Uppercase + Lowercase + Symbols  \n10 Uppercase + Digits + Symbols \n11 Lowercase + Digits \n12 Lowercase + Symbols \n13 Lowercase + Digits + Symbols \n14 Digits + Symbols \n15 All of the above: "))

if a == 1:
    print("Password: " + ''.join(random.choice(string.ascii_uppercase) for i in range(x)))
elif a == 2:
    print("Password: " + ''.join(random.choice(string.ascii_lowercase) for i in range(x)))
elif a == 3:
    print("Password: " + ''.join(random.choice(string.digits) for i in range(x)))
elif a == 4:
    print("Password: " + ''.join(random.choice(string.punctuation) for i in range(x))) #the first 4 attributes

elif a == 5:
    print("Password: " + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(x)))
elif a == 6:
    print("Password: " + ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(x)))
elif a == 7:
    print("Password: " + ''.join(random.choice(string.ascii_uppercase + string.punctuation) for i in range(x)))
elif a == 8:
    print("Password: " + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(x)))
elif a == 9:
    print("Password: " + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation) for i in range(x)))
elif a == 10:
    print("Password: " + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for i in range(x))) #uppercase attributes

elif a == 11:
    print("Password: " + ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(x)))
elif a == 12:
    print("Password: " + ''.join(random.choice(string.ascii_lowercase + string.punctuation) for i in range(x)))
elif a == 13:
    print("Password: " + ''.join(random.choice(string.ascii_lowercase + string.digits + string.punctuation) for i in range(x))) #lowercase attributes

elif a == 14:
    print("Password: " + ''.join(random.choice(string.digits + string.punctuation) for i in range(x))) #digits


else:
    print("Password: " + ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for i in range(x)))










