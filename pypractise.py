'''
def SwitchFunction(val):
    dictionary = {1:"Turky",2:"Maleshiya",3:"Newzeland"}
    if val in dictionary:
        return dictionary[val]
    else:
        return "No place found ?"
value = int(input("Where you want to go enter number 1/3 : "))


def main():
    print(SwitchFunction(value))

if __name__ == "__main__":
    main()
'''

'''
def adder(*num):
    sum = 0
    for n in num:
        sum += n
    return sum
def main():
    print(adder(3,2,15,3,100))
if __name__ == "__main__":
    main()
'''
