
'''a decorator is just another function which takes a functions and returns one.

'''

# 1 the first decoartor function implemention .
# def repeater(old_function):
#     def new_function(*args, **kws):
#          invoke this function twice
#         old_function(*args, **kws)
#         old_function(*args, **kws)
#
#     return new_function
#
# # this is equivalant to :
# # Mutiply=repeater(MuiltyPly)  --the function turn into a new function in actual, with the same Function Name
#
#
# @repeater
# def Multiply(num1, num2):
#     print num1 * num2
#
#
# Multiply(2, 4)


# # 2 modify the activity in the inner implement.
# def repeater(old_function):
#     def new_function(*args, **kws):
#         # change the return value in inner completion.
#         return 2 * old_function(*args, **kws)
#
#     return new_function
#
# # this is equivalant to :
# # Mutiply=repeater(MuiltyPly)  --the function turn into a new function in actual, with the same Function Name
#
#
# @repeater
# def Multiply(num1, num2):
#     return num1 * num2
#
#
# value = Multiply(2, 4)
# print value

# with decorator to multiply by the default value .
def Multiply(multiplier):
    def Multiply_Generator(old_function):
        def new_function(*args, **kwargs):
            return multiplier * old_function(*args, **kwargs)
        return new_function
    return Multiply_Generator


@Multiply(8)
def Num(num):
    return num


print Num(5)
