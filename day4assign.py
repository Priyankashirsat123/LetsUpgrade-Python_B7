start = 10242000
end = 702648265

for arm1 in range(start, end + 1):

    exp = len(str(arm1))
    num_sum = 0


    c = arm1
    while c > 0:
        num = c % 10
        num_sum += num ** exp
        c //= 10

        if arm1 != num_sum:
                continue
    else:
        if arm1 == num_sum:
            print("The First Armstrong Number Encountered Is : ",arm1)
            break




"""


##output

The First Armstrong Number Encountered Is :  548834

Process finished with exit code 0

"""