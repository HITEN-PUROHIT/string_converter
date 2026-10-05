'''This project encodes and decodes messages using a simple custom algorithm.'''
import random
def random_alpha():
    a = random.randint(0,25) 
    b = random.randint(0,25)
    c = random.randint(0,25)    
    stri = "abcdefghijklmnopqrstuvwxyz"
    return stri[a] + stri[b] + stri[c]
def coding(s):
    lis_of_char = s.split()
    coded = ""
    for i in lis_of_char:
        if(len(i) == 1):
            coded = coded + " " +i
        elif(len(i) == 2):
            word = i[1]+i[0]
            coded = coded+" " +word
        elif(len(i)>2):
            word = random_alpha() + i[1:]+i[0]+random_alpha()
            coded = coded+ " "+word
    return (coded)
def decoding(s):
    lis_of_char = s.split()
    coded = ""
    for i in lis_of_char:
        if(len(i) == 1):
            coded = coded + " " +i
        elif(len(i) == 2):
            word = i[1]+i[0]
            coded = coded+" " +word
        elif(len(i)>2):
            word = i[3:-3]
            word = word[-1]+word[0:-1]
            coded = coded + " "+ word
    return coded
try:
    task = int(input("Enter 1 for coding and 2 for decoding : "))
    if(task == 1):
        message = input("Enter the message that you want to code.\n>>>>")
        print(coding(message))
    elif(task == 2):
        message = input("Enter the message that you want to decode.\n>>>>")
        print(decoding(message))
    else:
        print("Enter the correct corresponding number.")
except ValueError:
    print("Enter the valid number.")