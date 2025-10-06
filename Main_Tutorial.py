
"""
Why we use main() function in python??????
Actually, in importing our python files or modules there might be some problems that we did not face yet.
In this file we learn how to work with Main() function to avoid these problems.
Can you gues why are in vscode????
"""
# First Step 1
# def Hi():
#     print('Hi, how are you?')

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y   

# Hi()
# print(add(5, 7))
# print(sub(7, 5))

# see this script works correctly

#################################################################################################

# Second Step 2
# def Hi():
#     print('Hi, how are you?')

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y   

# Hi()
# print(add(5, 7))
# print(sub(7, 5))

# print('Done :)')

# this works too

#################################################################################################

"""
Now we want to use this functions in another file so, we need to import this file to Main_Test.py.
"""


"""
So, as you can see there is a big problem here because when we import another python file, python run
all the file first and after that python run commands in this file.

what should we do???

It would be great if there was a flag that we could show Python
and let Python know which file we want to run.

Baaaaaaaaaaam :) name is here.
"""
# print(__name__)

"""
So, after doing these practises you can realize that by defult __name__ is __main__ but, if you import one 
file in another file at first __name__ is the name of the file that is imported(* at running import *) and
after that in file which we run __name__ is __main__.
Please be careful about it.

At last yes __name__ is flag
"""
# Third Step 3
# def Hi():
#     print('Hi, how are you?')

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y 

# if __name__ == '__main__':
#     Hi()
#     print(add(5, 7))
#     print(sub(7, 5))
#     print('Done :)')

# here we go. Now you know what is main() function.

"""
There is one thing that I want to add:
It's better that you write your code in main() function not in if condition due to Global Values
and errors
"""

# Forth Step 4
# def Hi():
#     print('Hi, how are you?')

# def add(x, y):
#     return x + y

# def sub(x, y):
#     print(armin)
#     return x - y 

# if __name__ == '__main__':
#     Hi()
#     print(add(5, 7))
#     print(sub(7, 5))
#     print('Done :)')
#     armin = 'armin'

# run this script and get error without help of the vscode

# Fifth Step 5
# def Hi():
#     print('Hi, how are you?')

# def add(x, y):
#     return x + y

# def sub(x, y):
#     print(armin)
#     return x - y 

# def main():
#     Hi()
#     print(add(5, 7))
#     # armin = 'armin'
#     print(sub(7, 5))
#     print('Done :)')
#     armin = 'armin'

# if __name__ == '__main__':
#     main()

# but here as you can see under armin vscode illustrate error

"""
Also, you can write main function and run all code in importing.
"""
# Sixth Step 6
armin = 'armin'
def Hi():
    print('Hi, how are you?')

def add(x, y):
    return x + y

def sub(x, y):
    return x - y 

def main():
    Hi()
    print(add(5, 7))
    print(sub(7, 5))
    print('Done :)')

if __name__ == 'Main_Tutorial':
    main()

# That's all about main function :)), Good Luck.