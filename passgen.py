import random
import string


print('passwort :')
print(''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation , k=16)))










# print(random.choices(string.ascii_uppercase))

# uppercaseLetter=chr(random.randint(65,90))
# uppercaseLetterSec=chr(random.randint(65,90))
# lowercaseLetter=chr(random.randint(97,122))
# lowercaseLetterSec=chr(random.randint(97,122))
# digits1=random.randint(0,200)
# digits2=random.randint(0,200)