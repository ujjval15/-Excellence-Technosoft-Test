'''Write a function in python in python, which will return maximum'''

dict = {  'ujjval': 5, 'dixit': 27, 'ankur' : 30 , 'bhumni' : 14, 'deep' : 19, 'bhavin':50, 'chirag':15 }
def key_with_maxval(dict):
    itemMaxValue = max(dict.items(), key = lambda x: x[1])
    return itemMaxValue
print(f"Max val in Dict: {key_with_maxval(dict)}")