import string

text = input("Please enter a sentence: ")
shift = 5 #Shifts every letter in the given string 

alphabet = string.ascii_lowercase #Shifted version of the alphabet
shifted =  alphabet[shift:] + alphabet[:shift] #shifts the letters and appends the remaining letters at a certain index
table = str.maketrans(alphabet, shifted) #translates the alphabet into the shifted alphabet (encrytion)

encrypt = text.translate(table)
print(encrypt)
