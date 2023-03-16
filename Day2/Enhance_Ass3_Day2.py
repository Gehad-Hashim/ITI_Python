# --------------------Assignment [3]----------------        #fatma samy ali
"""
def list_into_dict(str):
    str=str.split(' ')
    d = {str[0][0]: str[0], str[1][0]: [str[1]], str[2][0]: [str[2]]}
    print(d)

userInput =input('enter input : ')
list_into_dict(userInput)

"""


# --------------------Enhancing Assignment [3]----------------          fatma samy ali aliaa badr
def list_into_dict(str):
    str = str.split(' ')
    d = {}
    for ind, val in enumerate(str):
        #  dd = {str[ind][0]: str[ind]}
        dd = {val[0]: val}
        d.update(dd)
    print(d)


userInput = input('enter input : ')
list_into_dict(userInput)
