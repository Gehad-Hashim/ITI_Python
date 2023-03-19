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
"""
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
"""

# ------------------------------------------- calculate area ------
def calArea(name, num1, num2):
    pi = 3.14
    if name == 'tri':
        return 0.5 * num1 * num2
    if name == 'rect':
        return num1 * num2
    if name == 'sq':
        return num1 ** 2
    if name == 'cir':
        return pi * num1 ** 2
    else:
        return 'not found'


print('tri:', calArea('tri', 4, 5))
print('rect', calArea('rect', 4, 5))
print('sq', calArea('sq', 4, 0))
print('cir', calArea('cir', 4, 0))