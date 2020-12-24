'''Question1:
Use python lists and make an list of numbers.
Write a function which returns sum of the list of numbers'''


list=[1,5,10,7,3]

def sum(list):
    total = 0
    for x in list:
        total += x
    return total
print(f"sum of the list of numbers is: {sum(list)}")

