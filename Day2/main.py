print('hello day 2')
# --------------------Assignment [1]----------------
"""
statement =input('string : ')
letter=input('letter : ')
for index,char in enumerate(statement):
    if char ==letter:
        print([index],end=' ')

"""
# --------------------Assignment [2]----------------
"""
num = int(input('enter a number : '))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print([i * j], end='')
"""

# --------------------Assignment [3]----------------
"""
def list_into_dict(str):
    str=str.split(' ')
    print(str, type(str))
    print(str[0:2])
    d = {str[0][0]: str[0], str[1][0]: [str[1]], str[2][0]: [str[2]]}
    print(d)


userInput =input('enter input : ')
list_into_dict(userInput)

#fatma samy ali
"""


# --------------------Enhancing Assignment [3]----------------
def list_into_dict(str):
    str = str.split(' ')
    d = {}
    for ind,val in enumerate(str):
      #  dd = {str[ind][0]: str[ind]}
        dd = {val[0]: val}
        d.update(dd)
    print(d)

userInput = input('enter input : ')
list_into_dict(userInput)
