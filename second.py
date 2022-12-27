import random

def sayac(list):
    a = random.randint(1,6)
    
    if(a==1):
        list[0]+=1
    if(a==2):
        list[1]+=1
    if(a==3):
        list[2]+=1
    if(a==4):
        list[3]+=1
    if(a==5):
        list[4]+=1
    if(a==6):
        list[5]+=1

list = [0,0,0,0,0,0]

for i in range(6000):
    sayac(list)

first = list[0]
second =list[1]
third = list[2]
fourth =list[3]
fifth = list[4]
sixth = list[5]
print("You have rolled 1 "+first+" times.")
print("You have rolled 2 "+second+" times.")
print("You have rolled 3 "+third+" times.")
print("You have rolled 4 "+fourth+" times.")
print("You have rolled 5 "+fifth+" times.")
print("You have rolled 6 "+sixth+" times.")

