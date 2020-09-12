check_list = [1,5,6,4,1,2,3,5]
sub_list = [1,5,6,5,1,2,3,6]
print("Öriginal List : " + str(check_list))
print("Original List : " + str(sub_list))
flag = 0
if (set(sub_list).issubset(set(check_list))):
    flag = 1
if (flag):
    print("ITS A MATCH")
else:
    print("ITS GONE")

"""
  output
  assignment 5.1
Öriginal List : [1, 5, 6, 4, 1, 2, 3, 5]
Original List : [1, 5, 6, 5, 1, 2, 3, 6]
ITS A MATCH
"""

"""
str = ["hii,i am priyanka shirsat,i am from akola ,i am glad to join the letsupgrade team. "]
print(str)

cap = map(lambda x: str.upper(x),str)
print(cap)
"""

def capitalize_names(input):
    return list(map(lambda s: s.capitalize(), input))


















#assisgnment 5.2

def Prime(n):
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range (2,n):
            if (n%x==0):
                return False
            return True







