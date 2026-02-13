letra=input()
vocales="aeiouAEIOU"
if letra.islower():
    print("lowercase")
else:
    print("uppercase")
if letra in vocales:
    print("vowel")
else:
    print("consonant")