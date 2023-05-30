#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?

example_list = [10,15,3,8]
k = 17

def foo(bar_list,num):
    for index1,number1 in enumerate(bar_list):
        for index2,number2 in enumerate(bar_list):
            if index1 != index2 and number1+number2==num:
                return True
    return False 

def bonus(bar_list,num):
    #do it in one pass.
    for number in bar_list:
        goal = num - number
        if goal in bar_list and bar_list.index(goal)!=bar_list.index(number):
            return True
    return False

print(bonus(example_list,k))

