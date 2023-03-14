# ----------------------------- Assign [1] -------------
"""
word = input('enter a word : ')
# print(word)

for letter in word:
    if letter in ['o', 'e', 'i', 'u', 'a']:
        continue
    print(letter, end='')
print("""
""")
"""
# ---------------------------------- Assign [2] -------------
"""
x = int(input('enter a number : '))

for i in range(1, x + 1):
    print(' ' * (x - i), '*' * i)
    
"""
#-------------------------- Bonus -----------------------
def skip_vowel(anyWord):
    for letter in anyWord:
        if letter in ['o', 'e', 'i', 'u', 'a']:
            continue
        print(letter, end='')

skip_vowel('gehad hashim')  # calling function
print(type(skip_vowel))