
def reverse(num):
    num = num[-1]
    return num

def isitmirror (a,b):
    a = reverse(a)
    b=b
    if(a==b):
        return True
    else:
        return False
    

firstnum = int(input("Enter First Number: "))
secondum = int(input("Enter Second NUmber: "))
mirror= isitmirror(firstnum, secondum)

if(mirror==True):
    print(firstnum +"and" + secondum +"are prime")
else:
    print(firstnum +"and" + secondum +"are not prime")
